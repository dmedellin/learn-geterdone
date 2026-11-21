---
format: long
lesson: replication-and-consistency/reads-scale-writes-do-not
title: Replication: reads scale, writes don't
thumb: Three replicas, 2.5× the work
---

@chapter The question
@title text="Reads Scale, Writes Do Not" sub="Replication and Consistency" art=thumb
Three replicas means three times the throughput, right? For reads, yes. For writes, not at all. And for a real workload, somewhere in between, set by a number that has nothing to do with the fleet.

@art read-one-copy
A read is answered by one copy. So copies divide the read stream between them. Three replicas serve three times the reads of one.

@art write-every-copy
But a write has to reach every copy. A copy that skipped a write wouldn't be a copy. So copies multiply the write stream instead. That asymmetry isn't something a better design removes. It's what a replica is.

@chapter Four multipliers
@list heading="N replicas against one machine" items="read capacity N×@read capacity|write capacity 1×@write capacity|write work N×@write work|storage N×@storage"
So a replication factor of N buys four multipliers. Read capacity, times N. Write capacity, times one, however many you buy. Write work, times N, because every replica applies every write. And storage, times N. The first is the benefit. The other three are the bill.

@art storage-stack
And the bill is real. Each replica applies the full write stream, so the cluster does N times the disk writes, N times the index maintenance, N times the compaction. That's invisible in a throughput number and very visible on an invoice.

@chapter The mix decides
@math heading="ρ reads per write" items="w = 1/(1 + ρ) writes · r = ρ/(1 + ρ) reads@the share;;speed-up(N) = 1 / (w + r/N)@speed up"
A real workload is a mix. With rho reads per write, the share of writes is one over one plus rho, and the rest are reads. Only the read share divides by N. So the speed up is one over w plus r over N.

@math heading="ρ = 9, so w = 1/10" items="N = 1:  1 / (1/10 + 9/10) = 1×@one replica;;N = 3:  1 / (1/10 + 3/10) = 1/(2/5) = 2.5×@three replicas;;N = 12:  1 / (1/10 + 3/40) = 40/7 ≈ 5.714×@twelve;;N → ∞:  1/(1/10) = 10× = 1 + ρ@infinity"
At nine reads per write, a tenth of operations are writes. One replica is one times. Three replicas give one over a tenth plus three tenths, two fifths, so two and a half times. Twelve replicas give forty sevenths, about five point seven one. And as N goes to infinity, the reads cost nothing, leaving ten times, one plus rho.

@art serial-share
That's the serial part no amount of parallelism divides. Here the serial part is the write, and it's serial in a precise sense: every machine does all of it.

@chapter Three replicas, worked
@math heading="1000 ops/s per replica, N = 3, ρ = 9" items="cluster = 2.5 × 1000 = 2500 ops/s@two thousand five hundred;;2250 reads/s + 250 writes/s@two thousand two hundred;;3× storage · 3× write work@three times"
One machine serves a thousand operations a second. With three replicas, the cluster serves two thousand five hundred: two thousand two hundred and fifty reads and two hundred and fifty writes. For three times the storage and three times the write work. Defensible, but not three times.

@art diminishing
And four times the fleet, three replicas to twelve, takes the speed up from two point five to about five point seven. A little over double, against a ceiling that's still ten. The ceiling belongs to the workload. To raise it, change rho. Cache the reads elsewhere, or batch the writes.

@chapter The write-heavy service
@words text="ρ = 0  →  1× at every N"
At zero reads per write, every operation is a write. The speed up is one at every N, and so is the ceiling. Three replicas serve exactly what one served, for three times the storage and write work.

@art ingest-log
That's not a corner case. An append only ingest path, a metrics writer or an audit log sits close to it. Replicating them buys durability and availability, which are good reasons. Just not throughput.

@chapter Where people slip
@list heading="Common slips" items="Quoting N× for the cluster@The first|Forgetting write work is billed N times@The second|Reading the ceiling as reachable@The third"
The first slip is quoting N times for the cluster when it's N times for reads only. The second is forgetting that write work is billed N times: disk writes, index maintenance, compaction. The third is reading the ceiling as something a bigger fleet reaches. It's a limit, never arrived at.

@chapter Try it
@words text="ρ = 2 reads per write" sub="w = 1/3 · ceiling 3×"
Your turn. Same service, two reads per write. A third of operations are writes, so the ceiling is three times. Compute the speed up at three replicas and at twelve, the share of the ceiling each reaches, and the storage bill beside each.

@end text="Change ρ, watch the ceiling move"
You can set the replication factor and the read write ratio and see all four multipliers, on Learn. That's learn dot get er done dot I O.
