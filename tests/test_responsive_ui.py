"""Focused published CSS contracts, not a browser or a pixel-layout simulator.

Resolve the simple selectors, media queries and named container queries used by
these components. Exercise actual DOM ancestry and component declarations from
the full inline stylesheets, including source order, specificity, !important and
inline declarations. This is a CSS subset, without inheritance or pseudo states. Browser
measurement of line boxes, intrinsic text widths and clipping remains a CDP gate.
"""

import functools
import re
import unittest

import test_course_ui as ui
from test_site_invariants import css_rules, stylesheet, NOSCRIPT_RE


def ancestry(doc, node):
    if not hasattr(doc, "parents"):
        doc.parents = {id(child): parent for parent in doc.nodes for child in parent["children"]}
    parents = doc.parents
    chain = [node]
    while id(chain[0]) in parents:
        chain.insert(0, parents[id(chain[0])])
    return tuple((n["tag"], tuple(sorted(n["attrs"].items()))) for n in chain)


def matches(selector, chain):
    """Compound tag/class/id/attribute selectors and descendant/child relations.

    Interactive pseudo states and pseudo elements are outside this resting-state
    contract. They cannot contribute declarations to the real element here.
    """
    parts = selector.replace(">", " > ").split()

    def compound(part, node):
        tag, attrs = node[0], dict(node[1])
        tokens = re.findall(r'\[[\w-]+(?:=["\'][^"\']*["\'])?\]|[.#][\w-]+|[\w-]+|\*', part)
        if "".join(tokens) != part:
            return False
        for token in tokens:
            if token.startswith(".") and token[1:] not in attrs.get("class", "").split():
                return False
            if token.startswith("#") and token[1:] != attrs.get("id"):
                return False
            if token.startswith("["):
                key, sep, value = token[1:-1].partition("=")
                if key not in attrs or (sep and attrs[key] != value.strip('"\'')):
                    return False
            if token[0] not in ".#[*" and token != tag:
                return False
        return bool(tokens)

    def walk(i, j):
        if j < 0 or not compound(parts[i], chain[j]):
            return False
        if i == 0:
            return True
        if parts[i - 1] == ">":
            return i >= 2 and walk(i - 2, j - 1)
        return any(walk(i - 1, k) for k in range(j - 1, -1, -1))

    return bool(parts) and walk(len(parts) - 1, len(chain) - 1)


def active(context, viewport, container):
    for query in context:
        query = re.sub(r"\s*:\s*", ": ", re.sub(r"@media\s*\(", "@media (", query))
        width = viewport
        if query.startswith("@container lesson-step "):
            if container is None:
                return False
            width = container
            query = query.replace("@container lesson-step ", "@media ", 1)
        if query in ("@media (pointer: coarse)", "@media (hover: none)"):
            continue
        if query in ("@media (prefers-color-scheme: light)",
                     "@media (prefers-reduced-motion: reduce)") or query.startswith("@supports"):
            return False
        bound = re.fullmatch(r"@media \((min|max)-width:\s*([\d.]+)px\)", query)
        if not bound:
            raise AssertionError("responsive contract needs query support: " + query)
        if bound[1] == "min" and width < float(bound[2]):
            return False
        if bound[1] == "max" and width > float(bound[2]):
            return False
    return True


@functools.lru_cache(maxsize=32)
def rules(css):
    return css_rules(css)


@functools.lru_cache(maxsize=8192)
def effective(css, chain, viewport, container=None):
    values, priorities = {}, {}

    def apply(body, specificity, order):
        for declaration in body.split(";"):
            key, sep, value = declaration.partition(":")
            if not sep:
                continue
            key, value = key.strip(), value.strip()
            important = bool(re.search(r"\s*!important$", value))
            value = re.sub(r"\s*!important$", "", value).strip()
            priority = (important, specificity, order)
            keys = ("overflow-x", "overflow-y") if key == "overflow" else (key,)
            for prop in keys:
                if priority >= priorities.get(prop, (False, (-1,), -1)):
                    priorities[prop], values[prop] = priority, value

    for order, (context, selectors, body) in enumerate(rules(css)):
        for selector in selectors.split(","):
            if matches(selector, chain) and active(context, viewport, container):
                specificity = (0, len(re.findall(r"#[\w-]+", selector)),
                               len(re.findall(r"\.[\w-]+|\[", selector)),
                               len(re.findall(r"(?:^|[ >])([a-z][\w-]*)", selector)))
                apply(body, specificity, order)
    apply(dict(chain[-1][1]).get("style", ""), (1, 0, 0, 0), len(rules(css)))
    return values


def px(value):
    if value in (None, "auto", "none"):
        return 0
    if value == "0":
        return 0
    if not re.fullmatch(r"[\d.]+px", value):
        raise AssertionError("expected a pixel size, got " + value)
    return float(value[:-2])


class TestResponsiveUI(unittest.TestCase):
    def pages(self, capability):
        for page in sorted(ui.SITE.rglob("*.html")):
            markup = page.read_text()
            if capability in markup:
                markup = NOSCRIPT_RE.sub("", markup)
                yield page.relative_to(ui.SITE).as_posix(), ui.Elements(markup), stylesheet(markup)

    def test_inline_math_wraps_and_blocks_scroll(self):
        count = 0
        for route, doc, css in self.pages('class="math"'):
            spans = doc.find("span", **{"class": "math"})
            if not spans:
                continue
            count += 1
            # Different ancestor selectors can change otherwise identical spans.
            chains = {ancestry(doc, node) for node in spans}
            for width in (320, 390):
                for chain in chains:
                    style = effective(css, chain, width)
                    self.assertEqual("normal", style.get("white-space"), route + ": inline math must wrap")
                    self.assertEqual("anywhere", style.get("overflow-wrap"), route + ": long math tokens need emergency breaks")
                    self.assertNotEqual("none", style.get("user-select"), route + ": math remains selectable")
                    self.assertNotIn(style.get("overflow-x"), ("hidden", "clip"), route + ": math must not be clipped")
                blocks = doc.find(**{"class": "mathblock"})
                self.assertTrue(blocks, route + ": block-expression guard must run")
                for node in blocks:
                    chain = ancestry(doc, node)
                    style = effective(css, chain, width)
                    self.assertEqual("auto", style.get("overflow-x"), route + ": block math needs local scrolling")
                    if not any(dict(attrs).get("data-ui") == "hero" for _, attrs in chain):
                        self.assertEqual("pre", style.get("white-space"), route + ": block math preserves expression lines")
                for node in doc.find("html") + doc.find("body"):
                    style = effective(css, ancestry(doc, node), width)
                    self.assertNotIn(style.get("overflow-x"), ("hidden", "clip"), route + ": no global overflow masking")
        self.assertGreater(count, 200, "inline math sweep must cover the generated lesson families")

    def test_mobile_signin_hit_box(self):
        count = 0
        for route, doc, css in self.pages('data-ui="masthead"'):
            if not doc.find("header", **{"data-ui": "masthead"}):
                continue
            anchors = doc.find("a", id="signinLink")
            self.assertEqual(1, len(anchors), route + ": actual Sign in anchor")
            count += 1
            for width in (320, 390):
                style = effective(css, ancestry(doc, anchors[0]), width)
                self.assertEqual("inline-flex", style.get("display"), route)
                self.assertEqual("none", style.get("flex"), route + ": hit box must not shrink")
                for axis in ("width", "height"):
                    size = max(px(style.get(axis)), px(style.get("min-" + axis)))
                    self.assertGreaterEqual(size, 44, route + ": Sign in hit box " + axis)
                label = doc.find("span", id="signinLabel")[0]
                self.assertEqual("Sign in", ui.words(label), route + ": accessible label retained")
                label_style = effective(css, ancestry(doc, label), width)
                self.assertEqual("absolute", label_style.get("position"), route + ": compact mobile label")
        self.assertGreater(count, 360, "masthead sweep must cover every course and lesson family")

    def test_button_like_controls_have_minimum_hit_boxes(self):
        count = 0
        for route, doc, css in self.pages('data-page-kind='):
            if not doc.find("body", **{"data-page-kind": "lesson"}):
                continue
            count += 1
            controls = [n for n in doc.nodes if n["tag"] in ("button", "select", "summary")
                        or n["attrs"].get("role") == "button"]
            self.assertTrue(controls, route + ": lesson control sweep must run")
            chains = {ancestry(doc, node) for node in controls}
            # Truth tables and graph matrices create button-role cells at runtime.
            # Exercise their native table display: min-height does not size a cell.
            body = doc.find("body")[0]
            cell = ancestry(doc, body) + (("table", ()), ("tbody", ()), ("tr", ()),
                                         ("td", (("role", "button"),)))
            for width in (320, 390):
                for chain in chains | {cell}:
                    style = effective(css, chain, width)
                    for axis in ("width", "height"):
                        size = px(style.get("min-" + axis))
                        if chain[-1][0] == "td" and axis == "height":
                            size = px(style.get("height"))
                        self.assertGreaterEqual(size, 44, route + ": button-like hit box " + axis)
        self.assertEqual(336, count, "all lessons must enforce control hit boxes")

    def test_lab_grids_respect_their_container(self):
        capabilities = {"grid-2": 0, "kpi-grid": 0}
        for route, doc, css in self.pages('data-page-kind="lesson"'):
            grids = [n for n in doc.nodes if any(c in n["attrs"].get("class", "").split()
                                                for c in capabilities)]
            for node in grids:
                classes = node["attrs"].get("class", "").split()
                if "kpi-grid" in classes:
                    kind, minimum = "kpi-grid", 140
                elif doc.find("table", id="gMatrix"):
                    kind, minimum = "grid-2", 290
                else:
                    continue
                capabilities[kind] += 1
                for width in (320, 390, 1024):
                    style = effective(css, ancestry(doc, node), width)
                    self.assertEqual(
                        f"repeat(auto-fit, minmax(min(100%, {minimum}px), 1fr))",
                        style.get("grid-template-columns"), route + ": lab grid must fit its container")
        self.assertGreaterEqual(capabilities["grid-2"], 14, "graph matrix grid sweep must run")
        self.assertGreater(capabilities["kpi-grid"], 100, "lab metric grid sweep must run")

    def test_lesson_cards_use_available_width(self):
        count = 0
        for route, doc, css in self.pages('class="course-step"'):
            steps = doc.find(**{"class": "course-step"})
            if not steps:
                continue
            count += 1
            shell = doc.find(**{"class": "shell"})[0]
            track = doc.find(**{"class": "course-track"})[0]
            # Include media boundaries and the parent's scrollbar-reduced tablet.
            for viewport, client in ((768, 753), (320, 320), (390, 390), (720, 705), (721, 706),
                                     (759, 744), (760, 745), (1024, 1009), (1440, 1425)):
                shell_style = effective(css, ancestry(doc, shell), viewport)
                self.assertEqual("min(1160px, calc(100% - 32px))", shell_style.get("width"), route)
                grid = effective(css, ancestry(doc, track), viewport)
                columns = grid.get("grid-template-columns")
                self.assertIn(columns, ("minmax(0, 1fr)", "repeat(2, minmax(0, 1fr))"), route)
                ncols = 2 if columns.startswith("repeat") else 1
                available = (min(1160, client - 32) - px(grid.get("gap")) * (ncols - 1)) / ncols
                if viewport == 768:
                    self.assertEqual(351.5, available, "reproduce the parent's effective tablet card width")
                for step in steps:
                    step_style = effective(css, ancestry(doc, step), viewport)
                    container = available if (step_style.get("container-type") == "inline-size"
                                              and step_style.get("container-name") == "lesson-step") else None
                    card = next(n for n in step["children"] if "lesson-card" in n["attrs"].get("class", "").split())
                    card_style = effective(css, ancestry(doc, card), viewport, container)
                    thumb = next(n for n in card["children"] if n["attrs"].get("class") == "thumb")
                    thumb_style = effective(css, ancestry(doc, thumb), viewport, container)
                    self.assertEqual("hidden", card_style.get("overflow-x"), route + ": retain deliberate card clipping")
                    if available <= 560 or viewport < 760:
                        self.assertEqual("column", card_style.get("flex-direction"), route + ": narrow card must stack at " + str(viewport))
                        self.assertIn(thumb_style.get("width", "auto"), ("auto", "100%"), route + ": stacked thumbnail must fit its card")
                        self.assertEqual("0", thumb_style.get("border-right", "0"), route + ": stacked thumbnail has no side divider")
                        self.assertEqual("1px solid var(--line)", thumb_style.get("border-bottom"), route)
                    else:
                        self.assertEqual("row", card_style.get("flex-direction"), route + ": preserve wide desktop rows")
                        self.assertEqual("296px", thumb_style.get("width"), route + ": preserve desktop thumbnail")
                    self.assertEqual("inline-size", step_style.get("container-type"), route + ": query needs a sized ancestor")
                    self.assertEqual("lesson-step", step_style.get("container-name"), route + ": query must name the step ancestor")
        self.assertEqual(8, count, "all authored course tracks must exercise the effective-width guard")
