"""Analysis Patterns, Design Patterns and Refactoring, lessons 1-4 -- Chapters 11-13.

Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004): Chapter 11, Applying Analysis Patterns (its two
examples, Earning Interest with Accounts and Insight into the Nightly Batch,
and Analysis Patterns Are Knowledge to Draw On); Chapter 12, Relating Design
Patterns to the Model (Strategy, Composite, Why Not Flyweight?); Chapter 13,
Refactoring Toward Deeper Insight. Chapter 11's accounting patterns are Martin
Fowler's, from Analysis Patterns (1997); Chapter 12's patterns are those of
Gamma, Helm, Johnson and Vlissides. Pages in the comments are PDF pages of the
operator's copy; the lessons cite by chapter, section and pattern. Every
quotation is copied from that copy and checked with quotes.py. The models,
records and code are written for these lessons: none of the book's examples,
diagrams, dialogues or data is reproduced, and no lab uses the book's
domains. The design is docs/domain-driven-design/PLAN.md, section C, Course 6.
"""


def _lines(text):
    """A snippet or record constant as a code block's list of lines."""
    return text.split("\n")


def _records(text):
    """Records written one to a line, as the single string a lab field takes."""
    return " ".join(line.strip() for line in text.split("\n") if line.strip())


# ---------------------------------------------------------------- 6.1 records

# A theatre box office's week, double entry: a positive amount is a debit, a
# negative one a credit. t1 a sale for cash, t2 a gift voucher sold, t3 a
# voucher redeemed for tickets, t4 a refund.
WEEK_BALANCED = """t1, cash, 120.00;
t1, ticket-sales, -120.00;
t2, cash, 50.00;
t2, vouchers, -50.00;
t3, vouchers, 30.00;
t3, ticket-sales, -30.00;
t4, ticket-sales, 24.00;
t4, cash, -24.00"""

# The same week with two slips: t3's credit typed as 3.00, and t4's refund
# recorded on the cash side only.
WEEK_TWO_SLIPS = """t1, cash, 120.00;
t1, ticket-sales, -120.00;
t2, cash, 50.00;
t2, vouchers, -50.00;
t3, vouchers, 30.00;
t3, ticket-sales, -3.00;
t4, cash, -24.00"""

# Exercise: the theatre bar's evening.
BAR_EVENING = """b1, cash, 18.50;
b1, bar-sales, -18.50;
b2, bar-stock, 40.00;
b2, cash, -40.00;
b3, cash, 6.00;
b3, bar-sales, -6.50;
b4, bar-sales, 4.00;
b4, cash, -4.00"""

ACCOUNT_JAVA = """// An account keeps every entry; its balance is their sum.
final class Account {
    private final String name;
    private final List<Entry> entries = new ArrayList<>();

    Account(String name) { this.name = name; }

    void post(Entry e) {
        entries.add(e);   // an entry is never removed or edited
    }

    long balanceCents() {
        long sum = 0;
        for (Entry e : entries) {
            sum += e.cents();
        }
        return sum;
    }
}"""

TRANSACTION_JAVA = """// A transaction's entries must net to zero before any is posted.
final class Transaction {
    private final List<Entry> entries;

    Transaction(List<Entry> entries) {
        long net = 0;
        for (Entry e : entries) {
            net += e.cents();
        }
        if (net != 0) {
            throw new IllegalArgumentException("unbalanced by " + net);
        }
        this.entries = Collections.unmodifiableList(new ArrayList<>(entries));
    }
}"""


# ---------------------------------------------------------------- 6.2 records

# Takings recorded as positive amounts in single accounts. The theatre's trust
# sets aside five per cent of ticket income for restoration; an agency keeps
# twelve per cent of what it sells.
TAKINGS = """e1, ticket-income, 412.50;
e2, ticket-income, 96.30;
e3, agency-sales, 180.00;
e4, bar-income, 55.00"""

TAKINGS_WITH_DONATION = TAKINGS + """;
e5, restoration-fund, 200.00"""

RULES = """restore, ticket-income, restoration-fund, 0.05;
agency, agency-sales, agency-commission, 0.12"""

RULES_WITH_FEE = RULES + """;
trust-fee, restoration-fund, trust-admin, 0.10"""

MATINEE = """x1, ticket-income, 37.70;
x2, ticket-income, 18.10;
x3, bar-income, 12.00"""

MATINEE_RULES = """restore, ticket-income, restoration-fund, 0.05"""

POSTING_RULE_JAVA = """final class PostingRule {
    private final Account input;
    private final Account output;
    private final BigDecimal share;   // 0.05 for five per cent
    private Instant lastFired = Instant.MIN;
    PostingRule(Account input, Account output, BigDecimal share) {
        this.input = input; this.output = output; this.share = share;
    }

    // Posting-rule-based firing: the batch says when; the rule finds its input.
    void fire(Instant now) {
        for (Entry e : input.entriesSince(lastFired)) {
            BigDecimal moved = e.amount().multiply(share)
                    .setScale(2, RoundingMode.HALF_UP);
            output.post(new Entry(moved));
            input.post(new Entry(moved.negate()));
        }
        lastFired = now;
    }
}"""


# ---------------------------------------------------------------- 6.3 snippets

PLAN_TESTS = """// The rider's plan is tested in each computation that depends on it.
long fareCents(Ride r) {
    if (r.plan() == Plan.MEMBER && r.minutes() <= 45) {
        return 0;
    }
    if (r.plan() == Plan.MEMBER) {
        return 15 * (r.minutes() - 45);
    }
    if (r.plan() == Plan.STUDENT) {
        return 10 * r.minutes();
    }
    return 100 + 25 * r.minutes();
}

long depositCents(Ride r) {
    if (r.plan() == Plan.MEMBER || r.plan() == Plan.STUDENT) {
        return 0;
    }
    return 2000;
}"""

PRICING_POLICIES = """// Each plan is a pricing policy, given to the ride when it starts.
interface PricingPolicy {
    long fareCents(int minutes);
    long depositCents();
}
class CasualPolicy implements PricingPolicy {
    public long fareCents(int minutes) { return 100 + 25 * minutes; }
    public long depositCents() { return 2000; }
}
class StudentPolicy implements PricingPolicy {
    public long fareCents(int minutes) { return 10 * minutes; }
    public long depositCents() { return 0; }
}
class MemberPolicy implements PricingPolicy {
    public long fareCents(int minutes) {
        if (minutes <= 45) { return 0; }
        return 15 * (minutes - 45);
    }
    public long depositCents() { return 0; }
}"""

PROGRAMME_COMPOSITE = """// Every part of a festival programme answers the same question.
interface ProgrammePart {
    int minutes();
}
final class Act implements ProgrammePart {
    private final int minutes;
    Act(int minutes) { this.minutes = minutes; }
    public int minutes() { return minutes; }
}
final class Programme implements ProgrammePart {
    private final List<ProgrammePart> parts = new ArrayList<>();
    void add(ProgrammePart part) { parts.add(part); }
    public int minutes() {
        int sum = 0;
        for (ProgrammePart part : parts) { sum += part.minutes(); }
        return sum;
    }
}"""

SEAT_SCHEMES = """// A theatre prices a seat by the booking's scheme.
long seatCents(Seat s, Booking b) {
    if (b.scheme() == Scheme.STANDARD) {
        return s.baseCents();
    }
    if (b.scheme() == Scheme.CONCESSION && s.row() > 10) {
        return s.baseCents() / 2;
    }
    if (b.scheme() == Scheme.CONCESSION) {
        return s.baseCents() * 3 / 4;
    }
    return s.baseCents() - 300;
}

boolean refundable(Booking b) {
    return b.scheme() == Scheme.STANDARD || b.scheme() == Scheme.GROUP;
}"""


# ---------------------------------------------------------------- 6.4 records

# A clinic's appointment system before the cancellation rule was made an
# explicit concept: the 24-hour window is written into the screen, the
# reminder job and the invoice run; urgency is a flag on the patient record.
CLINIC_ELEMENTS = """AppointmentScreen, ui;
Calendar, scheduling;
ReminderJob, scheduling;
InvoiceRun, billing;
FeeTable, billing;
PatientRecord, patients"""

CLINIC_CHANGES_IMPLICIT = """window-48h, AppointmentScreen;
window-48h, ReminderJob;
window-48h, InvoiceRun;
urgent-exempt, AppointmentScreen;
urgent-exempt, InvoiceRun;
urgent-exempt, PatientRecord;
fee-amount, FeeTable;
reminder-text, ReminderJob"""

CLINIC_ELEMENTS_EXPLICIT = CLINIC_ELEMENTS + """;
CancellationPolicy, appointments"""

CLINIC_CHANGES_EXPLICIT = """window-48h, CancellationPolicy;
urgent-exempt, CancellationPolicy;
urgent-exempt, AppointmentScreen;
fee-amount, FeeTable;
reminder-text, ReminderJob"""

CANCELLATION_POLICY_JAVA = """// The rule the screen, the reminders and the invoices each used to repeat.
final class CancellationPolicy {
    private final Duration window;   // 24 hours today

    CancellationPolicy(Duration window) {
        this.window = window;
    }

    Instant lastFreeCancellation(Appointment a) {
        return a.start().minus(window);
    }

    boolean isLate(Appointment a, Instant cancelledAt) {
        if (a.isUrgent()) {
            return false;   // urgent visits are exempt
        }
        return cancelledAt.isAfter(lastFreeCancellation(a));
    }
}"""

# Exercise: a school timetable before and after a Period concept is made
# explicit.
TIMETABLE_EXERCISE = """// before: elements, as element, module
Timetable, scheduling; RoomBooking, rooms;
ExamPlanner, exams; ReportCard, reports
// before: changes, as change, element
longer-periods, Timetable; longer-periods, RoomBooking;
longer-periods, ExamPlanner; short-fridays, Timetable;
short-fridays, ExamPlanner; attendance, ReportCard
// after: elements, the same four and one more
Timetable, scheduling; RoomBooking, rooms;
ExamPlanner, exams; ReportCard, reports; Period, periods
// after: changes
longer-periods, Period; short-fridays, Period;
attendance, ReportCard"""


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 11, opening (PDF p. 181 of the operator's copy) and Example:
    # Earning Interest with Accounts (pp. 182-186), with Fowler's accounting
    # models as Evans summarises them (p. 183).
    # Quote: PDF p. 181 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "analysis-patterns",
        "title": "Applying Analysis Patterns",
        "module": "Chapter 11 · Applying Analysis Patterns",
        "one_line": "A model someone has already worked out for a common kind of business problem, taken as a starting point and then refactored to fit.",
        "summary": (
            "Chapter 11 opens with what an analysis pattern is and how a team draws on "
            "one, and works its first example through Martin Fowler's accounts and "
            "entries. Read Evans on why such a pattern is a lead and not a recipe, then "
            "post a week's entries to accounts, read off the balances, and find the "
            "transactions that do not balance."
        ),
        "key": [
            "a model for a common business problem",
            "a starting point, then refactor",
            "an account keeps every entry",
            "a balance is the sum of entries",
            "the entries of a transaction net to zero",
            "take what fits, leave what does not",
        ],
        "key_label": "Analysis patterns in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's, the other two "
            "are Fowler's accounting models as Evans summarises them."
        ),
        "concepts": [
            ("Analysis pattern",
             "A small group of concepts, worked out in practice, that represents a "
             "construction business models keep needing: accounts, quantities, "
             "parties, plans. It may belong to one domain or recur across many. The "
             "term and the best-known catalogue are Martin Fowler's, from his 1997 "
             "book Analysis Patterns."),
            ("Account and Entry",
             "An account holds something of value, usually money, and records every "
             "change to it as an entry. Value is added with a positive entry and taken "
             "away with a negative one; no entry is deleted, so the history stays. The "
             "balance is what all the entries add up to."),
            ("Transaction",
             "A group of entries that moves value from some accounts to others, so "
             "that its entries add up to zero: the conservation rule of double-entry "
             "book-keeping. It holds only in a closed system, one that includes every "
             "source and every sink of value."),
        ],
        "read_title": "The chapter's argument first, then the pattern, then the count",
        "read_intro": (
            "Read the opening of Chapter 11 and its first example, Earning Interest "
            "with Accounts, in your own copy first. The lesson reads the opening as an "
            "argument and Fowler's accounting models as a tool, and then counts a "
            "week's entries."
        ),
        "body": [
            ("p", "&ldquo;Analysis patterns are not technological solutions; they are guides "
                  "to help you work out a model in a particular domain.&rdquo; Evans writes "
                  "that near the start of Chapter 11, Applying Analysis Patterns, the first "
                  "of three short chapters that close Part III. This lesson reads the "
                  "chapter's opening and its first example, Earning Interest with Accounts. "
                  "Read both in your own copy first."),
            ("p", "The opening is an argument about where a deep model comes from. Usually, "
                  "Evans says, it is earned slowly, by learning, talking and trying. Now and "
                  "then a developer meets a problem whose shape is familiar, a kind of "
                  "responsibility or a web of relationships solved once before, and can "
                  "start from what was learned then. Some of those solutions have been "
                  "written down. They sit higher than Part II's building blocks and Chapter "
                  "10's principles of supple design: each uses a few objects to stand for "
                  "one concept. They save trial and error, and they give you a model that "
                  "already communicates and can be built; but they are where refactoring "
                  "starts, not a finished part to install. Evans takes the definition from "
                  "Fowler's 1997 book Analysis Patterns, which calls them groups of concepts "
                  "for a construction common in business modelling, belonging to one domain "
                  "or to many."),
            ("p", "He then corrects the name. &ldquo;Analysis&rdquo; suggests modelling done "
                  "apart from building, yet Fowler's patterns discuss implementation at "
                  "length, code included, and even look ahead to maintenance: Evans cites "
                  "Fowler's remark that a new accounting practice can be set up as new "
                  "instances of a rule, while the system keeps running, with no rebuild. "
                  "That experience is the most valuable thing a pattern carries. Taking "
                  "its model ideas without it, Evans warns, reopens the split between "
                  "analysis and design that Model-Driven Design, in Putting the Domain Model "
                  "to Work's Model-Driven Design and Hands-On Modelers, exists to close."),
            ("p", "The example returns to the interest-tracking application of Chapter 10. "
                  "It calculates what a borrower owes and pays, and a nightly batch hands "
                  "the figures to an older accounting system, naming the ledger for each. "
                  "It does the job, though it is clumsy to use and hard to change. One developer reads "
                  "the accounting chapter of Fowler's book, and Evans summarises the part "
                  "she finds useful: the models this lesson's lab counts."),
            ("p", "Read as a tool, Fowler's basic model is two objects. An Account holds "
                  "value; every change to that value is an Entry, positive to add and "
                  "negative to take away, and entries are kept rather than edited, so the "
                  "account's whole history stays. Its balance is what all its entries "
                  "come to, and whether it is added up on demand or cached is hidden "
                  "behind the account's interface. The second model adds conservation: "
                  "money only moves, from one account to another, so a Transaction groups "
                  "entries whose amounts add up to zero, every credit matched by a debit. "
                  "Evans, following Fowler, adds the condition and the qualification: the "
                  "rule holds only in a closed system, and many simple applications do "
                  "not need the rigour."),
            ("code", _lines(ACCOUNT_JAVA)),
            ("p", "What the team does with the pattern is the chapter's real lesson. The two "
                  "developers sketch a model with accounts, entries and a transaction tying "
                  "each interest charge to its payment, and take it to the domain expert. "
                  "Transaction does not fit: Fowler's version moves money between accounts "
                  "all at once, and their charges and payments are days apart and loosely "
                  "related; the expert says they are separate postings and the balance is "
                  "what matters. So they drop Transaction, keep accounts and entries, and "
                  "learn a word from the expert, accrual, which names the charge better "
                  "than anything in the code did. Coding refines it again: entries split "
                  "into payments and accruals, and a fee entry and an interest entry, alike "
                  "in the model, become separate classes after all, because the project's "
                  "tables and mapping framework required it. Evans calls that a calculated "
                  "compromise, to be made and moved past."),
            ("code", _lines(TRANSACTION_JAVA)),
            ("p", "Now the lab, on a theatre box office's week rather than the book's loans. "
                  "Amounts follow the usual double-entry signs, a debit positive and a "
                  "credit negative, so the box office's sales and the vouchers it owes "
                  "carry negative balances. On the preset <code>week-balanced</code> there "
                  "are 3 accounts and 4 transactions: a sale for cash, a gift voucher sold, "
                  "a voucher redeemed for tickets, and a refund. The balances, in the order "
                  "the accounts first appear, are cash 146.00, ticket-sales −126.00 and "
                  "vouchers −20.00. Every transaction nets to zero, so there are no "
                  "unbalanced transactions and the total of all entries is 0.00."),
            ("p", "The preset <code>week-two-slips</code> keeps the same week with two "
                  "mistakes in it. The credit side of t3 is typed as 3.00 instead of 30.00, "
                  "and t4's refund is recorded on the cash side only. The lab lists t3 "
                  "unbalanced by +27.00 and t4 by −24.00, while the total of all entries "
                  "is only 3.00, because the two errors partly cancel. That is what the "
                  "Transaction model buys: a check on each movement, where a grand total "
                  "hides errors that offset. It is a reason to look at t3 and t4, and "
                  "nothing more. Whether a system needs that check is the question the "
                  "chapter's own team answered no to."),
            ("h3", "Exercise"),
            ("code", _lines(BAR_EVENING)),
            ("p", "The theatre bar's evening, in the lab's record form: transaction, account, "
                  "amount. By hand, give each account's balance and the total of all "
                  "entries, and name every transaction whose entries do not add up to "
                  "zero, with its net. Then type the records into the lab to check, and "
                  "say in a sentence what the slip probably was."),
            ("p", "An account's entries were all made by hand here. The next lesson, Posting "
                  "Rules and the Nightly Batch, reads the chapter's second example, where "
                  "rules derive entries from other entries, and Evans's account of what an "
                  "analysis pattern is for."),
        ],
        "lab": ("dddkit", {
            "mode": "ledger",
            "view": "balance",
            "preset": "week-balanced",
            "presets": [
                {"id": "week-balanced",
                 "label": "A box office's week: sale, voucher sold, voucher redeemed, refund",
                 "entries": _records(WEEK_BALANCED),
                 "expect": {"dleAccounts": "3",
                            "dleBalances": "cash 146.00, ticket-sales −126.00, vouchers −20.00",
                            "dleTxns": "4", "dleUnbalanced": "0: none", "dleTotal": "0.00"}},
                {"id": "week-two-slips",
                 "label": "The same week with one credit mistyped and one refund one-sided",
                 "entries": _records(WEEK_TWO_SLIPS),
                 "expect": {"dleBalances": "cash 146.00, ticket-sales −123.00, vouchers −20.00",
                            "dleUnbalanced": "2: t3 +27.00, t4 −24.00", "dleTotal": "3.00"}},
            ],
            "panel_title": "Entries, balances and the transactions that do not balance",
        }),
        "steps_title": "Reading a ledger the way the pattern does",
        "steps_intro": "Four steps, the last of them on records of your own.",
        "steps": [
            ("Add each account's entries",
             "List the accounts in the order they first appear and add every entry to "
             "each. That sum is the balance: no entry is skipped or edited."),
            ("Add each transaction's entries",
             "Group the entries by transaction and add each group. Any group that does "
             "not come to zero is unbalanced; write down its net, with its sign."),
            ("Compare with the grand total",
             "Add every entry. A total of zero does not prove every transaction "
             "balances, since errors can offset; the per-transaction check is the one "
             "that finds them."),
            ("Do it on records of your own",
             "Take a statement, an expense sheet or a till report you know and write a "
             "few of its movements as transaction, account, amount. Count the accounts, "
             "say which movements need a matching entry, and decide whether your domain "
             "is a closed system in which the conservation rule should hold."),
        ],
        "worked": {
            "title": "Two slips in one week",
            "intro": [
                "Find the unbalanced transactions in <code>week-two-slips</code>.",
            ],
            "lines": [
                "t1: 120.00 − 120.00 = 0",
                "t2: 50.00 − 50.00 = 0",
                "t3: 30.00 − 3.00 = +27.00",
                "t4: −24.00, with nothing to match it",
                "total: +27.00 − 24.00 = +3.00",
                "two slips; the total shows 3.00",
            ],
            "after": [
                "Each transaction is checked on its own, which is how the slips are found. "
                "The total of all entries is the same check over the whole ledger at once, "
                "and two errors of opposite sign leave it looking nearly right.",
            ],
        },
        "quiz_title": "Accounts, transactions and Evans's claims",
        "quiz": [
            {"q": "In the exercise, what are the three balances, and which transaction does "
                  "not balance?",
             "a": ["cash −19.50, bar-sales −21.00, bar-stock 40.00; b3, by −0.50",
                   "cash −19.50, bar-sales −20.50, bar-stock 40.00; none",
                   "cash 19.50, bar-sales −21.00, bar-stock −40.00; b2, by −0.50",
                   "cash −20.00, bar-sales −21.00, bar-stock 40.00; b3, by +0.50"],
             "c": 0,
             "why": "Cash is 18.50 − 40.00 + 6.00 − 4.00 = −19.50; bar-sales is −18.50 − "
                    "6.50 + 4.00 = −21.00; bar-stock is 40.00. The total of all entries is "
                    "−0.50, and the only transaction that does not net to zero is b3: 6.00 "
                    "came into the till but 6.50 was credited to sales, a net of −0.50, "
                    "most likely a sale rung up at the wrong price. b2 is a purchase of "
                    "stock for cash and balances."},
            {"q": "On the preset <code>week-two-slips</code>, the total of all entries is "
                  "+3.00. What does the lab list as unbalanced?",
             "a": ["only t4, by −24.00",
                   "only t3, by +3.00",
                   "t3 by +27.00 and t4 by −24.00",
                   "nothing: a total of 3.00 is a rounding difference"],
             "c": 2,
             "why": "t3 debits vouchers 30.00 and credits sales only 3.00, a net of +27.00; "
                    "t4 has a single entry of −24.00. Together they come to +3.00, which is "
                    "why the grand total understates the trouble. The amounts are exact "
                    "cents, so nothing here is rounding."},
            {"q": "In Earning Interest with Accounts, why do the developers drop Fowler's "
                  "Transaction from their model?",
             "a": ["Their mapping framework could not store a transaction",
                   "Charges and payments are separate postings, days apart, not one "
                   "movement made at once",
                   "Fowler's chapter recommends against transactions for small systems",
                   "The domain expert had never heard the word"],
             "c": 1,
             "why": "Fowler's Transaction moves value between accounts in one go. The "
                    "team's interest charges and payments happen at different times and are "
                    "not paired one to one, and the expert tells them the balance is what "
                    "matters. The mapping framework is the reason for a different "
                    "compromise, the concrete fee and interest subclasses."},
            {"q": "According to the opening of Chapter 11, what does the name "
                  "&ldquo;analysis pattern&rdquo; fail to convey?",
             "a": ["That the patterns belong to a single domain",
                   "That the patterns are technological solutions",
                   "That the patterns come from field experience",
                   "That the patterns discuss implementation at length, code included"],
             "c": 3,
             "why": "Evans says the name stresses the patterns' conceptual nature and hides "
                    "how much implementation they discuss, which is why he warns against "
                    "taking their model ideas out of that context. Fowler's definition "
                    "allows a pattern to belong to one domain or span many; Evans says they "
                    "are not technological solutions; and their origin in practice is "
                    "something he states plainly."},
        ],
        "mistakes": [
            ("Installing an analysis pattern whole, as a finished component",
             "Evans says plainly that these are not out-of-the-box solutions: they give a "
             "starting model, and refactoring and experiment go on from there. His own "
             "example's team kept Fowler's accounts and entries and dropped his "
             "Transaction, because it did not match how their charges and payments "
             "behaved. On the lesson's illustration the lab can count what a Transaction "
             "would check; it cannot say whether your domain has one."),
            ("Assuming every money-like system needs double entry",
             "Fowler's conservation rule, as Evans summarises it, applies to a closed "
             "system that includes every source and sink of value, and many simple "
             "applications do not need that rigour. The interest application's team "
             "found their balances and entries were what the experts needed."),
            ("Reading the word analysis as analysis without design",
             "The name suggests models drawn before and apart from the code. Evans points "
             "out that Fowler's patterns discuss implementation and even long-term "
             "maintenance, and that model ideas lifted out of that discussion are harder "
             "to apply and reopen the divide between analysis and design that "
             "Model-Driven Design is meant to close."),
        ],
        "standard": (
            "Finish when you can post entries to accounts and find what does not balance.",
            "Given a list of entries, state every account's balance and the total, name "
            "each unbalanced transaction with its net, and say what Fowler's Transaction "
            "assumes about the domain."
        ),
        "note": (
            "The lab adds exact amounts. It cannot tell whether your domain is a closed "
            "system, whether its movements belong together as transactions, or which of "
            "Fowler's models fit it; Evans's example shows a team deciding that with its "
            "domain expert, and keeping only part of the pattern."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 11, Example: Insight into the Nightly Batch (PDF pp. 186-190 of the
    # operator's copy), with Fowler's Posting Rules and firing modes as Evans
    # summarises them (pp. 186-187); Analysis Patterns Are Knowledge to Draw On
    # (p. 190).
    # Quote: PDF p. 190 of the operator's copy, 27 words, quotes.py OK.
    # Lesson total: 27 words.
    {
        "slug": "posting-rules",
        "title": "Posting Rules and the Nightly Batch",
        "module": "Chapter 11 · Applying Analysis Patterns",
        "one_line": "Rules that derive new entries from entries already posted, turning a batch job's hidden logic into a model the team can name and discuss.",
        "summary": (
            "Chapter 11's second example finds a domain model inside a nightly batch "
            "job, through Fowler's Posting Rules and their three firing modes, and its "
            "last section says what an analysis pattern is for. Read the argument, then "
            "let rules derive entries from a theatre's takings and count the entries, "
            "the balances and the cents rounding leaves behind."
        ),
        "key": [
            "a rule derives entries from entries",
            "input account, output account, amount",
            "when rules fire is part of the language",
            "a batch can have a model inside it",
            "keep the concept a borrowed term names",
            "a pattern is a set of model parts",
        ],
        "key_label": "Posting rules in six lines",
        "concepts_intro": (
            "Two terms are Fowler's, as Evans summarises them; the third is Evans's own "
            "advice on borrowing."
        ),
        "concepts": [
            ("Posting Rule",
             "An object tied to an input account: an entry there is its input, from which it "
             "computes an amount by its calculation method and posts an entry to an "
             "output account. It makes explicit a dependency between accounts that would "
             "otherwise be tangled into whatever code updates them."),
            ("Firing mode",
             "When a rule runs. Eager firing runs it the moment an entry is posted; "
             "account-based firing waits until an account is told to process what has "
             "arrived since it last ran; posting-rule-based firing waits until an outside "
             "agent tells the rule to look for new entries in its input accounts."),
            ("Keeping a term's concept",
             "Using a well-known pattern's name for a concept that still means what the "
             "pattern means, however the implementation differs, and renaming it if the "
             "meaning drifts. The name then brings the pattern's understanding into the "
             "Ubiquitous Language."),
        ],
        "read_title": "The example's argument first, then the pattern, then the count",
        "read_intro": (
            "Read Insight into the Nightly Batch and Analysis Patterns Are Knowledge to "
            "Draw On, at the end of Chapter 11, in your own copy first. The lesson reads "
            "the example as an argument and Posting Rules as a tool, and then lets rules "
            "derive entries."
        ),
        "body": [
            ("p", "&ldquo;When you use a term from a well-known analysis pattern, take care "
                  "to keep the basic concept it designates intact, however much the "
                  "superficial form might change.&rdquo; That is the one change Evans "
                  "advises against, in Analysis Patterns Are Knowledge to Draw On, the "
                  "section that closes Chapter 11. This lesson reads it with the chapter's "
                  "second example, Insight into the Nightly Batch."),
            ("p", "The example begins where the first ended. With accounts and entries in "
                  "place, the clearer design shows up other problems, and the developer "
                  "adapting the nightly batch begins to recognise its behaviour in "
                  "concepts from Fowler's book. Evans "
                  "makes a general point of it: some parts of a program grew one step at a "
                  "time and look like application plumbing, not domain logic, and an "
                  "analysis pattern can show you that a model has been hiding there."),
            ("p", "The pattern he finds is Fowler's Posting Rule, which Evans summarises. "
                  "Accounting systems often hold several views of the same money, one "
                  "account tracking an amount and another tracking something worked out "
                  "from it. If the second must follow the first automatically, the code for "
                  "the two becomes intertwined, and in a system where most entries come "
                  "from such rules, that code becomes a mess. The first step is to make "
                  "each rule an object: a new entry in its input account triggers it, it "
                  "computes an amount by its calculation method, and it posts the result "
                  "to its output account."),
            ("p", "The harder part, Evans notes after Fowler, is timing: who sets a rule "
                  "going, and when. Fowler names three answers. Eager firing runs every rule "
                  "the moment an entry is posted; it is the obvious choice and usually the "
                  "least practical. Account-based firing defers the work until an account "
                  "is told to process its new entries. Posting-rule-based firing leaves it "
                  "to an outside agent, which tells each rule to fire, and the rule finds "
                  "the entries posted to its inputs since it last ran. The modes can be "
                  "mixed, but each set of rules needs one clear point of initiation. Evans "
                  "counts the three names as part of the pattern: in the Ubiquitous "
                  "Language they make a hidden decision visible and give it a vocabulary."),
            ("p", "The two developers' discussion is summarised here, not reproduced. The "
                  "batch already talks to the old accounting system through a Facade that "
                  "presents its interface as a Service, with an intention-revealing "
                  "interface for posting. They choose posting-rule-based firing: eager "
                  "firing would suit the interest charges the batch creates but not the "
                  "payments entered during the day, and it would tie the calculation to "
                  "the batch's schedule. They find they have misread the calculation "
                  "method, since their amount is always the full amount, and that the "
                  "rule's real job is choosing the ledger from the account's kind. The "
                  "batch shrinks to a loop that sends each asset a few plain messages and "
                  "commits. They depart from Fowler's details, keep the concept, and are "
                  "uneasy about one shortcut, letting the asset pick its rules through a "
                  "Singleton, which they leave for a later refactoring."),
            ("p", "The closing section says what such a pattern is for. It is hardly ever "
                  "the answer to your needs, Evans says, but it gives leads, a cleanly "
                  "abstracted vocabulary and warnings about consequences; the result may "
                  "look like the pattern, or not at all. Keep a borrowed term's concept "
                  "intact, for two reasons: the pattern's understanding comes with it, and, "
                  "more important to Evans, the Ubiquitous Language gains a term others "
                  "already know. If the meaning changes as the model evolves, change the "
                  "name too. And an analysis pattern is not a framework: a framework already "
                  "works as a whole, while an analysis pattern is a set of parts for a "
                  "model, aimed at the hardest decisions."),
            ("code", _lines(POSTING_RULE_JAVA)),
            ("p", "Now the lab, on a theatre's takings. Two rules are set: the theatre's "
                  "trust sets aside 5 per cent of ticket income for restoration, and an "
                  "agency keeps 12 per cent of the tickets it sells. In the lab, a rule "
                  "moves its share: an entry of share times amount, rounded to the cent, "
                  "half away from zero, into the output account, and the same amount "
                  "negated in the input account. On the preset "
                  "<code>levy-and-commission</code>, 4 entries are given and 6 derived: "
                  "20.63 and 4.82 to the restoration fund, 21.60 to the agency's "
                  "commission, each with its negative. The balances after, in the order "
                  "the accounts first appear, are ticket-income 483.35, restoration-fund "
                  "25.45, agency-sales 158.40, agency-commission 21.60 and bar-income "
                  "55.00."),
            ("p", "Two figures are worth a second look. Each derived pair nets to zero, so "
                  "the rules move money and never make it, the conservation of the "
                  "previous lesson. And the exact shares were 20.625 and 4.815: each "
                  "rounded up by half a cent, so the rounding left is −0.01, a cent the "
                  "fund holds that the 5 per cent does not strictly give it. The Money "
                  "lesson of Enterprise Application Patterns splits one amount so that no "
                  "cent is lost; a rule that rounds each entry on its own drifts, a little, "
                  "and a team decides with its experts whether that matters."),
            ("p", "The preset <code>donation-and-fee</code> adds a donation of 200.00 posted "
                  "straight to the restoration fund, and a third rule, trust-fee, taking 10 "
                  "per cent of what enters the fund for the trust's administration. It "
                  "fires once, on the donation: 8 derived entries, 20.00 to trust-admin, "
                  "and a fund of 205.45. It does not fire on the 20.63 and 4.82 the first "
                  "rule derived, because the lab never lets a derived entry fire a rule. "
                  "That is the lab's choice, not Fowler's: in a real system, whether a rule "
                  "sees entries other rules derived depends on the order and the point that "
                  "starts it, which is why each set of rules needs, as Evans puts it after "
                  "Fowler, one clear point of initiation and of responsibility for finding "
                  "its input entries."),
            ("h3", "Exercise"),
            ("code", _lines(MATINEE) + ["// the rule"] + _lines(MATINEE_RULES)),
            ("p", "A matinee's takings and the restoration rule alone. By hand, write every "
                  "entry the rule derives, rounding half away from zero, then give "
                  "ticket-income's and the fund's balances after and the rounding left. "
                  "Type the entries and the rule into the lab to check."),
            ("p", "Fowler's patterns supply a model for a domain. The next lesson, Strategy "
                  "and Composite in the Model, reads Chapter 12, where patterns written for "
                  "code turn out to name concepts in the domain."),
        ],
        "lab": ("dddkit", {
            "mode": "ledger",
            "view": "post",
            "preset": "levy-and-commission",
            "presets": [
                {"id": "levy-and-commission",
                 "label": "A theatre's takings, a restoration levy and an agency's commission",
                 "entries": _records(TAKINGS),
                 "rules": _records(RULES),
                 "expect": {"dleGiven": "4", "dleDerived": "6",
                            "dleBalances": "ticket-income 483.35, restoration-fund 25.45, "
                                           "agency-sales 158.40, agency-commission 21.60, "
                                           "bar-income 55.00",
                            "dleList": "restore on e1: 20.63 to restoration-fund; restore on "
                                       "e2: 4.82 to restoration-fund; agency on e3: 21.60 to "
                                       "agency-commission",
                            "dleLeft": "−0.01"}},
                {"id": "donation-and-fee",
                 "label": "A donation to the fund, and a fee on what the fund receives",
                 "entries": _records(TAKINGS_WITH_DONATION),
                 "rules": _records(RULES_WITH_FEE),
                 "expect": {"dleGiven": "5", "dleDerived": "8",
                            "dleBalances": "ticket-income 483.35, restoration-fund 205.45, "
                                           "agency-sales 158.40, agency-commission 21.60, "
                                           "bar-income 55.00, trust-admin 20.00",
                            "dleLeft": "−0.01"}},
            ],
            "panel_title": "The entries posting rules derive",
        }),
        "steps_title": "Firing posting rules by hand",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Find each rule's inputs",
             "For each rule, list the given entries posted to its input account. Derived "
             "entries are not inputs in a single pass."),
            ("Derive and round",
             "Multiply each input by the rule's share and round to the cent, half away "
             "from zero. Post that to the output account and its negative to the input."),
            ("Total and compare",
             "Add each account's entries for its balance after. Subtract each rounded "
             "share from the exact one and add the differences: that is the rounding "
             "left."),
            ("Do it on a system of your own",
             "Find a batch job or a trigger you know that writes figures derived from "
             "other figures. Write one of its rules as input, output and share, and say "
             "which of Fowler's three firing modes it uses and who starts it."),
        ],
        "worked": {
            "title": "Two rules over four entries",
            "intro": [
                "Derive the entries on <code>levy-and-commission</code>.",
            ],
            "lines": [
                "restore on e1: 0.05 × 412.50 = 20.625",
                "rounded half away from zero: 20.63",
                "restore on e2: 0.05 × 96.30 = 4.815",
                "rounded: 4.82",
                "agency on e3: 0.12 × 180.00 = 21.60",
                "e4 is bar income: no rule fires",
                "ticket-income: 508.80 − 25.45 = 483.35",
                "rounding left: −0.005 − 0.005 = −0.01",
            ],
            "after": [
                "Three inputs give three pairs, six entries in all. The rounding is done "
                "once an entry, so each half cent goes the same way; a rule that rounded "
                "the day's total instead would derive different entries.",
            ],
        },
        "quiz_title": "Rules, firing and keeping a pattern's terms",
        "quiz": [
            {"q": "In the exercise, with the restoration rule at 0.05 and rounding half away "
                  "from zero, what does the rule derive, and what is ticket-income's balance "
                  "after?",
             "a": ["1.88 and 0.90 to the fund; ticket-income 53.02",
                   "1.89 and 0.91 to the fund; ticket-income 53.00",
                   "1.89, 0.91 and 0.60 to the fund; ticket-income 53.00",
                   "2.80 to the fund in one entry; ticket-income 53.00"],
             "c": 1,
             "why": "0.05 × 37.70 = 1.885, which rounds to 1.89, and 0.05 × 18.10 = 0.905, "
                    "which rounds to 0.91: four derived entries, two to the fund and their "
                    "negatives in ticket-income. Ticket-income is 55.80 − 2.80 = 53.00 and "
                    "the fund 2.80; the rounding left is −0.005 − 0.005 = −0.01. The bar "
                    "income has no rule, and the lab derives one pair for each input entry, "
                    "not one for the total. Rounding down would give 1.88 and 0.90."},
            {"q": "On the preset <code>donation-and-fee</code>, how many entries does the "
                  "trust-fee rule derive, and why?",
             "a": ["2, from the donation only, since derived entries do not fire rules",
                   "6, from the donation and the two levy entries",
                   "0, since the fund is an output account",
                   "4, one pair for each rule that posted to the fund"],
             "c": 0,
             "why": "The only given entry in restoration-fund is the donation of 200.00, so "
                    "trust-fee derives 20.00 to trust-admin and −20.00 in the fund. The lab "
                    "fires rules once over the given entries, so the 20.63 and 4.82 the "
                    "restore rule derived do not set it off. In a system where trust-fee "
                    "ran after restore and looked up every entry since its last run, they "
                    "would, and the fee would be larger."},
            {"q": "Which firing mode do the developers in Insight into the Nightly Batch "
                  "choose, and why?",
             "a": ["Eager firing, since the batch creates the interest charges itself",
                   "Account-based firing, since each account knows its own entries",
                   "Posting-rule-based firing: the batch instructs every rule to run, and "
                   "payments entered in the day are still found",
                   "A mixture, eager for charges and account-based for payments"],
             "c": 2,
             "why": "They note that eager firing would work for the charges the batch "
                    "creates but not for payments entered during the day, and would couple "
                    "the calculation to the batch. Posting-rule-based firing keeps the "
                    "batch in control and lets each rule look for new entries itself."},
            {"q": "What does Evans advise when a model's definition of a term borrowed from "
                  "an analysis pattern changes as the model evolves?",
             "a": ["Keep the name, since the team already uses it",
                   "Keep the name and document the difference",
                   "Change the concept back to the pattern's",
                   "Change the name too"],
             "c": 3,
             "why": "Keeping a borrowed term's concept intact is the one change he warns "
                    "against breaking, because the term carries the pattern's understanding "
                    "and widely understood terms strengthen the Ubiquitous Language. If the "
                    "definition drifts anyway, he says, take the trouble to rename it."},
        ],
        "mistakes": [
            ("Treating a batch job as plumbing with no model in it",
             "Evans's example is a nightly batch nobody had thought of as domain-oriented, "
             "where domain logic had been collecting as the job grew. Fowler's Posting Rules showed the "
             "developer the model inside it, and the batch shrank to a loop over a domain "
             "layer. Code that grew step by step and looks like application logic is, "
             "Evans says, where an analysis pattern most often helps."),
            ("Keeping a pattern's name for a concept that has changed",
             "Departing from a pattern's details is expected; the team in the example "
             "dropped Fowler's calculation method altogether. What Evans warns against is "
             "a borrowed name whose concept has drifted: it imports understanding that no "
             "longer applies. Change the name with the meaning."),
            ("Leaving the timing of derived updates to the implementation",
             "When rules fire looks like a detail. Evans, following Fowler, counts the "
             "three firing modes as part of the pattern and of the Ubiquitous Language, "
             "and each set of rules needs one clear point of initiation. The lesson's "
             "second preset shows how much turns on whether a rule sees what other "
             "rules derived."),
        ],
        "standard": (
            "Finish when you can fire posting rules by hand and say when they fire.",
            "Given entries and rules, write every derived entry with its rounding, state "
            "the balances after, and name the firing mode and the point that starts it."
        ),
        "note": (
            "The lab fires each rule once over the given entries, with one rounding rule. "
            "It cannot say which firing mode, which rounding or which accounts suit your "
            "domain; those are decisions Evans's developers make with their expert, and "
            "the lab only shows what one set of choices derives."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 12, opening (PDF p. 191 of the operator's copy); Strategy (a.k.a.
    # Policy) and its route-finding example (pp. 192-194); Composite and its
    # route example (pp. 194-199); Why Not Flyweight? (pp. 199-200).
    # Quote: PDF p. 200 of the operator's copy, 24 words, quotes.py OK.
    # Lesson total: 24 words.
    {
        "slug": "strategy-and-composite",
        "title": "Strategy and Composite in the Model",
        "module": "Chapter 12 · Relating Design Patterns to the Model",
        "one_line": "Two of the Gang of Four's design patterns read on two levels at once: a technique in the code, and a concept in the domain.",
        "summary": (
            "Chapter 12 asks when a design pattern can also be a domain pattern, with "
            "Strategy, Composite and the counter-example of Flyweight. Read Evans's "
            "argument, then count the decision points of a pricing routine that tests a "
            "rider's plan in every computation, against the same prices given by "
            "interchangeable policies."
        ),
        "key": [
            "a design pattern read on two levels",
            "strategy: a policy the domain names",
            "pull the varying rule out of a process",
            "composite: parts the same kind as wholes",
            "same questions at every level",
            "flyweight: no domain concept at all",
        ],
        "key_label": "Chapter 12 in six lines",
        "concepts_intro": (
            "Three ideas from Chapter 12, the first of them the distinction the chapter "
            "is about."
        ),
        "concepts": [
            ("Domain pattern",
             "A pattern that says something about the domain, not only about the code. "
             "A design pattern from Gamma, Helm, Johnson and Vlissides can be one when it "
             "corresponds to a concept the domain has, and then it is read on two levels: "
             "a technique in the code and a concept in the model."),
            ("Strategy, or Policy",
             "A family of interchangeable ways of doing one thing, each an object of its "
             "own. As a domain pattern it separates a process's varying part, often a "
             "rule or policy the business talks about, from the stable part, so that each "
             "can be seen and changed alone."),
            ("Composite",
             "A tree whose parts are of the same kind as the whole they make up, "
             "behind one shared type: a whole answers from its parts, a single part from "
             "itself, and a client asks either the same way."),
        ],
        "read_title": "The chapter's argument first, then the patterns, then the count",
        "read_intro": (
            "Read Chapter 12, Relating Design Patterns to the Model, in your own copy "
            "first. The lesson reads its opening as an argument and its patterns as "
            "tools, and then counts the decisions a policy moves."
        ),
        "body": [
            ("p", "&ldquo;The only requirement is that the pattern should say something "
                  "about the conceptual domain, not just be a technical solution to a "
                  "technical problem.&rdquo; Evans ends Chapter 12, Relating Design Patterns "
                  "to the Model, with that test. The chapter is short: an opening, two "
                  "patterns, Strategy and Composite, and Why Not Flyweight?. Read it in "
                  "your own copy first."),
            ("p", "The argument starts from a difference of level. The patterns of Part II "
                  "and Part III were written for domain models; most published patterns "
                  "are technical. Evans quotes the authors of Design Patterns on the level "
                  "of theirs, objects and classes that communicate, tailored to a recurring "
                  "design problem in its setting, neither reusable data structures nor whole "
                  "domain-specific designs. Some of them, not all, can serve as domain "
                  "patterns, because they match concepts that arise in many domains. To use "
                  "one that way you read it twice at once: as a technical pattern in the "
                  "code and as a conceptual pattern in the model."),
            ("p", "Strategy, which Evans also calls Policy, is the first. Domain processes "
                  "often have more than one legitimate form, and once the alternatives are "
                  "written into the process, choosing among them tangles with the "
                  "alternatives themselves and the real options disappear into the rest of "
                  "the behaviour. His remedy: make the variable part an object of "
                  "the model in its own right, kept apart from the process it steers, with "
                  "one such object for each way the process can go, built as the design "
                  "pattern builds it. The design pattern's emphasis is substituting one "
                  "algorithm for another; the domain pattern's is expressing a concept, "
                  "most often a policy or a process."),
            ("p", "His example is a routing service in the book's shipping domain, tuned to "
                  "find the quickest or the least costly route, with that choice tested inside "
                  "every computation. Passing in a policy that scores each leg lets the "
                  "service treat every request the same way, its behaviour stated in one "
                  "sentence of the domain's language, and new policies need no change to "
                  "it. The design pattern's consequences "
                  "still hold, Evans adds: clients must know the strategies, which is a "
                  "modelling concern, and there are more objects, which stateless shared "
                  "strategies can reduce."),
            ("p", "Now the count, on a bike-share's ride pricing. The preset "
                  "<code>plan-tests</code> is one class's two methods, the fare and the "
                  "deposit, each testing the rider's plan. The lab counts decision points "
                  "by a stated rule, one plus one for each `if`, loop, `case`, `&&` and "
                  "`||`, and finds 7: `1 + if 4 + && 1 + || 1`, in the band 6–10. Five of "
                  "the six decisions ask which plan the rider is on, the `&&` on line 3 "
                  "asking about the ride instead, and a new plan would add a test to both "
                  "methods."),
            ("code", _lines(PLAN_TESTS)),
            ("p", "The preset <code>pricing-policies</code> gives every plan the same "
                  "prices as interchangeable policies, and the lab counts 2: `1 + if 1`, in "
                  "the band 0–5. The one test left is the member's 45 free minutes, a rule "
                  "of that policy and of the domain. The question which plan a rider is on "
                  "has not vanished: it is answered once, where a ride is given its policy, "
                  "and that code is outside the listing, so the lab does not see it. What "
                  "the count shows is that the choice no longer runs through every "
                  "computation; what makes this Strategy a domain pattern is that a pricing "
                  "plan is something riders and staff already talk about. The lab also "
                  "prints the deepest nesting of braces and the first line to reach it, 1 "
                  "at line 4 before and 2 at line 16 after, where the classes add a "
                  "level; this lesson does not lean on that measure."),
            ("code", _lines(PRICING_POLICIES)),
            ("p", "Composite is the second. Some domains nest things inside things of the "
                  "same kind. When the model does not say so, behaviour is copied at each "
                  "level, the nesting is rigid, clients use a different interface for each "
                  "level, and adding up across the hierarchy becomes complicated. Evans's "
                  "first question is whether the idea fits: are the parts truly of one "
                  "kind with the whole they belong to? If so, give whole and part one shared type, "
                  "let a whole answer a question from its parts and a single part from "
                  "itself, so that a client asks the same question at any size. Designers often stop at the structure, he notes, when "
                  "the power of the pattern is the same behaviour at every level. His "
                  "example is a shipment route made of routes, summarised: what the "
                  "developers saw as one string of legs, the experts saw as segments "
                  "planned at different times. He adds that before those segments were "
                  "needed, the plain model did fine: a design pattern earns its place "
                  "when the need for it has arrived."),
            ("code", _lines(PROGRAMME_COMPOSITE)),
            ("p", "A festival programme, above, is the lesson's own Composite: a whole "
                  "evening, a block of three acts, and one act all answer `minutes()`, and "
                  "a programme may hold programmes. Why Not Flyweight? draws the line. "
                  "Flyweight, sharing a few value objects used many times, is an "
                  "implementation option for values, not entities (Value Objects, in "
                  "The Building Blocks of a Model-Driven Design), and it says nothing about the domain. Composite is a domain "
                  "pattern because it applies to the model and the implementation alike. "
                  "Evans declines to list which design patterns qualify; he cannot think of "
                  "a domain use for Interpreter, and will not say there is none."),
            ("h3", "Exercise"),
            ("code", _lines(SEAT_SCHEMES)),
            ("p", "A theatre prices seats and refunds by the booking's scheme: standard, "
                  "concession or group. Count the decision points by the lab's rule, with "
                  "the breakdown, then sketch the three scheme policies that would give "
                  "every booking the same price and refund, and count again. Paste each "
                  "into the lab to check; the policies are yours."),
            ("p", "Chapters 11 and 12 bring models from outside. The next lesson, "
                  "Refactoring Toward Deeper Insight, reads Chapter 13, where Evans "
                  "gathers Part III into one account of when and how a model changes."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "complexity",
            "bands": [5, 10],
            "book": "other",
            "preset": "plan-tests",
            "presets": [
                {"id": "plan-tests",
                 "label": "The rider's plan tested in the fare and in the deposit",
                 "code": PLAN_TESTS,
                 "expect": {"coDecisions": "7",
                            "coBreakdown": "1 + if 4 + && 1 + || 1",
                            "coBand": "6–10", "coDepth": "1",
                            "coDeepest": "line 4"}},
                {"id": "pricing-policies",
                 "label": "The same prices as interchangeable pricing policies",
                 "code": PRICING_POLICIES,
                 "expect": {"coDecisions": "2", "coBreakdown": "1 + if 1",
                            "coBand": "0–5", "coDepth": "2",
                            "coDeepest": "line 16"}},
            ],
            "panel_title": "Where a policy's decisions go",
            "panel_intro": (
                "The lab counts decision points by a stated rule: one, plus one for each "
                "if, while, for and case, and for each conditional and and conditional "
                "or. The bands beside the count are McConnell's, from Code Complete; "
                "Evans gives no count. The listings are the lesson's."
            ),
        }),
        "steps_title": "Factoring a policy out of a process",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Count the decisions",
             "Count one, plus one for each `if`, `while`, `for`, `case`, `&&` and `||`. "
             "An `else` adds nothing."),
            ("Mark the tests on the policy",
             "For each decision, say whether it asks which policy applies or applies a "
             "rule within one. Tests of the first kind repeated across methods are what "
             "a Strategy gathers."),
            ("Write one class a policy",
             "Give each policy a class with every method that varied, and check that each "
             "input still gets the result it got before. Then name the one place where a "
             "policy is chosen."),
            ("Do it on your own code",
             "Find a routine in a system you know that tests the same kind, plan or mode "
             "in more than one method. Count its decisions, say whether the alternatives "
             "are a policy your domain's experts name, and only then decide whether a "
             "Strategy belongs in the model."),
        ],
        "worked": {
            "title": "Seven decisions, five of them on the plan",
            "intro": [
                "Count the decision points in <code>plan-tests</code>.",
            ],
            "lines": [
                "start at 1",
                "line 3: if, and &&: +2",
                "line 6: if on the plan: +1",
                "line 9: if on the plan: +1",
                "line 16: if, and ||: +2",
                "1 + if 4 + && 1 + || 1 = 7",
                "after: one if, the 45 minutes: 2",
            ],
            "after": [
                "Lines 3, 6 and 9 test the plan once each and line 16 twice; the second "
                "half of line 3 asks about the ride. The policies keep the second kind and "
                "move the first to wherever a ride is given its policy.",
            ],
        },
        "quiz_title": "Strategy, Composite and the domain-pattern test",
        "quiz": [
            {"q": "In the exercise, how many decision points does the listing have by the "
                  "lab's rule, and how many would three scheme policies have, with the "
                  "concession's row tested by an `if`?",
             "a": ["5 before, 1 after",
                   "6 before, 2 after",
                   "7 before, 2 after",
                   "6 before, 1 after"],
             "c": 1,
             "why": "One, plus three `if`s, plus the `&&` on line 6 and the `||` on line "
                    "16: `1 + if 3 + && 1 + || 1` = 6. With standard, concession and group "
                    "policies, the only test left is the concession's row beyond 10, so 1 "
                    "+ if 1 = 2. The `return` with no test adds nothing, and the starting "
                    "one is always counted."},
            {"q": "How does Evans distinguish Strategy used as a domain pattern from "
                  "Strategy as a design pattern?",
             "a": ["The domain pattern allows only one strategy at a time",
                   "The domain pattern does not need the design pattern's implementation "
                   "advice",
                   "The design pattern stresses substituting algorithms; the domain pattern "
                   "stresses expressing a concept, most often a policy or a process",
                   "The domain pattern must be implemented with subclasses of the service"],
             "c": 2,
             "why": "Evans says the design pattern's consequences and its discussion of "
                    "implementation still apply in full, since it is still a Strategy; what "
                    "changes is the motivation, which adds a layer of meaning when the "
                    "strategy is a real business policy."},
            {"q": "Why, in Why Not Flyweight?, is Flyweight not a domain pattern?",
             "a": ["It corresponds to nothing in the domain; it is an implementation "
                   "option for value objects",
                   "It cannot be implemented in Java",
                   "It applies only to entities, which have identity",
                   "It always conflicts with Composite"],
             "c": 0,
             "why": "Sharing a limited set of value objects used many times is an "
                    "implementation choice open to values and not to entities. Composite "
                    "applies to the model and to the implementation, which for Evans is "
                    "what makes a pattern a domain pattern."},
            {"q": "In Evans's statement of Composite, how do clients treat the members of "
                  "the composite?",
             "a": ["They ask a container for its leaves and add up the answers",
                   "They use a separate interface for each level",
                   "They test each member's type before calling it",
                   "They use one shared type and need not know which they hold"],
             "c": 3,
             "why": "A whole answers from its parts and a single part from itself, so "
                    "a client asks the same question at any level. A separate interface for each level is what "
                    "Evans describes as the problem when the model leaves the relatedness "
                    "out."},
        ],
        "mistakes": [
            ("Using a design pattern in the domain because it is convenient in code",
             "Evans's first concern whenever a design pattern is brought into the domain is "
             "whether its idea fits a concept the domain has. Recursion through some "
             "objects may be convenient without a real hierarchy of wholes and parts, and Flyweight "
             "is useful with no domain meaning at all. The test, which the lesson's "
             "opening quotation states, is that the pattern says something about the "
             "conceptual domain."),
            ("Thinking a Strategy removes the decision",
             "It moves it. On the lesson's illustration the count falls from 7 to 2 "
             "because the plan is no longer tested in every method; it is still chosen, "
             "once, wherever a ride is given its policy, in code the lab does not see. "
             "Evans names the related cost: clients must know the strategies exist."),
            ("Adding a Composite before the domain needs one",
             "Evans's route example ends with the observation that before the segments "
             "and their distinct legs were needed, the plain model did fine without "
             "Composite: a design pattern earns its place when the need for it has "
             "arrived. The nesting it allows is a capability, not a requirement."),
        ],
        "standard": (
            "Finish when you can say whether a design pattern is also a domain pattern.",
            "Count a routine's decisions before and after a Strategy, name where the "
            "choice of policy went, and say what concept the pattern names in the domain."
        ),
        "note": (
            "The lab counts decisions in the listing it is given. It does not see the "
            "code that chooses a policy, and it cannot say whether a plan, a scheme or a "
            "programme is a concept your domain's experts use; that, for Evans, is what "
            "decides whether a design pattern belongs in the model."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 13, opening (PDF p. 201 of the operator's copy); Initiation (p. 201);
    # Exploration Teams (pp. 201-202); Prior Art (p. 202); A Design for
    # Developers (p. 203); Timing (p. 203); Crisis as Opportunity (pp. 203-204).
    # Quote: PDF p. 203 of the operator's copy, 17 words, quotes.py OK.
    # Lesson total: 17 words.
    {
        "slug": "refactoring-toward-deeper-insight",
        "title": "Refactoring Toward Deeper Insight",
        "module": "Chapter 13 · Refactoring Toward Deeper Insight",
        "one_line": "Changing the model, and the code with it, because the team has understood the domain better, not only because the code is untidy.",
        "summary": (
            "Chapter 13 gathers Part III into one account of refactoring driven by "
            "insight into the domain: how it starts, who explores, where ideas come from, "
            "when to do it and when not. Read it, then count the modules a clinic's "
            "change requests reach before and after a rule that lived in three places "
            "becomes one explicit concept."
        ),
        "key": [
            "live in the domain",
            "keep looking at things differently",
            "keep talking with the experts",
            "small teams, short sessions, sleep",
            "refactor before you can justify it",
            "not the day before a release",
            "a crisis can be a breakthrough",
        ],
        "key_label": "Chapter 13 in seven lines",
        "concepts_intro": (
            "Three ideas from Chapter 13, the last of them what the lab counts."
        ),
        "concepts": [
            ("Refactoring toward deeper insight",
             "Restructuring code because the model behind it has improved: a missing "
             "concept found, a relationship corrected, a design made suppler. It sits on "
             "top of ordinary refactoring, the small behaviour-preserving changes made "
             "at the keyboard, which goes on all the time."),
            ("Exploration team",
             "A small group gathered for one design problem, some developers who know "
             "that area or model well and, where there are subtleties, a domain expert, meeting two or three times "
             "over a few days and then disbanding."),
            ("Modules a change touches",
             "For one change request, the number of distinct modules holding the "
             "classes it alters. A rule written in three modules sends one change to "
             "three; the same rule as one concept sends it to one."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read Chapter 13, Refactoring Toward Deeper Insight, in your own copy first; "
            "it is a few pages. The lesson reads it as an argument, section by section, "
            "and then counts what one such refactoring changes."
        ),
        "body": [
            ("p", "&ldquo;If you wait until you can make a complete justification for a "
                  "change, you've waited too long.&rdquo; That is the first sentence of "
                  "Timing, in Chapter 13, Refactoring Toward Deeper Insight. The chapter is "
                  "short and gathers the five before it into one account. Read it in your "
                  "own copy first."),
            ("p", "Evans opens with three things to focus on: live in the domain, keep "
                  "changing the angle you look at it from, and keep an unbroken dialogue with "
                  "the domain experts. He then places the chapter beside the classic "
                  "picture of refactoring, a developer or two at the keyboard improving "
                  "code in small steps with unit tests to confirm nothing broke, the "
                  "practice read in Code Complete's lesson Refactoring Safely. That should go on all "
                  "the time, he says, but it is not the whole story; Part III has laid an "
                  "expanded view over it."),
            ("p", "Initiation says where the expanded kind begins. It may begin with a "
                  "problem in the code, an awkwardness whose root the developers sense is "
                  "in the model, a concept missing or a relationship wrong. Unlike the "
                  "conventional kind, it may also begin when the code looks tidy: when the "
                  "model's language has drifted from the experts', when new requirements "
                  "do not fit naturally, or when a developer has simply learned more. "
                  "Finding where the trouble lies is often the least certain step; then the team "
                  "can search deliberately, with colleagues, experts and written "
                  "patterns."),
            ("p", "Exploration Teams says who does the searching when a change needs more "
                  "than a few hours. The initiators gather a few people who know the area "
                  "or model well, with a domain expert where there are subtleties, and "
                  "brainstorm for between half an hour and an hour and a half, sketching and walking through scenarios; "
                  "then they code what they found or sleep on it and meet again a couple "
                  "of days later. Evans names three keys: self-determination, since the "
                  "team forms and disbands with no standing structure; scope and sleep, a "
                  "few short meetings over a few days, and a smaller piece of the problem "
                  "if the team is stuck; and exercising the Ubiquitous Language, whose "
                  "refinement is what the developers take back and put into code."),
            ("p", "Prior Art says where ideas come from: books about the domain itself, "
                  "analysis patterns such as the two this course has read, design patterns "
                  "where they fit both the implementation and the concept, and formalisms "
                  "such as arithmetic or predicate logic where one fits part of the domain. "
                  "A Design for Developers recalls why it matters: software is also for "
                  "the developers who change it again and again, and a supple design lets "
                  "them anticipate what code does and so what changing it will do."),
            ("p", "Timing makes the chapter's sharpest claim. Teams are too cautious: what "
                  "they notice is the danger in touching code and the hours a change "
                  "takes, and what they miss is the danger of living with a clumsy design "
                  "and the hours spent coding around it. Demanding a justification first sounds reasonable, Evans "
                  "says, and tends to stop refactoring or drive it underground, because "
                  "the costs and benefits cannot be calculated accurately. So, he says, "
                  "refactor when the design no longer says what the team now understands, when "
                  "important concepts are implicit and you see how to make them explicit, "
                  "or when you see a chance to make an important part suppler. And he "
                  "fences it: not the day before a release, not supple designs that show "
                  "off technique but miss the core of the domain, not a deeper model a "
                  "domain expert would not use. Be undogmatic, he ends, but lean toward "
                  "refactoring."),
            ("p", "Crisis as Opportunity closes with a story from biology. For a century "
                  "after Darwin, evolution was pictured as steady change; in the 1970s, "
                  "with the punctuated-equilibrium model that Niles Eldredge and Stephen "
                  "Jay Gould proposed (names Evans does not give), it came to be seen as long stability broken by short "
                  "bursts. Evans's point is that refactoring toward deeper insight has "
                  "that rhythm too. A breakthrough often arrives looking like a crisis, a "
                  "model suddenly seen to be inadequate or wrong, and it means the team now "
                  "understands more; then steady refinement starts again. Breakthrough, in "
                  "Breakthroughs and Implicit Concepts, read his story of one."),
            ("p", "Now the lab, on a clinic's appointment system. Its rule for late "
                  "cancellation, a 24-hour window with urgent visits exempt, is nowhere a "
                  "concept: the booking screen, the reminder job and the invoice run each "
                  "work it out, and urgency is a flag on the patient record. On the preset "
                  "<code>rule-implicit</code> the lab takes 6 classes in 4 modules and 4 "
                  "change requests, and counts the modules each touches: widening the "
                  "window to 48 hours 3, exempting urgent visits 3, a new fee amount 1, a "
                  "new reminder text 1. That is 8 module touches in all, and 2 changes "
                  "confined to one module. The window change and the exemption tie for the "
                  "largest, at 3; the tile shows the first given, and the status line "
                  "names both."),
            ("code", _lines(CANCELLATION_POLICY_JAVA)),
            ("p", "The preset <code>rule-explicit</code> is the same system after the "
                  "refactoring that makes the rule explicit: a CancellationPolicy class, "
                  "above, in a module of its own that the other three call. The window "
                  "change now touches 1 module, the urgent exemption 2, since the screen "
                  "must still show it, and the other two changes 1 each: 5 module touches, "
                  "3 changes confined to one module, the largest 2. The count says how far "
                  "these four requests reach in each design. It does not say the "
                  "refactoring was worth its cost, and a different list of requests would "
                  "give different figures; Evans's point in Timing is that no one can "
                  "calculate that in advance."),
            ("h3", "Exercise"),
            ("code", _lines(TIMETABLE_EXERCISE)),
            ("p", "A school timetable, before and after the length of a period becomes a "
                  "Period class in its own module. By hand, give the modules each change "
                  "touches in each design, the total module touches and the changes "
                  "confined to one module. Then enter both designs into the lab to "
                  "check."),
            ("p", "That ends Part III. The next course, Maintaining Model Integrity, opens "
                  "Part IV with Bounded Context: what happens when more than one model is "
                  "at work in a system, and how to keep each one consistent."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "change",
            "preset": "rule-implicit",
            "presets": [
                {"id": "rule-implicit",
                 "label": "A clinic's late-cancellation rule written into three modules",
                 "elements": _records(CLINIC_ELEMENTS),
                 "changes": _records(CLINIC_CHANGES_IMPLICIT),
                 "expect": {"dmoChanges": "4",
                            "dmoPer": "window-48h 3, urgent-exempt 3, fee-amount 1, "
                                      "reminder-text 1",
                            "dmoTotal": "8",
                            "dmoConfined": "2 of 4: fee-amount, reminder-text",
                            "dmoLargest": "window-48h, 3 modules"}},
                {"id": "rule-explicit",
                 "label": "The same system with the rule as an explicit CancellationPolicy",
                 "elements": _records(CLINIC_ELEMENTS_EXPLICIT),
                 "changes": _records(CLINIC_CHANGES_EXPLICIT),
                 "expect": {"dmoPer": "window-48h 1, urgent-exempt 2, fee-amount 1, "
                                      "reminder-text 1",
                            "dmoTotal": "5",
                            "dmoConfined": "3 of 4: window-48h, fee-amount, reminder-text",
                            "dmoLargest": "urgent-exempt, 2 modules"}},
            ],
            "panel_title": "The modules each change request reaches",
        }),
        "steps_title": "Counting what a deeper model changes",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("List the classes and modules",
             "Write each class with the module it lives in, before the refactoring and "
             "after it, including any class the refactoring adds."),
            ("List the change requests",
             "For each request the system has had or expects, write the classes it "
             "alters in each design. Use the same requests for both."),
            ("Count the modules",
             "For each request, count the distinct modules among its classes. Add them "
             "for the total, and count the requests that stay inside one module."),
            ("Do it on a system of your own",
             "Pick a rule in a system you know that is worked out in more than one place. "
             "Count the modules your last three changes to it touched, and say in a "
             "sentence which of Evans's three reasons in Timing applies, if any."),
        ],
        "worked": {
            "title": "Four requests, before the refactoring",
            "intro": [
                "Count the modules each request touches on <code>rule-implicit</code>.",
            ],
            "lines": [
                "window-48h: ui, scheduling, billing: 3",
                "urgent-exempt: ui, billing, patients: 3",
                "fee-amount: billing: 1",
                "reminder-text: scheduling: 1",
                "total: 3 + 3 + 1 + 1 = 8",
                "confined to one module: 2",
                "after: 1 + 2 + 1 + 1 = 5, confined 3",
            ],
            "after": [
                "The two requests that were about the rule fall from three modules to one "
                "and two; the two that were not stay where they were. That is the shape "
                "of the gain, on these requests and no others.",
            ],
        },
        "quiz_title": "Timing, teams and what a refactoring reaches",
        "quiz": [
            {"q": "In the exercise, what are the total module touches and the changes "
                  "confined to one module, before and after the Period class?",
             "a": ["before 6 and 1; after 3 and 3",
                   "before 6 and 0; after 3 and 3",
                   "before 5 and 1; after 3 and 2",
                   "before 6 and 1; after 4 and 2"],
             "c": 0,
             "why": "Before: longer-periods touches scheduling, rooms and exams, 3; "
                    "short-fridays scheduling and exams, 2; attendance reports, 1: a total "
                    "of 6, with only attendance confined to one module. After: each change "
                    "touches one module, periods, periods and reports: 3, all three "
                    "confined. The attendance change was never about periods and is "
                    "unchanged."},
            {"q": "On the preset <code>rule-explicit</code>, why does the urgent exemption "
                  "still touch two modules?",
             "a": ["Urgency is still a flag on the patient record",
                   "The booking screen must still show the exemption, besides the policy "
                   "changing",
                   "The invoice run still computes the window itself",
                   "The lab counts the new module twice"],
             "c": 1,
             "why": "After the refactoring the exemption is a clause of CancellationPolicy, "
                    "in the appointments module, and the screen in ui must display it: two "
                    "modules. The invoice run and the patient record no longer hold the "
                    "rule, so they are not touched."},
            {"q": "Which of these does Evans, in Timing, name as a time not to refactor?",
             "a": ["When the code already looks tidy",
                   "When an important concept is implicit in the design",
                   "The day before a release",
                   "Before you can fully justify the change"],
             "c": 2,
             "why": "He fences his aggressive attitude with three don'ts: not the day before "
                    "a release, not supple designs that only display technique, and not a "
                    "deeper model the domain expert would not use. Tidy code can still call "
                    "for it (Initiation), an implicit concept is one of his three reasons "
                    "to refactor, and waiting for a full justification is waiting too "
                    "long."},
            {"q": "What does Evans advise an exploration team to do if it gets stuck?",
             "a": ["Meet for longer until the design is settled",
                   "Hand the problem to the most senior developer",
                   "Write down the costs and benefits before going on",
                   "Narrow the problem to a smaller part of the design"],
             "c": 3,
             "why": "Under scope and sleep he says that dragging the sessions out does not "
                    "help, that being stuck may mean taking on too much at once, and that "
                    "the team should narrow its focus. The team is self-determined and "
                    "short-lived, and Timing argues against demanding a full justification "
                    "first."},
        ],
        "mistakes": [
            ("Waiting to refactor until the change can be fully justified",
             "Evans's Timing argues that by then the costs are already being paid and "
             "the code is harder to change, and that development is not predictable "
             "enough for a change's benefits, or the cost of not making it, to be "
             "calculated accurately. On the lesson's illustration the lab counts how far "
             "four requests reach in each design; it cannot price the refactoring, and "
             "neither, he says, can anyone."),
            ("Refactoring only when the code smells",
             "The conventional trigger is awkward code. Evans adds triggers that can "
             "appear while the code looks tidy: a model whose language has drifted from "
             "the experts', requirements that do not fit naturally, or a developer who "
             "has learned enough to see a better model."),
            ("Taking the case for refactoring as licence for any change",
             "Evans fences his own advice: not the day before a release, not supple "
             "designs that show off technique without reaching the core of the domain, "
             "not a deeper model a domain expert would not use. He asks teams to lean "
             "toward refactoring without being absolute about it."),
        ],
        "standard": (
            "Finish when you can say why and when to refactor toward a deeper model.",
            "Given a system before and after a concept is made explicit, count the "
            "modules each change touches in both, and name the reason in Timing that "
            "applies."
        ),
        "note": (
            "The lab counts modules over the requests listed. It cannot choose which "
            "requests are likely, weigh the cost of the refactoring, or say whether the "
            "new concept is one the experts recognise; Evans's last condition, a model "
            "the expert would use, is the one no count reaches."
        ),
    },
]
