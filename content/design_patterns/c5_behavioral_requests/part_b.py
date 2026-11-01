"""Behavioral Patterns I, lesson 6 -- Memento.

Gamma, Helm, Johnson and Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995), Chapter 5, Memento. Pages in
the comments are PDF pages of the operator's copy; the lesson cites by
chapter, section and pattern. The quotation is copied from that copy and
checked with quotes.py. The design, records and Java are written for the
lesson: none of the book's code, diagrams or example data (the constraint
solver and its connected shapes) is reproduced or used as lab data. The design
is docs/design-patterns/PLAN.md, section C, Course 5.
"""

from .part_a import _lines, _records

# A map tile viewer's view: zoom level and the centre's position.
TILES_STATE = "zoom, 3; x, 120; y, 80"

TILES_COMMANDS = """nearer, add, zoom, 1;
farther, add, zoom, -1;
east, add, x, 40;
home, set, x, 0;
level, set, y, 0"""

TILES_SCRIPT = "nearer nearer east home level undo farther"

# A quiz app's scoreboard: six players' scores.
BOARD_STATE = "ana, 0; ben, 0; cai, 0; dev, 0; eli, 0; fay, 0"

BOARD_COMMANDS = """ana2, add, ana, 2;
ben1, add, ben, 1;
fix, set, cai, 5;
wipe, set, ana, 0"""

BOARD_SCRIPT = "ana2 ben1 fix wipe ana2"

LOCKER_EXERCISE = """// state, as cell, value
free, 12; held, 0; fee, 3
// commands, as command, op, cell, amount
drop, add, held, 1;
pick, add, held, -1;
surge, set, fee, 5
// the script
drop drop surge pick undo"""

MEMENTO_JAVA = """final class TileView {                        // the Originator
    private int zoom, x, y;

    Snapshot save() { return new Snapshot(zoom, x, y); }

    void restore(Snapshot s) { zoom = s.zoom; x = s.x; y = s.y; }

    // The Memento. Its fields and constructor are private, so only the
    // enclosing TileView can make one or read it: the wide interface.
    static final class Snapshot {
        private final int zoom, x, y;
        private Snapshot(int zoom, int x, int y) {
            this.zoom = zoom; this.x = x; this.y = y;
        }
    }
}"""

CARETAKER_JAVA = """// The Caretaker keeps snapshots and hands them back. It sees only the
// type, which is the narrow interface: it cannot look inside one.
final class ViewHistory {
    private final Deque<TileView.Snapshot> saved = new ArrayDeque<>();

    void checkpoint(TileView view) { saved.push(view.save()); }

    void undo(TileView view) {
        if (!saved.isEmpty()) {
            view.restore(saved.pop());
        }
    }
}"""


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Memento (PDF pp. 303-311 of the operator's copy).
    # Quote: PDF p. 303 of the operator's copy, the Intent, 21 words,
    # quotes.py OK. Lesson total: 21 words.
    {
        "slug": "memento",
        "title": "Memento",
        "module": "Chapter 5 · Behavioral Patterns",
        "one_line": "An object that holds a snapshot of another object's internal state, so it can be restored later by objects that never see what the state is.",
        "summary": (
            "Memento lets an object hand out a record of its own state that only it can "
            "read, so undo and checkpoints work without breaking its encapsulation. Read "
            "the narrow and wide interfaces, the cost of mementos and the case for "
            "storing only what changed, then run a map viewer's history and count the "
            "values kept as full snapshots against inverse operations."
        ),
        "key": [
            "save state without exposing it",
            "only the originator reads a memento",
            "the caretaker only holds it",
            "a narrow and a wide interface",
            "snapshots cost every cell",
            "an inverse keeps only what it replaced",
        ],
        "key_label": "Memento in six lines",
        "concepts_intro": "Three terms carry the lesson, all of them the pattern's.",
        "concepts": [
            ("Originator",
             "The object whose state is saved. It makes a memento holding a snapshot of "
             "its own internal state, and later restores itself from one; it alone "
             "decides what goes in."),
            ("Caretaker",
             "The object that keeps mementos safe and passes them back, such as an undo "
             "mechanism. It never examines or changes what a memento contains."),
            ("Narrow and wide interface",
             "The two faces of a memento. The caretaker sees the narrow one, which lets "
             "it hold the memento and pass it on and nothing more; the originator sees "
             "the wide one, which gives it everything it needs to restore itself."),
        ],
        "read_title": "The pattern first, then its costs, then the count",
        "read_intro": (
            "Read Memento in your own copy first, including its Known Uses, which link "
            "it back to Iterator. The lesson reads the pattern as a tool and counts what "
            "a history keeps under two schemes."
        ),
        "body": [
            ("p", "&ldquo;Without violating encapsulation, capture and externalize an "
                  "object's internal state so that the object can be restored to this "
                  "state later.&rdquo; That is Memento's Intent, the last pattern of this "
                  "course and the one that Command's undo and Iterator's cursors both "
                  "point to. This lesson reads it section by section; read it in your own "
                  "copy first."),
            ("p", "The motivation is undo and checkpoints. To put an object back as it "
                  "was, its state must be saved somewhere, yet an object normally hides its "
                  "state, and exposing it would cost the reliability and extensibility "
                  "encapsulation buys. The book's example is a graphical editor in which a "
                  "constraint solver keeps connected shapes connected as they move. "
                  "Undoing a move by moving the shape back the same distance need not put "
                  "everything where it was, because the solver may have resolved slack "
                  "differently, and the solver's public interface is not enough to reverse "
                  "it exactly. So the editor asks the solver for a memento before the move "
                  "and gives it back on undo, and the solver restores its own equations "
                  "and variables from it."),
            ("p", "The participants, as you would apply them. The Memento holds whatever "
                  "part of the Originator's state the originator decides to put in it, and "
                  "lets no one else at it. The Originator makes a memento of where it stands "
                  "now and later resets itself from one. The Caretaker keeps the memento and "
                  "never looks inside. The collaboration is short: the caretaker asks for a "
                  "memento, holds it a while and hands it back, or never does if no undo "
                  "comes. A memento does nothing by itself; only the originator that made it "
                  "writes or reads what it holds."),
            ("code", _lines(MEMENTO_JAVA)),
            ("p", "Java gives the two interfaces directly, as the sketch shows: a nested "
                  "class whose fields and constructor are private can be made and read by "
                  "the class that encloses it and by nothing else, while any class may hold "
                  "a reference to it. The book's C++ does the same by making the "
                  "originator a friend of the memento, and its first implementation issue "
                  "is exactly this: ideally the language offers two levels of protection. "
                  "The pattern fits when two things hold together: an object must be put "
                  "back to an earlier state, so part of that state has to be kept "
                  "somewhere, and handing the state out through ordinary getters would show "
                  "other objects how the object is built."),
            ("code", _lines(CARETAKER_JAVA)),
            ("p", "Five consequences, and the authors are candid about the costs. Memento "
                  "preserves encapsulation boundaries, keeping state only the originator "
                  "should manage out of other objects' reach even though it is stored "
                  "outside it. It simplifies the originator, which no longer keeps every "
                  "version clients asked for. But mementos may be expensive, if the "
                  "originator must copy a lot of state or mementos are made often; unless "
                  "saving and restoring is cheap, the pattern may not fit. Some languages "
                  "make narrow and wide interfaces hard to enforce. And there are hidden "
                  "costs in caring for them: the caretaker cannot see how much state a "
                  "memento holds, so a light caretaker can carry a heavy load."),
            ("p", "The second implementation issue answers the cost. When mementos are made "
                  "and returned in a predictable order, as on a command history where undo "
                  "and redo go in sequence, a memento can store only the incremental change "
                  "rather than the whole state, which is why a Command can keep just what "
                  "it needs for undo. The Sample Code builds the editor's move command with "
                  "a solver memento; the Known Uses are Unidraw's connectivity solver, the "
                  "iteration state of Dylan's collections, a memento by another name, and "
                  "the QOCA constraint toolkit, whose mementos hold only the variables "
                  "that changed and so must be restored in order. Related Patterns: "
                  "Command, which can keep undo state in mementos, and Iterator, since a "
                  "memento can hold an iteration's state, as Dylan's collections do; "
                  "Iterator's own Implementation calls its cursor a simple memento."),
            ("p", "Now the lab, on a map tile viewer whose state is its zoom level and the "
                  "position of its centre: zoom 3, x 120, y 80. Five commands: "
                  "<code>nearer</code> and <code>farther</code> add 1 and −1 to the zoom, "
                  "<code>east</code> adds 40 to x, <code>home</code> sets x to 0 and "
                  "<code>level</code> sets y to 0. On the preset <code>tiles</code> the "
                  "script zooms in twice, moves east, goes home, levels, undoes the level "
                  "and zooms out. The final view is zoom 4, x 0, y 80; the undo stack holds "
                  "5 commands and the redo stack none, because <code>farther</code> "
                  "discarded the 1 entry the undo had put there. Under the inverse scheme "
                  "the history holds 1 value, the 160 that <code>home</code> replaced: each "
                  "<code>add</code> is undone by subtracting, and the <code>level</code> "
                  "that replaced a y value has gone with the discarded redo entry."),
            ("p", "The preset <code>tiles-snapshot</code> runs the same script under the "
                  "snapshot scheme, a full memento of all 3 cells for each of the 5 "
                  "entries: 15 values against the inverse scheme's 1. The states are the "
                  "same step for step; only what is kept differs. The preset "
                  "<code>scoreboard</code>, a quiz app's six players, shows the cost "
                  "growing with the originator: 5 entries, of which two are sets, hold 2 "
                  "values as inverses and 5 × 6 = 30 as snapshots. That is the authors' "
                  "warning about expensive mementos in a number. It is not a verdict on "
                  "snapshots: an inverse is exact here only because adding whole numbers "
                  "is exactly reversible, and the book's case for a memento is the solver "
                  "whose effects are not."),
            ("h3", "Exercise"),
            ("code", _lines(LOCKER_EXERCISE)),
            ("p", "A parcel locker bank's counters. By hand, run the script, give the final "
                  "state and both stacks, and count the values the history holds at the "
                  "end under each scheme. Then type it into the lab and switch the scheme "
                  "to check, and say which cell every snapshot stores without any command "
                  "ever touching it."),
            ("p", "This course ends here, half way through Chapter 5. The next course, "
                  "Behavioral Patterns II: Notification, State and Algorithms, and the "
                  "Conclusion, reads its other five patterns, beginning with Observer, "
                  "then State, Strategy, Template Method and Visitor, the chapter's "
                  "Discussion of Behavioral Patterns, and the book's last chapter."),
        ],
        "lab": ("gofkit", {
            "mode": "history",
            "view": "undo",
            "preset": "tiles",
            "presets": [
                {"id": "tiles",
                 "label": "A map tile viewer, undo kept as inverse operations",
                 "state": TILES_STATE, "commands": _records(TILES_COMMANDS),
                 "script": TILES_SCRIPT, "scheme": "inverse",
                 "expect": {"ghiFinal": "zoom 4, x 0, y 80",
                            "ghiUndo": "5: nearer, nearer, east, home, farther",
                            "ghiRedo": "0: none", "ghiRefused": "undo 0, redo 0",
                            "ghiDiscarded": "1", "ghiStored": "1",
                            "ghiOther": "snapshot: 15"}},
                {"id": "tiles-snapshot",
                 "label": "The same viewer, undo kept as full snapshots",
                 "state": TILES_STATE, "commands": _records(TILES_COMMANDS),
                 "script": TILES_SCRIPT, "scheme": "snapshot",
                 "expect": {"ghiFinal": "zoom 4, x 0, y 80", "ghiStored": "15",
                            "ghiOther": "inverse: 1"}},
                {"id": "scoreboard",
                 "label": "A quiz scoreboard of six players",
                 "state": BOARD_STATE, "commands": _records(BOARD_COMMANDS),
                 "script": BOARD_SCRIPT, "scheme": "inverse",
                 "expect": {"ghiFinal": "ana 2, ben 1, cai 5, dev 0, eli 0, fay 0",
                            "ghiUndo": "5: ana2, ben1, fix, wipe, ana2",
                            "ghiStored": "2", "ghiOther": "snapshot: 30"}},
            ],
            "panel_title": "Snapshots against inverse operations",
        }),
        "steps_title": "Counting what a history keeps",
        "steps_intro": "Four steps, the last of them on an application of your own.",
        "steps": [
            ("Run the script",
             "Work through the commands, undos and redos with two stacks, as in the "
             "lesson Command, and write the state after each step. The scheme does not "
             "change the states."),
            ("Count the snapshots",
             "Under full snapshots, each entry on either stack keeps a memento of every "
             "cell: entries times cells, whether or not the command touched them."),
            ("Count the inverses",
             "Under inverse operations, an addition is undone by subtracting and keeps "
             "nothing; a set keeps the one value it replaced. Count the sets on the two "
             "stacks."),
            ("Do it on an application of your own",
             "Pick an object in a system you know that needs undo or a checkpoint. "
             "Estimate the size of its state and of a typical change, say whether every "
             "change can be reversed exactly from its inputs, and choose between "
             "snapshots and incremental mementos with a reason."),
        ],
        "worked": {
            "title": "The tile viewer's history, both ways",
            "intro": [
                "Count what <code>tiles</code> keeps at the end of its script.",
            ],
            "lines": [
                "nearer, nearer: zoom 4, then 5",
                "east: x 160; home: x 0; level: y 0",
                "undo level: y 80; redo stack holds level",
                "farther: zoom 4; level is discarded",
                "stacks: 5 entries, 0 on the redo stack",
                "inverse: 1 set, home, so 1 value",
                "snapshot: 5 entries × 3 cells, so 15 values",
            ],
            "after": [
                "Both schemes restore the same states. The snapshot scheme pays for every "
                "cell on every entry; the inverse scheme pays only where a value was "
                "overwritten.",
            ],
        },
        "quiz_title": "Mementos, interfaces and their cost",
        "quiz": [
            {"q": "In the exercise, counting what both stacks hold at the end, how many "
                  "values does the history keep under inverse operations and under full "
                  "snapshots?",
             "a": ["1 and 12", "1 and 9", "2 and 12", "0 and 12"],
             "c": 0,
             "why": "After drop, drop, surge and pick, the undo takes pick back: the undo "
                    "stack holds drop, drop and surge and the redo stack holds pick, 4 "
                    "entries. Only surge is a set, so the inverse scheme keeps 1 value, the "
                    "fee of 3 it replaced; snapshots keep 4 × 3 = 12. Nine counts only the "
                    "undo stack; 2 counts pick's addition as storing a value; 0 forgets the "
                    "set. The final state is free 12, held 2, fee 5, and every snapshot "
                    "stores free, which no command touches."},
            {"q": "What can the caretaker do with a memento through its narrow interface?",
             "a": ["Read the saved state but not change it",
                   "Change the saved state but not read it",
                   "Hold it and pass it to other objects, and nothing more",
                   "Restore the originator from it directly"],
             "c": 2,
             "why": "The caretaker sees a narrow interface that lets it only pass the "
                    "memento on; only the originator, through the wide interface, reads or "
                    "sets its state, and the originator restores itself."},
            {"q": "When, according to Implementation, can a memento store only the "
                  "incremental change instead of the whole state?",
             "a": ["When mementos are made and returned to the originator in a "
                   "predictable sequence",
                   "When the originator's state is small",
                   "When the caretaker is allowed to read the memento",
                   "Whenever the language has garbage collection"],
             "c": 0,
             "why": "If mementos come back in a known order, as on a command history, each "
                    "need only hold what changed since the one before. The cost is the "
                    "one QOCA's Known Use shows: such mementos cannot be restored in any "
                    "order."},
            {"q": "On the preset <code>tiles</code>, the inverse scheme keeps exactly 1 "
                  "value at the end. Which?",
             "a": ["The y value of 80 that level replaced",
                   "The x value of 160 that home replaced",
                   "The zoom of 3 before the first nearer",
                   "None: the 1 counts the discarded redo entry"],
             "c": 1,
             "why": "The stacks end with nearer, nearer, east, home and farther. Only home "
                    "is a set, and it keeps the x of 160 it overwrote. level replaced y "
                    "too, but it was undone and its redo entry was discarded by farther, "
                    "so nothing of it remains."},
        ],
        "mistakes": [
            ("Opening the originator's state so undo can save it",
             "Getters and setters for every private field let an undo mechanism save and "
             "restore an object, at the price the pattern exists to avoid: its "
             "implementation becomes everyone's business. A memento gives the saved "
             "state to the originator alone. On the lesson's illustration the "
             "<code>ViewHistory</code> stores 15 values it cannot read."),
            ("Assuming a memento is cheap because the caretaker is",
             "The caretaker cannot see how much a memento holds, so a small history "
             "class can carry a great deal of state. The authors list this hidden cost, "
             "and the expense of copying large state often, among the consequences."),
            ("Undoing by inverse where the inverse is not exact",
             "Moving a shape back the distance it moved does not undo what a constraint "
             "solver did in between; that is the book's motivating case. An inverse "
             "operation is enough only when the change can be reversed exactly from its "
             "inputs; otherwise a memento of the state is needed."),
        ],
        "standard": (
            "Finish when you can say what a history keeps under each scheme.",
            "Given a state, commands and a script, give the final state and both stacks, "
            "count the values kept as snapshots and as inverses, and name the "
            "originator, the caretaker and the two interfaces in a design you know."
        ),
        "note": (
            "The lab's inverse operations are exact because they add and set whole "
            "numbers. It cannot show a change whose inverse is not exact, which is the "
            "case the pattern was written for, or the time copying a large state takes; "
            "it counts the values kept on the design stated."
        ),
    },
]
