"""wonkit_core -- the seam shared by the two families of wonkit, the lab kit
of The Wealth of Nations, Read Along.

Specified in docs/wealth-of-nations/PLAN.md section D. Family A is
wonkit.py (Book I modes, and the kit's entry point `wonkit_lab`); family B is
wonkit_b.py (Books II to V). Both build every view through `mode_lab` below.

This module is acckit's machinery under another name. It reuses, unchanged:

  - eakit_core (as `ea`): the field parser, printers, markup and wiring;
  - acckit's field kinds (`arec`, `alist`, `rat`), its preset reader and its
    `aktRead` wiring, so a wonkit page reads its boxes exactly as an acckit
    page does, and AKT_CORE_JS, whose exact helpers (aktDec, aktParseRat,
    aktSqrtFixed, aktUnit, aktTimes ...) a view may call. A wonkit view never
    calls aktStatus: its caution is the Accelerate one. Use wnkStatus.

What is wonkit's own is the family sentence, the caution every status line
ends with, WNK_CORE_JS (helpers beginning wnk / WNK_, defined only here) and
the KIT name in every error message.

THE BUILDER SIGNATURE (both families). A mode is built by
`builder(cfg) -> common.Lab`; every builder is
`lambda cfg: mode_lab(cfg, <mode>, <SPEC>)`, SPEC shaped exactly as
docs/accelerate/kit-contract.md section 2 describes (prefix, fn, title, js,
views; a view has fields, tiles, check, subtitle, rules, js, options). A page
ships RATIONAL_JS, EA_CORE_JS, AKT_CORE_JS, WNK_CORE_JS, its mode's block and
its own view's block -- never another view's or mode's.
"""

from . import eakit_core as ea
from .acckit import (AKT_CORE_JS, _COMMENT_LINES, _WIRE_JS, _presets, alist, arec, dec_text, num_text,
                     parse_dec, parse_field, parse_rat, pp_text, rat, to_text, unit_text)
from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal

KIT = "wonkit"
CAUTION = "it follows from the figures stated, not from any economy's records"
FAMILY_SENTENCE = "A figure computed from the quantities the lesson states."

WNK_CORE_JS = r"""
  /* wonkit's shared helpers (docs/wealth-of-nations/PLAN.md section D.0). */
  var WNK_CAUTION = 'it follows from the figures stated, not from any economy’s records';
  function wnkStatus(s) { return String(s).replace(/[.\s]+$/, '') + '; ' + WNK_CAUTION + '.'; }
"""


def family_intro():
    return (FAMILY_SENTENCE + " It shows what Smith's reasoning in the chapter implies for those quantities; "
            "his own figures are his, of his century, and the lab neither checks them nor tests the argument.")


def _no_options(cfg, kit, tiles):
    return {}, [], tiles


def _build_lab(cfg, *, kit, prefix, view, fields, tiles, fn, js, fixed, title, subtitle, intro, rules, extra_keys=(),
               check=None):
    """acckit._build_lab with wonkit's family sentence."""
    allowed = ea.COMMON_CFG | set(extra_keys) | {key for key, _s, _d in fields}
    stray = sorted(set(cfg) - allowed)
    if stray:
        raise ValueError("%s: cfg sets %s, which this view does not take (it takes %s)"
                         % (kit, ", ".join(stray), ", ".join(sorted(allowed))))
    table, menu, expect, chosen = _presets(cfg, kit, fields, tiles, check, fixed)
    here = table[chosen]
    spec, controls = [], ea.select_html(prefix + "Preset", "Worked example", menu, chosen)
    for key, fspec, _default in fields:
        cid = ea.camel(prefix, key)
        spec.append(dict(fspec, key=key, id=cid))
        if fspec["control"] == "select":
            controls += ea.select_html(cid, fspec["what"], [(w, w) for w in fspec["words"]], here[key])
        elif fspec["control"] == "area":
            controls += ea.area_html(cid, fspec["what"], here[key], fspec.get("rows", 3))
        else:
            controls += ea.text_html(cid, fspec["what"], here[key])
    controls += ea.kpis_html(tiles)
    ids = [s["id"] for s in spec] + [cid for _l, cid in tiles] + [prefix + x for x in ("Preset", "Status", "Table")]
    if len(set(ids)) != len(ids):
        raise ValueError("%s: two controls or tiles share an id: %s" % (kit, sorted({i for i in ids if ids.count(i) > 1})))
    script = (RATIONAL_JS + ea.EA_CORE_JS + js
              + cfg_literal("PRESETS", table) + cfg_literal("SPEC", spec)
              + cfg_literal("TILES", [cid for _label, cid in tiles])
              + cfg_literal("FIXED", fixed) + cfg_literal("VIEW", view)
              + _WIRE_JS.replace("%P%", prefix).replace("%FN%", fn))
    script = _COMMENT_LINES.sub("", script)
    panel_intro = ea.plain(cfg, kit, "panel_intro", intro, limit=1200)
    if FAMILY_SENTENCE not in panel_intro:
        panel_intro = FAMILY_SENTENCE + " " + panel_intro
    title = ea.plain(cfg, kit, "title", title)
    return Lab(title=title, subtitle=subtitle,
               markup=ea.markup_html(prefix, title, subtitle, rules), controls=controls, script=script,
               panel_title=ea.plain(cfg, kit, "panel_title", "Change the inputs, or choose a worked example"),
               panel_intro=panel_intro, expect={prefix + "Preset": expect})


def mode_lab(cfg, mode, spec):
    """One wonkit mode as a Lab, from its spec dict."""
    views = spec["views"]
    order = tuple(views)
    view = cfg.get("view", order[0])
    if view not in views:
        raise ValueError("%s/%s: unknown view %r; the views are %s" % (KIT, mode, view, ", ".join(order)))
    kit = "%s/%s/%s" % (KIT, mode, view)
    v = views[view]
    fixed, keys, tiles = v.get("options", _no_options)(cfg, kit, v["tiles"])
    for _label, cid in tiles:
        if not cid.startswith(spec["prefix"]):
            raise ValueError("%s: tile id %r does not begin with the prefix %r" % (kit, cid, spec["prefix"]))
    return _build_lab(cfg, kit=kit, prefix=spec["prefix"], view=view, fields=v["fields"], tiles=tiles,
                      fn=spec["fn"], js=AKT_CORE_JS + WNK_CORE_JS + spec["js"] + v["js"], fixed=fixed,
                      title=spec["title"], subtitle=v["subtitle"], intro=family_intro(), rules=v["rules"],
                      extra_keys=keys, check=v["check"])


__all__ = ["mode_lab", "family_intro", "KIT", "CAUTION", "FAMILY_SENTENCE", "WNK_CORE_JS", "AKT_CORE_JS",
           "arec", "alist", "rat", "parse_field", "to_text", "parse_dec", "parse_rat", "dec_text", "num_text",
           "unit_text", "pp_text", "ea"]
