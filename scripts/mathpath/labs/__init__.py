"""The lab registry.

A lesson names a lab by key and hands it a config. Adding a lab means adding a
function here; a lesson can never inline its own widget, which is the rule that
keeps 106 lessons from becoming 106 slightly different implementations of the
same control.
"""

from . import (
    algebra_basics,
    argkit,
    choicekit,
    algebra_equations,
    algebra_expo,
    algebra_functions,
    algebra_polynomials,
    algebra_quadratic,
    algebra_rational,
    algebra_systems,
    algorithms,
    avail,
    birthdeath,
    cache,
    coping,
    counting,
    dpseq,
    dpkit,
    duality,
    estimate,
    flowkit,
    geometry,
    graph,
    graphkit,
    greedy,
    hash,
    heap,
    induction,
    integer,
    inventory,
    latency,
    logic,
    lp,
    markov,
    measure,
    network,
    number,
    probability,
    queue,
    random,
    reduction,
    replica,
    scale,
    schedule,
    seqkit,
    sets,
    shard,
    simplex,
    simulate,
    sortkit,
    storage,
    strings,
    english,
    transport,
    tree,
)
from .common import QUIZ_MARKUP, QUIZ_SCRIPT, Lab, cfg_literal

REGISTRY = {
    "truth_table": logic.truth_table,
    "quantifier": logic.quantifier,
    "sets": sets.set_lab,
    "relation": sets.relation_lab,
    "function": sets.function_lab,
    "counting": counting.counting_lab,
    "pascal": counting.pascal_lab,
    "inclusion_exclusion": counting.inclusion_exclusion,
    "derangement": counting.derangement_lab,
    "induction": induction.induction_lab,
    "recurrence": induction.recurrence_lab,
    "number": number.number_lab,
    "rsa": number.rsa_lab,
    "graph": graph.graph_lab,
    "probability": probability.probability_lab,
    "distribution": probability.distribution_lab,
    "bayes": probability.bayes_lab,
    "algorithm": algorithms.algorithm_lab,

    # The algebra path. Its labs share the exact-arithmetic core in
    # algebra_core.py: rationals over BigInt, polynomials over those
    # rationals, an expression parser for what a reader types, and an SVG
    # grapher that samples the function rather than storing a shape.
    "expression": algebra_basics.expression_lab,
    "realline": algebra_basics.realline_lab,
    "exponents": algebra_basics.exponents_lab,
    "radicals": algebra_basics.radicals_lab,
    "equation": algebra_equations.equation_lab,
    "inequality": algebra_equations.inequality_lab,
    "expo": algebra_expo.expo_lab,
    "logarithm": algebra_expo.logarithm_lab,
    "line": algebra_functions.line_lab,
    "grapher": algebra_functions.grapher_lab,
    "transform": algebra_functions.transform_lab,
    "funcops": algebra_functions.funcops_lab,
    "polynomial": algebra_polynomials.polynomial_lab,
    "factoring": algebra_polynomials.factoring_lab,
    "rationalfn": algebra_rational.rationalfn_lab,
    "complex": algebra_rational.complex_lab,
    "system": algebra_systems.system_lab,
    "matrix": algebra_systems.matrix_lab,
    "sequence": algebra_systems.sequence_lab,
    "quadratic": algebra_quadratic.quadratic_lab,

    # The System Design path. Its labs share the exact engine in
    # sysdesign_core.py on top of algebra_core's rationals: one kit per
    # course, with the mode chosen by cfg["mode"].
    "estimate": estimate.estimate_lab,
    "latency": latency.latency_lab,
    "cache": cache.cache_lab,
    "queue": queue.queue_lab,
    "avail": avail.avail_lab,
    "replica": replica.replica_lab,
    "shard": shard.shard_lab,
    "storage": storage.storage_lab,
    "scale": scale.scale_lab,
    "measure": measure.measure_lab,

    # The Operations Research path. Its kits share the exact simplex in
    # or_core.py; courses 4 and 9 take two kits each, which is a stated
    # exception to one-kit-per-course because a drawing and a tableau
    # cannot share a mode.
    "lp": lp.lp_lab,
    "simplex": simplex.simplex_lab,
    "duality": duality.duality_lab,
    "network": network.network_lab,
    "transport": transport.transport_lab,
    "integer": integer.integer_lab,
    "simulate": simulate.simulate_lab,
    "schedule": schedule.schedule_lab,
    "dpseq": dpseq.dpseq_lab,
    "inventory": inventory.inventory_lab,
    "markov": markov.markov_lab,
    "birthdeath": birthdeath.birthdeath_lab,

    # The Algorithms path, over algo_core.py. A kit concatenates only the
    # blocks it needs: the whole core is 68 KB gzipped, above the page
    # ceiling on its own.
    "seqkit": seqkit.seqkit_lab,
    "heap": heap.heap_lab,
    "hash": hash.hash_lab,
    "tree": tree.tree_lab,
    "sortkit": sortkit.sortkit_lab,
    "graphkit": graphkit.graphkit_lab,
    "flowkit": flowkit.flowkit_lab,
    "greedy": greedy.greedy_lab,
    "dpkit": dpkit.dpkit_lab,
    "random": random.random_lab,
    "reduction": reduction.reduction_lab,
    "coping": coping.coping_lab,
    "strings": strings.strings_lab,
    "english": english.english_lab,
    "geometry": geometry.geometry_lab,
    "argkit": argkit.argkit_lab,
    "choicekit": choicekit.choicekit_lab,
}


def build(key, cfg):
    if key not in REGISTRY:
        raise KeyError("no lab named %r; known labs: %s" % (key, ", ".join(sorted(REGISTRY))))
    return REGISTRY[key](cfg or {})


__all__ = ["REGISTRY", "build", "Lab", "QUIZ_MARKUP", "QUIZ_SCRIPT", "cfg_literal"]
