#!/usr/bin/env python3
"""Prove the UI guards reject broken output, using copies and temporary mocks.

Run from the repository root with /usr/bin/python3 tests/mutate_course_ui.py.
No source or published file in the worktree is changed by this runner.
"""

import contextlib
import copy
import io
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import test_course_ui as ui
import test_site_invariants as invariants
import intake_course


@contextlib.contextmanager
def output(obj, name, rewrite):
    original = getattr(obj, name)
    with mock.patch.object(obj, name, side_effect=lambda *a, **kw: rewrite(original(*a, **kw))):
        yield


def replace(old, new):
    def rewrite(value):
        if old not in value:
            raise RuntimeError("mutation anchor missing: " + old)
        return value.replace(old, new)
    return rewrite


def run(label, case, mutation, expected=None):
    result = unittest.TestResult()
    with mutation, contextlib.redirect_stdout(io.StringIO()):
        unittest.TestSuite([case]).run(result)
    if result.errors or not result.failures:
        raise AssertionError("mutation was not caught by an assertion: " + label + repr(result.errors))
    detail = result.failures[0][1].split("AssertionError: ")[-1].splitlines()[0]
    if expected and expected not in result.failures[0][1]:
        raise AssertionError("mutation hit the wrong guard: " + label + result.failures[0][1])
    print("CAUGHT " + label + ": " + detail[:160], flush=True)


@contextlib.contextmanager
def page_mutation(site, relative, rewrite):
    target = site / relative
    before = target.read_text()
    target.write_text(rewrite(before))
    try:
        yield
    finally:
        target.write_text(before)


def main():
    with tempfile.TemporaryDirectory(prefix="learn-ui-mutations-") as tmp:
        site = Path(tmp) / "site"
        shutil.copytree(ui.SITE, site)
        with mock.patch.object(ui, "SITE", site), mock.patch.object(invariants, "SITE_ROOT", site):
            run("published regions", ui.TestPublishedUI("test_every_page_family_exposes_the_shared_contract"),
                page_mutation(site, "index.html", replace('data-ui="hero"', 'data-ui="missing"')))
            run("published taxonomy", ui.TestVisitorTaxonomy("test_published_copy_uses_subjects_and_course_titles"),
                page_mutation(site, "index.html", replace("<h1", "<p>Course 3</p><h1")))
            run("library and search", ui.TestLibraryUI("test_library_browses_subjects_and_search_reports_subject_names"),
                page_mutation(site, "index.html", replace("Learn library</h1>", "Learning paths</h1>")))
            run("dynamic search taxonomy", ui.TestLibraryUI("test_library_browses_subjects_and_search_reports_subject_names"),
                page_mutation(site, "index.html", replace("metaItem(course.path)", "metaItem(course.position)")))
            run("literal Trading identity", ui.TestTradingNormalization("test_published_trading_names_are_literal"),
                page_mutation(site, "market-structure/market-structure/index.html",
                              lambda s: re.sub(r"<title>.*?</title>", "<title>Wrong identity</title>", s)))
            run("pinned lesson pager", invariants.TestPinnedConventions("test_every_lesson_carries_the_pinned_pager_markup"),
                page_mutation(site, "market-structure/market-structure/index.html", replace('data-ui="lesson-navigation"', 'data-ui="wrong-navigation"')))
            run("subject context", invariants.TestCourseContext("test_every_course_home_declares_subject_and_page_kind"),
                page_mutation(site, "market-structure/index.html", replace('data-ui="page-kind">Course', 'data-ui="page-kind">Module')))
            run("library vocabulary", invariants.TestSharedChromeIsSubjectAgnostic("test_site_index_copy_uses_subject_taxonomy"),
                page_mutation(site, "index.html", replace("<h1", "<p>Browse paths</p><h1")))

        render = ui.build_paths.render
        run("lesson ancestry", ui.TestGeneratedLessonUI("test_lesson_hierarchy"),
            output(render, "lesson_page", replace(">Learn library</a>", ">Home</a>")))
        run("understanding criterion heading", ui.TestGeneratedLessonUI("test_understanding_and_terminal_navigation"),
            output(render, "lesson_page", replace("Check your understanding", "Completion standard")))
        run("masthead control order", ui.TestSharedMasthead("test_navigation_and_control_order"),
            output(ui.chrome, "topbar", replace('id="signinLink"', 'id="wrongControl"')))
        run("subject cards", ui.TestGeneratedCatalogUI("test_subject_catalog_has_unnumbered_courses"),
            output(render, "path_page", replace('data-ui="page-kind">Subject', 'data-ui="page-kind">Path')))
        run("course anatomy", ui.TestGeneratedCatalogUI("test_course_overview_has_factual_identity_and_optional_navigation"),
            output(render, "course_home", replace("Recommended background", "Required course order")))
        run("readable completion state", ui.TestMarkLabels("test_course_marks_have_readable_state"),
            mock.patch.object(ui.progress, "COURSE_JS", ui.progress.COURSE_JS.replace("Marked complete", "Done")))
        run("fresh intake", ui.TestTradingIntakeUI("test_intake_breadcrumb_and_terminal_return"),
            output(intake_course, "build_breadcrumb", replace("Learn library", "Home")))

        run("taxonomy scanner boundary", ui.TestVisitorTaxonomy("test_visible_copy_separates_adjacent_elements"),
            mock.patch.object(ui.TestVisitorTaxonomy, "ORDINAL", re.compile(r"cannot-match-this-copy")))
        bad_paths=copy.deepcopy(ui.build_paths.GENERATED_PATHS)
        algebra=next(p for p in bad_paths if p["slug"]=="algebra")
        course=next(c for c in algebra["courses"] if c["slug"]=="exponential-and-logarithmic-functions")
        course["lessons"][-1]["note"]=course["lessons"][-1]["note"].replace("Sequences and Series", "Systems and Matrices")
        run("reference topic", ui.TestVisitorTaxonomy("test_generated_cross_references_use_titles_and_topics"),
            mock.patch.object(ui.build_paths, "GENERATED_PATHS", bad_paths))

        trading = ui.trading
        run("legacy teaching preservation", ui.TestTradingNormalization("test_legacy_shells_preserve_domain_copy_and_hero_controls"),
            output(trading, "prepare_lesson", lambda s: s.replace("Keep the trading path explicit", "Keep the subject explicit")))
        run("palette and touch controls", ui.TestTradingNormalization("test_legacy_palette_and_hero_controls_support_shared_styles"),
            output(trading, "ensure_css", replace("--on-accent:", "--wrong-accent:")))
        run("entity decoding", ui.TestTradingNormalization("test_authored_inventory_names_are_decoded_once"),
            output(trading, "strip_tags", lambda s: s.replace("&", "&amp;")))
        run("authored catalog authority", ui.TestTradingNormalization("test_normalized_catalog_prose_remains_authored"),
            output(trading, "normalize_course_ui", lambda s: s.replace("Authored factual overview retained on later runs.", "Discarded authored copy.")))
        run("card completion placement", ui.TestTradingNormalization("test_trading_lesson_state_is_inside_the_card_content"),
            output(trading, "ensure_course_hooks", replace('<span class="lesson-state">Not marked</span>', '')))
        run("incomplete inventory preflight", ui.TestTradingNormalization("test_incomplete_inventory_is_rejected_before_transformation"),
            mock.patch.object(trading, "main", return_value=None))
        run("Trading catalog parity", ui.TestTradingNormalization("test_course_and_subject_catalog_contract"),
            output(trading, "normalize_course_ui", replace('data-page-kind="course"', 'data-page-kind="module"')))

        original = trading.prepare_lesson

        def premature_write(before, relative, *args):
            result = original(before, relative, *args)
            (trading.SITE / relative).write_text(result)
            return result

        run("atomic preflight", ui.TestTradingNormalization("test_failed_preflight_writes_nothing"),
            mock.patch.object(trading, "prepare_lesson", side_effect=premature_write))
        run("Trading lesson parity", ui.TestTradingNormalization("test_lesson_shell_preserves_instruction_and_is_idempotent"),
            output(trading, "prepare_lesson", replace('data-page-kind="lesson"', 'data-page-kind="module"')))
    print("26/26 UI guard mutations caught; worktree inputs untouched.", flush=True)


def progress_mutations():
    """Exercise each new progress UI assertion against a rebuilt copied page."""
    cases = [
        ("completion is described as marks", "Courses fully marked", "Courses finished"),
        ("subject catalog totals are not displayed", "<h1>Your progress</h1>",
         '<h1>Your progress</h1><span id="statPaths">3</span>'),
        ("aggregate footer has no algebra warning", "<h1>Your progress</h1>",
         '<h1>Your progress</h1><p>a step that gives the right answer here</p>'),
        ("course rows have no ordinal badges", '<span><span class="pg-course-name">',
         '<span class="pg-num">3</span><span><span class="pg-course-name">'),
        ("subject headings link to subject courses", 'href="../paths/', 'href="../subjects/'),
    ]
    with tempfile.TemporaryDirectory(prefix="learn-progress-mutations-") as tmp:
        root = Path(tmp)
        for area in ("scripts", "content", "site"):
            shutil.copytree(ui.ROOT / area, root / area)
        builder = root / "scripts/build_auth_pages.py"
        original = builder.read_text()
        for label, old, new in cases:
            builder.write_text(replace(old, new)(original))
            result = subprocess.run(["node", str(root / "scripts/progresscheck.js")],
                                    capture_output=True, text=True)
            if result.returncode != 1 or "FAIL  UI: " + label not in result.stdout:
                raise AssertionError("progress mutation escaped its guard: " + label + result.stderr)
            print("CAUGHT progress: " + label, flush=True)
    print("5/5 progress UI mutations caught; worktree inputs untouched.", flush=True)


def responsive_mutations():
    """Late live overrides must beat safe declarations, comments and dead media."""
    from test_responsive_ui import TestResponsiveUI
    math = "algebra-foundations/absolute-value/index.html"
    trading = "algorithmic-and-automated-trading/index.html"
    cases = [
        ("inline math nowrap", math, "test_inline_math_wraps_and_blocks_scroll",
         '.math { white-space: nowrap !important; } /* .math { white-space: normal; } */',
         "inline math must wrap"),
        ("unbreakable math token", math, "test_inline_math_wraps_and_blocks_scroll",
         '.math { overflow-wrap: normal !important; }', "long math tokens need emergency breaks"),
        ("block math clipped", math, "test_inline_math_wraps_and_blocks_scroll",
         '.mathblock { overflow: hidden !important; }', "block math needs local scrolling"),
        ("global overflow masking", math, "test_inline_math_wraps_and_blocks_scroll",
         'html { overflow-x: hidden; }', "no global overflow masking"),
        ("generated Sign in width", math, "test_mobile_signin_hit_box",
         '#signinLink { min-width: 0; width: 40px; } '
         '@media (min-width: 900px) { #signinLink { min-width: 44px; } }', "Sign in hit box width"),
        ("Trading Sign in width", trading, "test_mobile_signin_hit_box",
         '#signinLink { min-width: 0; width: 38px; }', "Sign in hit box width"),
        ("Sign in height", math, "test_mobile_signin_hit_box",
         '#signinLink { min-height: 0; height: 40px; }', "Sign in hit box height"),
        ("lab button width", math, "test_button_like_controls_have_minimum_hit_boxes",
         'button { min-width: 0 !important; }', "button-like hit box width"),
        ("lab select height", math, "test_button_like_controls_have_minimum_hit_boxes",
         'select { min-height: 0 !important; }', "button-like hit box height"),
        ("interactive table cell height", math, "test_button_like_controls_have_minimum_hit_boxes",
         'td[role="button"] { height: auto !important; }', "button-like hit box height"),
        ("graph grid fixed minimum", "graphs-and-trees/graphs-and-graph-models/index.html",
         "test_lab_grids_respect_their_container",
         '.grid-2 { grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)) !important; }',
         "lab grid must fit its container"),
        ("metric grid forced columns", "technical-indicators/average-true-range/index.html",
         "test_lab_grids_respect_their_container",
         '.kpi-grid { grid-template-columns: repeat(4, minmax(0, 1fr)) !important; }',
         "lab grid must fit its container"),
        ("tablet horizontal card", trading, "test_lesson_cards_use_available_width",
         '@media (min-width: 760px) { [data-ui="lesson-list"] .course-step .lesson-card '
         '{ flex-direction: row; } }', "narrow card must stack at 768"),
        ("tablet fixed thumbnail", trading, "test_lesson_cards_use_available_width",
         '[data-ui="lesson-list"] .course-step .thumb { width: 296px; }', "stacked thumbnail must fit its card"),
        ("missing query ancestor", trading, "test_lesson_cards_use_available_width",
         '[data-ui="lesson-list"] .course-step { container-type: normal; }', "narrow card must stack at 768"),
        ("lost desktop row", trading, "test_lesson_cards_use_available_width",
         '[data-ui="lesson-list"] .course-step .lesson-card { flex-direction: column; }', "preserve wide desktop rows"),
    ]
    with tempfile.TemporaryDirectory(prefix="learn-responsive-mutations-") as tmp:
        site = Path(tmp) / "site"
        shutil.copytree(ui.SITE, site)
        with mock.patch.object(ui, "SITE", site):
            for label, page, test, css, expected in cases:
                run(label, TestResponsiveUI(test), page_mutation(site, page,
                    replace("</head>", "<style>" + css + "</style></head>")), expected=expected)
    print(f"{len(cases)}/{len(cases)} responsive mutations caught; worktree inputs untouched.", flush=True)


if __name__ == "__main__":
    if "--responsive-only" in sys.argv:
        responsive_mutations()
    elif "--progress-only" in sys.argv:
        progress_mutations()
    else:
        main()
        progress_mutations()
        responsive_mutations()
