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


def split_selector(value, relations=False):
    """Split only at the top level, respecting functions and attribute strings."""
    parts, buf, depth, bracket, quote = [], [], 0, 0, None
    for char in value:
        if quote:
            buf.append(char)
            if char == quote:
                quote = None
            continue
        if char in "\"'":
            quote = char
        elif char == "[":
            bracket += 1
        elif char == "]":
            bracket -= 1
        elif not bracket and char == "(":
            depth += 1
        elif not bracket and char == ")":
            depth -= 1
        if not depth and not bracket and not quote and (
                (relations and (char.isspace() or char == ">")) or (not relations and char == ",")):
            if "".join(buf).strip():
                parts.append("".join(buf).strip())
            buf = []
            if char == ">":
                parts.append(char)
        else:
            buf.append(char)
    if depth or bracket or quote:
        raise AssertionError("unbalanced selector: " + value)
    if "".join(buf).strip():
        parts.append("".join(buf).strip())
    return parts


@functools.lru_cache(maxsize=4096)
def selector_tree(selector):
    """Supported static selector AST; unsupported pseudo states exclude a rule.

    Excluding the whole selector also prevents :not(:hover) from spuriously
    matching when hover is outside this contract's state model.
    """
    result = []
    for part in split_selector(selector, relations=True):
        if part == ">":
            result.append(part)
            continue
        tokens, i = [], 0
        while i < len(part):
            simple = re.match(r'\[[\w-]+(?:=(?:"[^"]*"|\'[^\']*\'|[\w-]+))?\]|[.#][\w-]+|[\w-]+|\*', part[i:])
            if simple:
                tokens.append(simple[0]); i += len(simple[0]); continue
            function = re.match(r':(is|where|not)\(', part[i:])
            if not function:
                return None
            start = i + len(function[0]); j, depth, quote, bracket = start, 1, None, 0
            while j < len(part) and depth:
                c = part[j]
                if quote:
                    if c == quote: quote = None
                elif c in "\"'": quote = c
                elif c == "[": bracket += 1
                elif c == "]": bracket -= 1
                elif not bracket and c == "(": depth += 1
                elif not bracket and c == ")": depth -= 1
                j += 1
            if depth:
                raise AssertionError("unbalanced functional selector: " + part)
            arguments = tuple(selector_tree(arg) for arg in split_selector(part[start:j-1]))
            if not arguments or any(arg is None for arg in arguments):
                return None
            tokens.append((function[1], arguments)); i = j
        if not tokens:
            return None
        result.append(tuple(tokens))
    return tuple(result)


def tree_specificity(tree):
    total = [0, 0, 0, 0]
    for part in tree:
        if part == ">": continue
        for token in part:
            if isinstance(token, tuple):
                name, args = token
                score = (0, 0, 0, 0) if name == "where" else max(tree_specificity(arg) for arg in args)
                total = [a+b for a, b in zip(total, score)]
            elif token.startswith("#"): total[1] += 1
            elif token.startswith((".", "[")): total[2] += 1
            elif token != "*": total[3] += 1
    return tuple(total)


def tree_matches(tree, chain):
    def compound(tokens, at):
        tag, attrs = chain[at][0], dict(chain[at][1])
        for token in tokens:
            if isinstance(token, tuple):
                name, args = token
                found = any(tree_matches(arg, chain[:at+1]) for arg in args)
                if found == (name == "not"): return False
            elif token.startswith("."):
                if token[1:] not in attrs.get("class", "").split(): return False
            elif token.startswith("#"):
                if token[1:] != attrs.get("id"): return False
            elif token.startswith("["):
                key, sep, value = token[1:-1].partition("=")
                if key not in attrs or (sep and attrs[key] != value.strip('"\'')): return False
            elif token != "*" and token != tag:
                return False
        return True

    def walk(i, j):
        if j < 0 or tree[i] == ">" or not compound(tree[i], j): return False
        if i == 0: return True
        if tree[i-1] == ">": return i >= 2 and walk(i-2, j-1)
        return any(walk(i-1, k) for k in range(j-1, -1, -1))
    return bool(tree) and walk(len(tree)-1, len(chain)-1)


def matches(selector, chain):
    tree = selector_tree(selector)
    return tree is not None and tree_matches(tree, chain)


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
        for selector in split_selector(selectors):
            if matches(selector, chain) and active(context, viewport, container):
                specificity = tree_specificity(selector_tree(selector))
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
