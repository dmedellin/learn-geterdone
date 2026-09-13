"""Storage Engines and Indexes."""


from . import part_a, part_b


COURSE = {
    "slug": "storage-engines-and-indexes",
    "title": "Storage Engines and Indexes",
    "level": "Intermediate",
    "summary": (
        "The bargain every storage engine makes, counted: seeks against bytes, tree "
        "levels against fanout, bytes rewritten per byte ingested, bits per key for a "
        "Bloom filter, fsyncs per second, and the recovery window a backup schedule "
        "implies."
    ),
    "blurb": (
        "Every storage engine is a bargain between reads, writes and space, and the "
        "bargain is countable: seeks against bytes, tree levels against fanout, bytes "
        "rewritten per byte ingested, bits per key for a Bloom filter, fsyncs per "
        "second. The course prices each structure so that &ldquo;use an LSM&rdquo; or "
        "&ldquo;add an index&rdquo; becomes a number a designer can defend."
    ),
    "key": [
        "time = seeks × t_seek + bytes/bandwidth      the pattern, not the size",
        "height = ⌈log_B N⌉                           a billion keys at B = 500 is four",
        "k indexes  ⟹  k + 1 random writes an insert",
        "WA ≈ L·F/2        RA ≈ L before filters",
        "bits/key ≈ log₂(1/p) / ln 2                  independent of n",
        "durable writes/s ≤ 1/t_fsync,  or B/t_fsync grouped",
    ],
    "assumes_short": "Capacity Estimation and Caching and Hit Rates; trees, logarithms, independence",
    "assumes_long": (
        "capacity estimation and caching and hit rates on this path; discrete "
        "mathematics: trees, independence, recursion-trees-and-amortised-analysis, "
        "big-o-notation; algebra: what-a-logarithm-is, change-of-base, the-number-e"
    ),
    "outcomes_intro": (
        "By the end you can price a read and a write against the structure that serves "
        "them, compute the amplification an LSM pays for its sequential writes, size the "
        "filter that cancels most of it, and say what your backup schedule means in "
        "bytes and in hours."
    ),
    "outcomes": [
        ("Price an access pattern",
         "The crossover between sequential and random I/O for a stated seek time and "
         "bandwidth, a B-tree&rsquo;s height and the I/Os a lookup and a range scan cost, "
         "and the I/O count of a workload mix on a hash index against a tree."),
        ("Price a write",
         "The `k + 1` random writes an insert costs with `k` indexes, the write "
         "amplification of a levelled LSM at a given fanout, and the compaction bandwidth "
         "that amplification implies."),
        ("Size a Bloom filter for an engine",
         "Bits per key at a target false-positive rate, the memory that costs for `n` "
         "keys, and the read amplification a filter on every level turns `L` into."),
        ("State the recovery and durability bargain",
         "The RUM triple for three engine shapes, the durable write rate a single fsync "
         "allows and what grouping buys, and the RPO and RTO a backup schedule and a "
         "restore bandwidth imply."),
    ],
    "syllabus_intro": (
        "The physics first &mdash; what a seek costs and what a tree height is &mdash; "
        "then the write side, then the filter and the trade-off the course is named "
        "after, and last what a running engine owes its hardware: the fsync, the layout, "
        "the page cache and the recovery window."
    ),
    "how_to": [
        "Convert everything into I/Os before comparing structures. Bytes and seconds "
        "make two engines look similar; I/O counts make the bargain visible, and every "
        "lab on this course reports in them.",
        "Compute the amplification before the latency. Write amplification decides how "
        "much disk bandwidth you need and therefore whether the latency question is even "
        "interesting &mdash; an engine whose compaction cannot keep up has no steady "
        "latency to quote.",
        "Take &ldquo;Working Set and the Page Cache&rdquo; as a callback rather than as "
        "new material. It is the cache of Caching and Hit Rates under different names, "
        "and the point of it is that you already know how to size one.",
    ],
    "not_covered": [
        "Isolation levels, query planning, and any particular product&rsquo;s internals. "
        "The structures here are shapes, and every figure is a ratio rather than a "
        "benchmark.",
        "The derivation of the Bloom filter&rsquo;s false-positive rate and its optimal "
        "`k`. Both are stated in &ldquo;Bloom Filters: Bits per Key&rdquo; and derived in "
        "&ldquo;Bloom Filters&rdquo; on the Algorithms path, which owns them along with "
        "the rule that a filter supports no deletion.",
        "Compression algorithms. The ratio is an input on this course; the break-even it "
        "feeds &mdash; whether the processor time a codec costs is worth the bytes it "
        "saves &mdash; is &ldquo;Compress or Not&rdquo; in Scaling Laws and Cost.",
    ],
    "footer_lead": (
        "I/O counts, tree heights, amplification factors, fsync rates and recovery "
        "windows on this course are exact &mdash; a height is the smallest integer `h` "
        "with `Bʰ ≥ N`, found by multiplication rather than by a logarithm that rounds, "
        "and the page prints what a logarithm would have said beside it. Two figures are "
        "rounded and say so on their faces: the Bloom filter&rsquo;s bits per key, which "
        "comes from the standard approximation to the false-positive rate and is `9.585` "
        "rather than the `9.57` a two-digit constant gives, and the page cache&rsquo;s "
        "Zipf hit rate past the size at which an exact harmonic number is still readable."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
