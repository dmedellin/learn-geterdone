# Accelerate, Read Along — the build specification

The curriculum, lab and authoring contract for the eighteenth Subject: a
read-along of Nicole Forsgren, Jez Humble and Gene Kim, *Accelerate: The
Science of Lean Software and DevOps: Building and Scaling High Performing
Technology Organizations* (Portland, OR: IT Revolution, 2018; ISBN
978-1942788331), its sixteen chapters, conclusion and three appendices in the
book's own order, one lesson per section or group of sections. The operator
asked for it "next in line", the same way as the previous read-alongs, all the
way to live.

It is built the way *Domain-Driven Design* (`docs/domain-driven-design/PLAN.md`)
and *Design Patterns* were, and adopts their conventions by reference wherever
this one is silent: Enterprise Patterns' §E (package, quoting, author's
checklist), §F (voice) and §R lessons. Read before this: `AGENTS.md` §0, §1,
§1a, §7, §8; `content/AGENTS.md`; `docs/domain-driven-design/AUTHORING.md`.

**This Subject is a book about measurement, so it is unlike the other
read-alongs.** Code Complete, Enterprise Patterns, Domain-Driven Design and
Design Patterns are books of judgements about code; Accelerate is a book of
findings from a survey, and half of it (Part II and Appendix C) is about how
the findings were reached. Its labs therefore compute what the book's
researchers computed — delivery measures from a log, classes of performer by
cluster analysis, a construct's score and reliability, a correlation and why
it does not show a cause, a Net Promoter Score — on small data written for the
lesson. System Design and Operations Research are its nearest neighbours for
queues and flow: a lesson that meets utilization and queueing (Chapter 2) or
work in process (Chapters 7, 8) names the System Design or Operations Research
lesson that teaches it once, by title, and does not repeat its prose.

Contents: §0 the one question · §A PATH · §B courses · §C every lesson ·
§D the new kit · §E package, text, quoting · §F voice · §G left out

---

## §0 The one question: what does the reader compute?

Accelerate's every claim is a number about a sample. The reader computes the
same kinds of numbers on a small sample written for the lesson:

1. **Delivery performance.** Deployment frequency, lead time for changes, time
   to restore service and change fail rate, from a log of commits, deploys and
   incidents, or from survey answers on the book's six-option scales
   (Chapter 2).
2. **Classes of performer.** Which teams a hierarchical (Ward's) cluster
   analysis groups together, and what the groups' typical answers are
   (Chapter 2, Chapter 12, Appendix C).
3. **Flow.** How lead time grows as utilization approaches 100 percent; work in
   process, throughput and lead time by Little's law; what a smaller batch does
   to the wait for feedback (Chapters 2, 4, 7, 8).
4. **Practice from a log.** Active branches and branch lifetimes against the
   trunk-based thresholds; which components can be released alone; deploys per
   developer per day as a team grows; lead time an approval step adds; the
   share of time on new work against unplanned work and rework (Chapters 4, 5,
   7).
5. **Constructs.** A construct's score from Likert-type items, reverse-coded
   where stated; a Westrum culture score; Cronbach's alpha, average variance
   extracted and composite reliability; whether the square root of the AVE
   exceeds the cross-construct correlations (Chapters 3, 11, 13, Appendix C).
6. **Relationships.** Pearson's r between two measures, what it becomes when a
   third variable drives both or when two trends are differenced, and which
   kind of analysis (descriptive, exploratory, inferential predictive, …) a
   stated claim needs (Chapter 12).
7. **Groups and samples.** "Twice as likely": the share of each group meeting
   an outcome and their ratio; an employee Net Promoter Score; a chi-square
   test of early against late respondents; who a snowball sample reaches from
   its seeds (Chapters 2, 10, 14, 15, Appendix C).
8. **Capabilities.** Which of the 24 capabilities a team has in place, by
   category, and what a maturity model's single level hides about the same
   team (Chapter 1, Appendix A).

**What the lab never does** is grade a team or an organization. Every figure
is computed from the small data the lesson states, and the book's own figures
are the survey's, of its sample, in its years. A figure on this path shows
what one measure says about one stated sample; it does not show what causes
what, which the book argues from theory and from many years of data. The
material clause (§A) says so, and every lesson closes on that gap.

## §A PATH fields (`content/accelerate/__init__.py`)

```
"slug": "accelerate",
"title": "Accelerate, Read Along",
"level": "Introductory",
"level_note": "you have worked on, with or near a team that builds and runs software",
"speech": "code",
```

(`"speech": "code"` as on the other software read-alongs; a lesson's backtick
runs are names, metrics and the occasional command, and the read-out reads
them that way. If a spoken form reads badly the author adds it to
`content/spoken/accelerate.py`.)

Catalog (`scripts/catalog.py`): `short_title` `"Accelerate"`, `"kind": "Read
along"`, last in the computing group (after Design Patterns), card:
"Forsgren, Humble and Kim&rsquo;s <em>Accelerate</em>, chapter by chapter,
with each finding recomputed on a small sample: delivery measures, clusters,
culture scores, reliability and correlation." Extend the computing group's
note with one clause: Accelerate assumes only that you have worked on or near
a software team. Course slug prefix `accelerate-`; check-id prefix `acc`;
package `accelerate` → slug `accelerate` needs no `PACKAGE_OF_SLUG` entry.

**material** (unique; required by `TestGeneratedPathIsCurrent`):
"every figure on this path is computed in your browser from the small sample
a lesson states &mdash; its log, its answers, its teams &mdash; and shows what
one measure says about that sample; it is not a finding about any team or
organization, and a correlation in it is not a cause."

tagline / description: written by course 1's author from the final counts
(`test_the_tagline_and_description_state_the_real_counts`). The tagline names
the book with `<em>`, says each finding is recomputed on a small sample, and
ends "Eight courses and N lessons are available."

## §B The eight courses

| # | slug | title | Part, chapters | lessons | module dir |
|---|---|---|---|---|---|
| 1 | `accelerate-measuring-performance` | Accelerate and Measuring Performance | Preface, I: 1–2 | 5 | `c1_measuring_performance` |
| 2 | `accelerate-culture` | Measuring and Changing Culture | I: 3 | 4 | `c2_culture` |
| 3 | `accelerate-technical-practices` | Technical Practices and Architecture | I: 4–5 | 7 | `c3_technical_practices` |
| 4 | `accelerate-lean-management` | Security, Lean Management and Product Development | I: 6–8 | 5 | `c4_lean_management` |
| 5 | `accelerate-people` | Sustainable Work, Satisfaction and Leadership | I: 9–11 | 7 | `c5_people` |
| 6 | `accelerate-the-science` | The Science Behind the Book | II: 12–13 | 7 | `c6_the_science` |
| 7 | `accelerate-surveys-and-data` | Surveys, Data and Statistical Methods | II: 14–15, App. C | 6 | `c7_surveys_and_data` |
| 8 | `accelerate-transformation` | Transformation | III: 16, Conclusion, App. A–B | 5 | `c8_transformation` |

46 lessons. Part I holds eleven chapters and is split by the book's own
topics: performance (1–2), culture (3), technical practice and architecture
(4–5), the three short chapters on security, management and product (6–8),
and the three on people (9–11). Part II is split between the general science
(12–13) and the survey method (14–15), which takes Appendix C because the
appendix is the method's reference. Part III is one chapter by guest authors
(Steve Bell and Karen Whitley Bell); it takes the Conclusion and Appendices A
and B, which close the book.

Modules (the `module` field) are the book's chapter titles, e.g.
`"Chapter 2 · Measuring Performance"`; the Preface is `"Preface"`; appendices
are `"Appendix C · Statistical Methods Used in Our Research"`.

## §C Every lesson

Format: slug — Title — chapter and sections (PDF pages of the operator's copy,
approximate: check with `book.py`) — lab `kit/mode` view — focus. Instances
are the lesson's own: **never the book's data as lab data** (no row of Tables
2.2/2.3 or B.1 typed in as the sample, no figure's bars, no ING teams, no
cheese and bedsheets series). The book's findings are stated in prose with
the chapter that reports them; each lab works a sample written for the lesson,
plainly labelled invented ("a team of eight", "twelve teams"). Where a lab
needs the book's answer options (the six lead-time options, the six
deployment-frequency options) or its thresholds (AVE > 0.50, alpha 0.70, items
loading above 0.60, correlations below 0.85, fewer than three active branches,
branches merged within a day), those are facts the lab may use as cfg, cited
in prose.

### Course 1 — Accelerate and Measuring Performance (Preface, Chapters 1–2)

1. `capabilities-not-maturity` — Capabilities, Not Maturity — Preface (23–34), Ch. 1 all (35–43): the research and its years; focus on capabilities, not maturity; evidence-based transformations; the value of adopting DevOps — `acckit/capability` `profile` — one team's 24 capabilities in place by category; the single level a stated maturity model would give it and the capabilities that level hides.
2. `the-flaws-in-previous-measures` — The Flaws in Previous Attempts to Measure Performance — Ch. 2 §flaws (45–47): lines of code, velocity, utilization — `acckit/flow` `utilization` — lead time as a multiple of service time as utilization rises (u/(1−u) queueing, stated as the simple model it is), so 100 percent utilization has no finite wait.
3. `the-four-measures` — Measuring Software Delivery Performance — Ch. 2 §measuring (47–51): global outcomes not output; lead time (design vs delivery), deployment frequency as batch-size proxy, time to restore, change fail rate; the six-option scales — `acckit/delivery` `metrics` — the four measures from a two-week log; each mapped to the book's answer option.
4. `high-medium-and-low-performers` — High, Medium and Low Performers — Ch. 2 (51–57): cluster analysis with no notion of good or bad; Tables 2.2 and 2.3 described in prose; no trade-off between tempo and stability; the 2016 surprise — `acckit/delivery` `cluster` — Ward's hierarchical clustering of ten invented teams' coded answers into k groups; the groups' medians on each measure.
5. `delivery-and-organizational-performance` — Delivery and Organizational Performance — Ch. 2 §impact and §driving change (58–62): profitability, productivity, market share; noncommercial goals; "twice as likely"; measures used to drive change, not to punish — `acckit/groups` `likely` — the share of high and low performers in an invented sample that exceed a goal, and the ratio "times as likely"; what the ratio is not (a cause, an odds ratio).

### Course 2 — Measuring and Changing Culture (Chapter 3)

1. `modeling-culture` — Modeling and Measuring Culture — Ch. 3 §modeling (63–66): three levels of culture (Schein), Westrum's typology, its six aspects (Table 3.1 in prose only) — `acckit/likert` `westrum` — seven respondents' answers to six items; each respondent's mean; the team's mean and its place among stated cut-points.
2. `likert-type-questions` — Measuring Culture — Ch. 3 §measuring culture (66–70): Likert-type items, strongly disagree to strongly agree, the construct as the mean of its items, why several items not one — `acckit/likert` `score` — item and construct means with one reverse-coded item; what the score would be without reversing.
3. `what-westrum-culture-predicts` — What Westrum Culture Predicts — Ch. 3 §predicts and §consequences (70–74): culture predicts delivery and organizational performance and job satisfaction; Google's team study; blameless postmortems; bad news as information — `acckit/stats` `pearson` — r between culture score and a delivery measure over invented teams.
4. `how-do-we-change-culture` — How Do We Change Culture? — Ch. 3 §change (74–75): Shook's argument, acting your way to a new culture through practices — `acckit/likert` `westrum` (two surveys, before and after) — the change in each respondent's score and the team mean; what the change does not tell us about why.

### Course 3 — Technical Practices and Architecture (Chapters 4–5)

1. `what-is-continuous-delivery` — What Is Continuous Delivery? — Ch. 4 §what (77–80): its five principles (quality built in, small batches, computers do repetitive work, relentless improvement, everyone responsible) and its foundations — `acckit/flow` `batch` — Little's law: work in process, throughput and lead time; how halving batch size shortens the wait for the first feedback.
2. `the-impact-of-continuous-delivery` — The Impact of Continuous Delivery — Ch. 4 §impact and §quality (80–88): drivers and impacts (Figures 4.1–4.3 in prose), less deployment pain and burnout, new work versus unplanned work and rework (Figure 4.4 in prose) — `acckit/work` `split` — a month's hours by kind; shares of new work, unplanned work and rework; time freed when rework halves.
3. `version-control-and-test-automation` — Version Control, Test Automation and Test Data — Ch. 4 §practices (88–91): what works (application and system configuration in version control, reliable tests developers own) and what doesn't (tests written by a separate QA team) — `acckit/groups` `likely` — shares of invented teams that meet a reliability goal with and without a practice; the ratio.
4. `trunk-based-development` — Trunk-Based Development — Ch. 4 §trunk-based, §infosec, §adopting (91–93): fewer than three active branches, branches and forks living less than a day, no code freezes — `acckit/branches` `trunk` — a month of branches: active branches per day, maximum, lifetimes, branches over a day, freeze days; which thresholds the log meets.
5. `deployability-and-testability` — Types of Systems and Deployability — Ch. 5 §types and §deployability (95–99): system type does not predict performance; what does: testing and deploying a service independently — `acckit/release` `independent` — components and "must release with" ties: release groups, the largest group, components deployable alone; before and after one tie is removed.
6. `loosely-coupled-architecture-enables-scaling` — A Loosely Coupled Architecture Enables Scaling — Ch. 5 §scaling (99–102): deploys per developer per day as teams grow (Figure 5.1 in prose), Conway's law, the inverse Conway manoeuvre — `acckit/release` `scaling` — deploys per developer per day for invented organizations of different sizes; whether it rises, holds or falls with size.
7. `tools-and-architects` — Allow Teams to Choose Their Own Tools — Ch. 5 §tools and §architects (102–104): tool choice and its limits; architects focus on engineers and outcomes — `acckit/release` `independent` — a second system: how many teams must coordinate a release when a shared tool or library forces lock-step upgrades.

### Course 4 — Security, Lean Management and Product Development (Chapters 6–8)

1. `shifting-left-on-security` — Integrating Infosec into the Delivery Lifecycle — Ch. 6 all (105–110): shifting left, preapproved libraries and tools, security reviews in the cycle; the Rugged movement — `acckit/work` `split` — hours spent remediating security findings, by the stage at which they were found; what finding them earlier would save at the stated costs.
2. `lean-management-practices` — Lean Management Practices — Ch. 7 §lean (111–114): limiting work in progress, visual management, feedback from production monitoring; WIP limits on their own are not enough — `acckit/flow` `wip` — Little's law with a WIP limit: throughput held, lead time with and without the limit.
3. `lightweight-change-management` — A Lightweight Change Management Process — Ch. 7 §change management (114–117): external approval (change advisory boards) is negatively correlated with performance and does not lower change fail rate; peer review — `acckit/change` `approval` — invented changes by approval route: lead time each route adds, change fail rate by route; what the sample does and does not show.
4. `lean-product-development` — Lean Product Development Practices — Ch. 8 §lean product (118–121): small batches, visibility of work, customer feedback, team experimentation — `acckit/flow` `batch` — a feature as one release against the same work in four slices: when the first customer feedback arrives.
5. `team-experimentation-and-product-management` — Team Experimentation and Effective Product Management — Ch. 8 §experimentation and §effective (121–124): teams free to change specifications without outside approval, the reciprocal model in which lean product management and delivery performance drive each other — `acckit/stats` `pearson` — r between a lean-product score and a delivery score; why a correlation cannot say which drives which.

### Course 5 — Sustainable Work, Satisfaction and Leadership (Chapters 9–11)

1. `deployment-pain` — Deployment Pain — Ch. 9 §pain (125–130): fear and anxiety at deploy time, what predicts it — `acckit/stats` `pearson` — r between a deployment-pain score and the share of manual deployment steps in invented teams.
2. `burnout` — Burnout — Ch. 9 §burnout to §reduce (130–137): Maslach's definition, the six organizational risk factors, what reduces it — `acckit/likert` `score` — burnout items for a team with a reverse-coded item; per-respondent scores; respondents above a stated line.
3. `employee-loyalty-and-nps` — Employee Loyalty and the Net Promoter Score — Ch. 10 §loyalty and §NPS (139–142): eNPS, promoters 9–10, passives 7–8, detractors 0–6; high performers' employees more likely to recommend — `acckit/groups` `enps` — an invented team's 0–10 answers: promoters, passives, detractors, eNPS; how one answer moving from 8 to 9 changes it.
4. `identity-and-job-satisfaction` — Identity and Job Satisfaction — Ch. 10 §identity, §satisfaction, §DevOps and satisfaction (142–147): identification with the organization, satisfaction and performance — `acckit/likert` `score` — identity items for two teams; the two constructs' means.
5. `diversity-in-tech` — Diversity in Tech — Ch. 10 §diversity to §what we can do (147–154): women and underrepresented minorities in the sample (stated in prose with the year), what other research says, inclusion — `acckit/groups` `likely` — shares in an invented sample and a ratio; why a share of respondents is not a share of the industry (sampling, Chapter 15).
6. `transformational-leadership` — Transformational Leadership — Ch. 11 §transformational (155–162): Rafferty and Griffin's five dimensions (vision, inspirational communication, intellectual stimulation, supportive leadership, personal recognition); leadership enables capabilities but does not deliver by itself — `acckit/likert` `score` (five constructs) — a leader rated by six reports on two items per dimension; each dimension's mean; the lowest.
7. `the-role-of-managers` — The Role of Managers — Ch. 11 §managers and §tips (162–169): investment in skills, a budget and time for learning, safe experimentation — `acckit/groups` `likely` — teams with and without a learning budget meeting an outcome; the ratio and its limits.

### Course 6 — The Science Behind the Book (Chapters 12–13)

1. `primary-secondary-qualitative-quantitative` — Primary and Secondary, Qualitative and Quantitative Research — Ch. 12 §primary to §types (170–173) — `acckit/stats` `describe` — the same invented answers described: count, mean, median, mode, range and standard deviation; what each describes and what none of them explains.
2. `descriptive-and-exploratory-analysis` — Descriptive and Exploratory Analysis — Ch. 12 §descriptive and §exploratory (173–177): correlation, spurious correlation (Figure 12.1's example named, never used as data) — `acckit/stats` `spurious` — two invented series that both rise with time: r of the levels, r of the year-on-year changes.
3. `inferential-predictive-analysis` — Inferential Predictive Analysis — Ch. 12 §inferential and §predictive, causal, mechanistic (177–180): a hypothesis from theory first, then the test; why the book does not claim causation from a survey — `acckit/stats` `spurious` (common-cause view: `confound`) — a third variable driving two measures; r of the two before and after holding the third fixed (within strata).
4. `classification-analysis` — Classification Analysis — Ch. 12 §classification and §research in this book (180–182) — `acckit/delivery` `cluster` — the same teams clustered into two, three and four groups; the fusion coefficients (Ward's increase in within-group squares) at each merge, which the book's method compares.
5. `latent-constructs` — Latent Constructs — Ch. 13 opening and §trusting data (183–190): manifest variables, latent constructs, operationalizing a construct, Westrum's culture as an example — `acckit/likert` `score` — a construct from four items; the score with one item dropped.
6. `several-views-and-rogue-data` — Several Views, and a Safeguard Against Rogue Data — Ch. 13 §several views and §rogue data (190–195): convergent and discriminant validity; one bad item or one bad respondent — `acckit/validity` `matrix` — an item correlation matrix with two constructs; mean within-construct and cross-construct correlations; the item that loads on the wrong construct.
7. `latent-constructs-and-system-data` — Latent Constructs and System Data — Ch. 13 §system data (195–196): measuring a system through several signals — `acckit/likert` `alpha` — Cronbach's alpha for a four-item scale; alpha with one item removed; the 0.70 cutoff.

### Course 7 — Surveys, Data and Statistical Methods (Chapters 14–15, Appendix C)

1. `surveys-collect-data-quickly` — Surveys Allow You to Collect and Analyze Data Quickly — Ch. 14 §quickly and §full stack (197–201): speed, breadth, a view across systems no log covers — `acckit/delivery` `metrics` — the same team measured from a log that misses a manual hotfix path: the measures with and without the missing deploys.
2. `you-can-trust-survey-data` — You Can Trust Survey Data — Ch. 14 §completely, §trust, §only surveys (201–208): system data has gaps; lying on a survey is hard to do consistently; some things (culture, satisfaction) only a survey measures — `acckit/likert` `score` — one respondent who answers every item 7; the construct's mean with and without them; their pattern across a reverse-coded item.
3. `the-data-for-the-project` — The Data for the Project — Ch. 15 all (209–218): snowball sampling, why it fits a population with no list, its limits and the countermeasures — `acckit/sample` `snowball` — seeds and referrals: who each wave reaches, the share of the sample that comes from each seed, what a missing seed community would leave out.
4. `tests-for-bias` — Tests for Bias — App. C §survey preparation to §tests for bias (266–268): chi-square and t-tests between early and late responders; common method bias (Harman's single-factor test and the marker variable test named) — `acckit/groups` `bias` — early and late respondents by a categorical answer: the chi-square statistic against a stated critical value.
5. `tests-of-the-measurement-model` — Tests of the Measurement Model — App. C §relationships and §measurement model (268–270): PCA with varimax, loadings above 0.60 and no cross-loading, AVE above 0.50, its square root above the cross-construct correlations, correlations below 0.85, Cronbach's alpha and composite reliability above 0.70 — `acckit/validity` `ave` — two constructs' loadings: AVE, composite reliability, √AVE against the correlation; every test passed or failed.
6. `tests-for-relationships-and-classification` — Tests for Relationships and Classification — App. C §correlation and prediction, §classification (270–273): Pearson's r, PLS and linear regression, cluster analysis by Ward's method and four others, ANOVA with Tukey's test — `acckit/stats` `pearson` (with the fitted line) — r and the least-squares line for invented scores; the share of variance r² accounts for.

### Course 8 — Transformation (Chapter 16, Conclusion, Appendices A–B)

1. `a-high-performing-management-framework` — A High-Performing Management Framework in Practice — Ch. 16 opening and §framework (219–227): ING's transformation, the obeya, squads, tribes and chapters (in prose only; never as lab data) — `acckit/flow` `wip` — a team's board: work in process, throughput and lead time; the effect of the stated WIP limit.
2. `stand-ups-catchball-and-kata` — Stand-ups, Catchball and Improvement Kata — Ch. 16 §framework continued (227–234): the stand-up and catchball rhythm (Figure 16.3 in prose), strategy deployment, the improvement kata — `acckit/delivery` `metrics` (two periods) — a team's current condition and target condition on the four measures; which targets the next period met.
3. `transforming-leadership-and-team-practices` — Transforming Your Leadership, Management and Team Practices — Ch. 16 §transforming (234–240) — `acckit/capability` `profile` (two dates) — the capabilities a team added in a quarter, by category.
4. `conclusion` — Conclusion — Conclusion (241–243): what the research found and what it asks of leaders — `acckit/groups` `likely` — the book's closing claim restated as one comparison on an invented sample; what the comparison cannot carry.
5. `capabilities-and-the-stats` — Capabilities to Drive Improvement, and the Stats — App. A (244–251) and App. B (252–265): the 24 capabilities by category; the statistics behind each chapter, as a reference — `acckit/capability` `profile` — a whole-organization view: the categories where most teams lack a capability.

## §D The new kit: `acckit`

Built on `eakit_core` exactly as `dddkit` and `itakit` are (copy `dddkit`'s
`mode_lab` pattern: import `eakit_core` as `ea`; one pure JS
`<prefix>Compute(view, inst, opts)` per mode returning `{tiles, status,
table}` or `{refuse}`; a Python `check` per view mirroring every JS refusal;
presets with `expect`; listed in `build_paths.KITS_WITH_EXPECTATIONS`;
mathcheck cases in `scripts/mathcheck.js`, each seen to fail when its function
is broken). Two modules: `acckit.py` (entry point + family A) and
`acckit_b.py` (family B), with a seam contract `docs/accelerate/kit-contract.md`
in the shape of `docs/domain-driven-design/kit-contract.md`. Report for
authors: `docs/accelerate/kit-report.md`, same shape as
`docs/domain-driven-design/kit-report.md`.

Id prefixes: three letters beginning `a`, as listed below (grepped free on
main at 3e4cfd2; family A's engineer re-greps, including the Design Patterns
branch's `gofkit`, and changes any that collide, announcing it at the top of
the contract). Shared helpers begin `akt` / `AKT_` (`acc` is taken).

Everything is exact counting and exact rational arithmetic (`RATIONAL_JS`).
Where a statistic needs a square root (Pearson's r, standard deviation,
√AVE), the kit computes the exact rational under the root and prints the root
to a stated number of decimals by an exact method (integer square root of the
scaled rational, rounded half up), so the printed digits are a function of
the inputs and nothing else; comparisons against a threshold are done on the
squares, exactly (√AVE > |r| as AVE > r²). Nothing typed is evaluated as
script; names are `ea.NAME`-shaped. Each view's rules sentence says what is
computed, the formula in words, and how ties and orders go. Every lab ends its
status line with the same caution in a few words: the figure is of the sample
stated.

The panel intro, unless a lesson overrides it: "A figure computed from the
small sample the lesson states. It shows what one measure says about that
sample; the book's findings are its survey's, and a correlation is not a
cause."

**Family A (`acckit.py`)**: delivery, flow and practice.

| mode (prefix) | views | input | tiles (at least) |
|---|---|---|---|
| `delivery` (ade) | `metrics` | a period (`days`, whole); `changes`: records `change, committed, deployed, failed` (times as `day.hh:mm` or decimal hours from the period start; `failed` yes/no); `incidents`: records `incident, start, restored`; optional `period2` second set (columns `period` 1/2) to compare | deployments; deployments per day and per week; median lead time (commit to deploy) and its answer option on the book's six-option scale; change fail rate (failed / deployed, exact %) and its band (0–15, 16–30, 31–45, 46–60, …%); median time to restore and its option; per period when two; the table: each change with its lead time |
|  | `cluster` | `teams`: records `team, deploy, lead, restore, fail` coded 1–6 on the book's scales (cfg says which end is better; the clustering ignores it), `k` 2–5 | Ward's agglomerative clustering on squared Euclidean distance, exact; each merge in order with its fusion coefficient (increase in within-group sum of squares); the k groups (members); each group's median on each measure, decoded to the option's words; ties broken by the earlier team in input order (stated) |
| `flow` (afl) | `utilization` | `levels`: a list of utilizations as percentages 0–99 (or a single one with `service` time) | for each level the queueing multiple u/(1−u) and the lead time (service × (1 + u/(1−u)) = service/(1−u)), exact; refuses 100 with the reason; the rules sentence names the model (a single server with random arrivals) as a simplification |
|  | `batch` | `work` items (count), `batch` size(s) (one or two to compare), `per_item` time, `release_cost` fixed time per batch | batches; time to first feedback (first batch done); time to last; average wait per item; releases; total release overhead |
|  | `wip` | `throughput` items per day (exact rational), `wip` (one or two values: without and with a limit), or a board log `items: record item, start, done` | lead time = WIP / throughput (Little's law) for each; from a log: average WIP, throughput, average lead time, and Little's law checked on the log |
| `branches` (atb) | `trunk` | `days` (whole); `branches`: records `branch, created, merged` (day numbers; merged `-` = open at the end); `freezes`: days list; thresholds from cfg defaulting to the book's (fewer than three active, i.e. at most 2; lifetime ≤ 1 day; 0 freeze days) | active branches each day (table); maximum; mean lifetime of merged branches (exact); branches living over the limit (listed); open at the end; freeze days; each threshold met yes/no |
| `release` (arl) | `independent` | `components`; `ties`: records `a, b` ("must release together"); optional `remove` (one tie) | release groups (connected components, listed); largest group; components deployable alone; teams that must coordinate (when a `team` column is given); the same after removing the tie |
|  | `scaling` | `orgs`: records `org, developers, deploys` over `days` | deploys per developer per day per org, exact; ordered by size; whether the rate rises, holds or falls from smallest to largest (stated as of these rows) |
| `change` (acm) | `approval` | `changes`: records `change, route, wait, failed` (route `none`/`peer`/`cab`/… a name; wait in hours) | changes by route; mean and median wait each route adds; change fail rate by route (exact %); overall; the difference in fail rate between two named routes |
| `work` (awk) | `split` | `entries`: records `kind, hours` (kinds named in cfg, e.g. `new`, `unplanned`, `rework`, `security`, `stage` optional) and optional `scale` (a kind and a factor, e.g. rework × 1/2) | total; hours and share per kind (exact %); new work's share; after the scaling, the new shares and the hours freed |

**Family B (`acckit_b.py`)**: constructs, statistics, groups and samples.

| mode (prefix) | views | input | tiles (at least) |
|---|---|---|---|
| `likert` (alk) | `score` | `points` (5 or 7, default 7); `items`: records `item, construct, reverse` (yes/no); `answers`: records `respondent, a1 … ak` (whole 1…points) | per respondent per construct: mean (reverse = points + 1 − answer); per item mean; per construct mean over respondents; respondents above/below a stated `line`; the same without reversing (to show the error) |
|  | `westrum` | as `score` with one construct, plus `cuts` (two values on the scale, defaults from cfg only — the book gives no cut-points, the lesson states its own and says so); optional second `answers2` (before/after) | each respondent's mean and band (pathological / bureaucratic / generative by the stated cuts); team mean and band; with two surveys: change per respondent and in the mean |
|  | `alpha` | `answers` for one construct's k items (k ≥ 2, n ≥ 3) | item variances, total-score variance (population or sample — state which; alpha is the same either way), α = k/(k−1)·(1 − Σσᵢ²/σₜ²), exact and to three decimals; alpha with each item removed; meets 0.70 yes/no |
| `stats` (ast) | `describe` | `values` (a list, or records `name, value`) | n, mean, median, mode(s), minimum, maximum, range, population and sample standard deviation (3 decimals by the exact method) |
|  | `pearson` | `pairs`: records `name, x, y` (n ≥ 3) | n; means; r (3 decimals, exact method), r² exact and %; the least-squares line y = a + b·x (exact rationals, shown to 3 decimals); sign and strength words by stated cut-offs (cfg) |
|  | `spurious` | `series`: records `t, x, y` (ordered) | r of the levels; r of the first differences; the two compared |
|  | `confound` | `rows`: records `name, x, y, z` with z a category | r over all rows; r within each z group (where n ≥ 3 and variance non-zero); the pooled within-group r (from within-group sums of squares and products) |
| `validity` (avd) | `matrix` | `items`: records `item, construct`; `corr`: the lower triangle of an item correlation matrix (records `a, b, r`, decimals) | mean within-construct correlation per construct; mean cross-construct correlation; for each item, its mean correlation with its own construct's items and with each other construct's; items whose cross mean exceeds their own (listed) |
|  | `ave` | `loadings`: records `item, construct, loading` (decimals 0–1); `between`: records `c1, c2, r` | per construct: AVE = mean of squared loadings; composite reliability CR = (Σλ)² / ((Σλ)² + Σ(1 − λ²)); items loading ≤ 0.60; √AVE (3 decimals); for each pair: √AVE of each > |r| (tested as AVE > r²), r < 0.85; every test with pass/fail; thresholds from cfg defaulting to the book's |
| `groups` (agr) | `likely` | `rows`: records `group, met` counts as `group, n, met` (two or more groups) | per group: n, met, share (exact %); the ratio of two named groups' shares ("times as likely", exact, 2 decimals); the difference in percentage points; the odds ratio shown separately, so the two are not confused |
|  | `enps` | `answers`: whole 0–10 (list, or records `name, answer`) | n; promoters (9–10), passives (7–8), detractors (0–6); eNPS = %promoters − %detractors (exact, whole when it is); the answers that would raise it by moving one band |
|  | `bias` | `table`: records `category, early, late` counts; `critical` (the critical value the lesson states for its degrees of freedom and level) | expected counts; χ² = Σ (O − E)²/E exact and to 3 decimals; degrees of freedom; χ² > critical yes/no; cells with expected < 5 flagged |
| `sample` (asn) | `snowball` | `people`: records `person, referred_by, group` (`-` for a seed); optional `drop` (a seed) | seeds; waves (wave 0 seeds, wave n referred by wave n−1) with counts; sample size; share from each seed's tree; share per `group`; with `drop`: who is lost and the shares after |
| `capability` (acp) | `profile` | `capabilities`: records `capability, category` (the book's 24 names and 5 categories are facts the preset may carry); `teams`: records `team, cap₁ … ` as yes/no, or `has` lists; optional `levels`: a stated maturity model (records `level, capabilities required`) and optional `team2`/`date2` | per team per category: in place / total; overall; with a maturity model, the level reached (highest level whose requirements and all lower levels' are met) and the capabilities in place above that level (what the level hides); with two dates, capabilities added; across teams: the capability fewest teams have |

**Never**: grade a team, an organization or a leader; carry the book's tables
or figures as data; run typed text as script; print a figure the inputs do
not determine; print a statistical significance the inputs cannot support (no
p-values; the chi-square view compares with a critical value the lesson
states).

## §E Package, text, quoting

Package `content/accelerate/`, one directory per course (§B), each with
`__init__.py` (COURSE dict, same fields as
`content/domain_driven_design/c2_building_blocks/__init__.py`) and `part_a.py`
(and `part_b.py` past five lessons). Spoken forms in
`content/spoken/accelerate.py`, one block per course.

**The text** is the operator's copy, extracted privately outside the
repository (see `docs/accelerate/AUTHORING.md`). It is a 315-page PDF whose
footer numbers equal its PDF pages; cite by chapter and section in prose,
never by page; source comments give the PDF page (`# PDF p. N of the
operator's copy`). The book is in copyright: never copy any stretch of it into
the repository, the project files or a report. Drop capitals split the first
word of each chapter in the extraction ("B usiness"); never quote a chapter's
first sentence.

**Quoting** (Enterprise Patterns §E.3): one opening quotation of at most 40
words, at most 60 words of quotation per lesson, character for character.
Never reproduce the book's tables, figures, survey items (the Likert items of
Figure 3.1 and their wording), lists of capabilities beyond the capability
names, or its example data. The 24 capability names, the four measures' names
and their answer options, the five dimensions of transformational leadership,
Westrum's three types and six aspect names, and the statistical thresholds are
facts and may be used.

**Overlap scan**: no run of 8+ consecutive words shared with the book except
titles, capability and section names, answer options, and counted quotations.

## §F Voice

The read-along for someone who works on or near a software team and is
reading the book. Each lesson: which sections, what question the chapter
asks, what the research found in the lesson's own words (with the year when
the book gives one), how the researchers measured it, the finding's limits
where the book states them (and where Fowler's foreword does: subjective
perceptions, the sample), then the lab on a sample written for the lesson, a
worked example by hand, and a quiz whose distractors are each arguable-for and
wrong. Credit the book to "the authors" or "Forsgren, Humble and Kim"; Chapter
16 is by Steve Bell and Karen Whitley Bell, and its lessons say so. The
statistics lessons are exact and plain: a formula in words and symbols, one
worked line by hand, no p-values the reader cannot compute. Be fair to the
book's argument and to its critics: the book itself names its limits
(perceptual measures, snowball sampling, inferential prediction rather than
proof of cause), and the lesson says them too.

## §G What is left out, and why

- The two forewords and the praise pages: pointed to; Fowler's caution
  (surveys of perception, the sample) is cited in Course 1 and Course 7.
- The Quick Reference: it is Appendix A's list, taught in Course 8.
- Acknowledgments, Bibliography, Index, About the Authors.
- The book's figures, tables, survey items and example data (copyright, §E).
