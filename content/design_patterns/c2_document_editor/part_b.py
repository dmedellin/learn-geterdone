"""A Case Study: Designing a Document Editor, lessons 6-7 -- Chapter 2, sections 2.7-2.9.

Gamma, Helm, Johnson and Vlissides, Design Patterns (Addison-Wesley, 1995),
Chapter 2: 2.7 User Operations (Command), 2.8 Spelling Checking and
Hyphenation (Iterator and Visitor) and 2.9 Summary. Pages in the comments are
PDF pages of the operator's copy; the lessons cite by chapter, section and
pattern. Every quotation is copied from that copy and checked with quotes.py.
Lexi's design is summarised in prose; the designs, records and code are
written for these lessons (a garden irrigation controller, the recipe book of
lesson 1, a mixtape), and none of the book's code, diagrams or example data is
reproduced. The design is docs/design-patterns/PLAN.md, section C, Course 2.
"""

from .part_a import MIXTAPE, RECIPE_BOOK, _lines, _records


# ---------------------------------------------------------------- 2.7 records

# A garden irrigation controller: minutes of watering for two zones.
GARDEN_STATE = "front, 20; back, 30"
GARDEN_COMMANDS = "boost, add, front, 10; trim, add, back, -5; rain, set, front, 0; summer, set, back, 45"
GARDEN_SCRIPT = "boost trim rain undo undo redo summer undo"
GARDEN_REFUSALS = "boost undo undo redo redo redo"

# Exercise: the same controller, another script.
GARDEN_EXERCISE = """state:    front 20, back 30
commands: boost  add front +10    trim   add back -5
          rain   set front 0      summer set back 45
script:   rain boost undo trim redo undo"""

ZONE_COMMAND_JAVA = """// A command remembers what it needs to undo itself.
interface Command {
    void execute();
    void unexecute();
}
final class SetMinutes implements Command {
    private final Zone zone;
    private final int minutes;
    private int before;                  // stored by execute
    SetMinutes(Zone zone, int minutes) {
        this.zone = zone; this.minutes = minutes;
    }
    public void execute() {
        before = zone.minutes();
        zone.setMinutes(minutes);
    }
    public void unexecute() { zone.setMinutes(before); }
}"""

HISTORY_JAVA = """// The history: done commands on one stack, undone on the other.
final class History {
    private final Deque<Command> done = new ArrayDeque<>();
    private final Deque<Command> undone = new ArrayDeque<>();
    // c is a fresh command per request; a reused one would be copied first
    void run(Command c) { c.execute(); done.push(c); undone.clear(); }
    void undo() {
        if (done.isEmpty()) { return; }          // nothing to undo
        Command c = done.pop(); c.unexecute(); undone.push(c);
    }
    void redo() {
        if (undone.isEmpty()) { return; }        // nothing to redo
        Command c = undone.pop(); c.execute(); done.push(c);
    }
}"""


# ---------------------------------------------------------------- 2.8 records

BOOK_VISITOR_JAVA = """// One accept per element class; one visit method per element class.
interface BookVisitor {
    void visitSection(Section s);
    void visitRecipe(Recipe r);
    void visitPhoto(Photo p);
}
interface BookPart { void accept(BookVisitor v); }
final class Recipe implements BookPart {
    public void accept(BookVisitor v) { v.visitRecipe(this); }
}
final class ShoppingList implements BookVisitor {
    private final List<String> items = new ArrayList<>();
    public void visitSection(Section s) { }               // nothing to buy
    public void visitRecipe(Recipe r) { items.addAll(r.ingredients()); }
    public void visitPhoto(Photo p) { }
    List<String> items() { return items; }
}"""


LESSONS = [
    # ---------------------------------------------------------------- 06
    # 2.7 User Operations (PDF pp. 78-84 of the operator's copy): the
    # requirements, encapsulating a request, Command and its subclasses,
    # undoability and Reversible, the command history, Command. Command's
    # implementation notes on undo are from the pattern (p. 258).
    # Quote: PDF p. 80 of the operator's copy, 16 words, quotes.py OK.
    # Lesson total: 16 words.
    {
        "slug": "user-operations",
        "title": "User Operations",
        "module": "Chapter 2 · A Case Study: Designing a Document Editor",
        "one_line": "Each request a menu or button makes turned into an object that can be stored, executed, undone and redone.",
        "summary": (
            "Section 2.7 gives every menu item and button one way to reach Lexi's "
            "scattered operations, and undo and redo without a fixed limit, by making "
            "each request a command object kept in a history. Read the argument, then "
            "run a garden irrigation controller's commands, undos and redos, and read "
            "the two stacks and the state after each step."
        ),
        "key": [
            "a request becomes an object",
            "invoker and operation are decoupled",
            "execute stores what unexecute needs",
            "a history with a present line",
            "undo left, redo right",
            "a new command discards the redos",
        ],
        "key_label": "User operations in six lines",
        "concepts_intro": (
            "The section's two mechanisms, and the pattern that holds them."
        ),
        "concepts": [
            ("Command object",
             "An object that stands for one request, with an operation to carry it out. "
             "A menu item or button holds one and calls it when chosen, without knowing "
             "what the request does or which objects do the work."),
            ("Command history",
             "The list of commands executed so far, with a marker for the present. Undo "
             "reverses the command just before the marker and moves the marker back one place; redo "
             "re-executes the one just after and moves it forward; the length of the "
             "list is the only limit."),
            ("Command",
             "The pattern: a Command interface with an execute operation, "
             "ConcreteCommands that bind a Receiver to an action, an Invoker that "
             "stores and triggers them, and a Client that creates them. It has a lesson "
             "of its own, Command, in Behavioral Patterns I."),
        ],
        "read_title": "Requests as objects, and a history of them",
        "read_intro": (
            "Read Section 2.7, User Operations, in your own copy first. The lesson "
            "follows its argument, then steps a small controller's commands through "
            "undo and redo."
        ),
        "body": [
            # PDF p. 80 of the operator's copy
            ("p", "&ldquo;Here we have another example of encapsulating the concept that "
                  "varies, in this case a request.&rdquo; Section 2.7, User Operations, "
                  "applies the chapter's refrain to what users ask Lexi to do. Read the "
                  "section in your own copy first."),
            ("p", "Some of Lexi's work happens directly in the page, typing and selecting; "
                  "the rest is reached through menus, buttons and keyboard shortcuts: "
                  "new, open, save and print, cut and paste, fonts and alignment, quit. "
                  "The authors set four requirements. One operation may have several "
                  "interfaces, a menu entry and a page button for the same jump, and the "
                  "interfaces may change. The operations live in many classes, and the "
                  "interface classes should not come to depend on all of them. Most "
                  "operations that change the document should be undoable and redoable, "
                  "but not saving or quitting, which should not touch the undo history at "
                  "all. And there should be no fixed limit on the levels of undo."),
            ("p", "The first idea is a subclass of the menu-item class for each operation. "
                  "The authors reject it: it ties the request to one kind of widget, so a "
                  "page button for the same request needs its own subclass, and the "
                  "classes approach the number of widget kinds times the number of "
                  "requests. A function pointer is closer, but it does nothing for undo, "
                  "has nowhere to keep state such as which font to apply, and is hard to "
                  "extend or reuse. An object does all three. So each request becomes a "
                  "command, an instance of a subclass of an abstract Command class whose "
                  "one operation is Execute. A subclass may do the work itself or hand it "
                  "to other objects; the menu item neither knows nor cares, and calls "
                  "Execute when it is chosen."),
            ("p", "Undo adds a second operation, Unexecute, which reverses Execute using "
                  "whatever Execute saved, as a font change saves the range and its "
                  "former fonts. A third, Reversible, lets a command report at run time "
                  "that it changed nothing, so that a font change to the font already "
                  "there does not cost the user an undo. The history is the list of "
                  "executed commands with a line marking the present. To undo, call "
                  "Unexecute on the command left of the line and move the line left; to "
                  "redo, call Execute on the command to its right and move the line "
                  "right. The authors call this Command, which describes how to "
                  "encapsulate a request; its catalog entry adds that undo state can "
                  "include the receiver, the arguments and the receiver's values before "
                  "the change. It also warns that a command whose state changes when it "
                  "runs must be copied before it goes on the history, and that errors "
                  "can pile up over many undos and redos."),
            ("code", _lines(ZONE_COMMAND_JAVA)),
            ("code", _lines(HISTORY_JAVA)),
            ("p", "The second sketch keeps the present line as two stacks: the commands "
                  "left of it on one, those right of it on the other. Running a new "
                  "command clears the redo stack, as a new edit in an editor ends any "
                  "chance of redoing what was undone. The lab steps through the same "
                  "model on a garden irrigation controller with two zones, front at 20 "
                  "minutes and back at 30, and four commands: boost adds 10 to front, "
                  "trim takes 5 from back, rain sets front to 0, summer sets back to 45. "
                  "On the preset <code>garden-week</code> the script is boost, trim, "
                  "rain, undo, undo, redo, summer, undo. The table gives the state and "
                  "both stacks after each step. At step 7 summer runs while rain still "
                  "waits to be redone, so rain is discarded: 1 redo entry lost. The run "
                  "ends with front 30, back 25, boost and trim on the undo stack and "
                  "summer alone on the redo stack, and nothing refused."),
            ("p", "The last tile counts what the history must hold. Kept as inverse "
                  "commands, a set command stores the one value it overwrote and an add "
                  "stores nothing, since it is undone by subtracting: 1 value at the end, "
                  "for summer. Kept as snapshots of the whole state, each of the 3 "
                  "commands on the stacks holds both zones: 6. The preset "
                  "<code>garden-snapshots</code> runs the same script under snapshots, "
                  "and the states do not change, only the count, 6 against 1. The "
                  "preset <code>nothing-to-undo</code> runs boost, then two undos and "
                  "three redos: one undo and two redos find their stack empty, and the "
                  "lab counts them, undo 1, redo 2, leaving front at 30 with boost on the "
                  "undo stack. The snapshot alternative is the "
                  "subject of Memento, in Behavioral Patterns I."),
            ("h3", "Exercise"),
            ("code", _lines(GARDEN_EXERCISE)),
            ("p", "The same controller, another script. By hand, write the state and both "
                  "stacks after each of the six steps, and count the redo entries "
                  "discarded and the requests refused. Then type the script into the lab "
                  "to check."),
            ("p", "Every design problem so far has been about the document or what is "
                  "done to it as a whole. The next lesson, Spelling Checking and "
                  "Hyphenation, reads the last design problem, operations that must "
                  "visit every part, and the chapter's summary."),
        ],
        "lab": ("gofkit", {
            "mode": "history",
            "view": "undo",
            "preset": "garden-week",
            "state": GARDEN_STATE,
            "commands": GARDEN_COMMANDS,
            "presets": [
                {"id": "garden-week",
                 "label": "An irrigation controller: three commands, undo, redo, a fourth",
                 "script": GARDEN_SCRIPT,
                 "scheme": "inverse",
                 "expect": {"ghiFinal": "front 30, back 25",
                   "ghiUndo": "2: boost, trim",
                   "ghiRedo": "1: summer",
                   "ghiRefused": "undo 0, redo 0",
                   "ghiDiscarded": "1",
                   "ghiStored": "1",
                   "ghiOther": "snapshot: 6"}},
                {"id": "garden-snapshots",
                 "label": "The same script, the history kept as snapshots",
                 "script": GARDEN_SCRIPT,
                 "scheme": "snapshot",
                 "expect": {"ghiFinal": "front 30, back 25",
                   "ghiUndo": "2: boost, trim",
                   "ghiRedo": "1: summer",
                   "ghiRefused": "undo 0, redo 0",
                   "ghiDiscarded": "1",
                   "ghiStored": "6",
                   "ghiOther": "inverse: 1"}},
                {"id": "nothing-to-undo",
                 "label": "One command, then more undos and redos than there are",
                 "script": GARDEN_REFUSALS,
                 "scheme": "inverse",
                 "expect": {"ghiFinal": "front 30, back 30",
                   "ghiUndo": "1: boost",
                   "ghiRedo": "0: none",
                   "ghiRefused": "undo 1, redo 2",
                   "ghiDiscarded": "0",
                   "ghiStored": "0",
                   "ghiOther": "snapshot: 2"}},
            ],
            "panel_title": "Commands, undo and redo on a small state",
        }),
        "steps_title": "Stepping a command history",
        "steps_intro": "Four steps, the last of them on an application of your own.",
        "steps": [
            ("Start from the state and two empty stacks",
             "Write each cell's value, an empty undo stack and an empty redo stack."),
            ("Run, undo and redo in order",
             "A command executes and goes on the undo stack, clearing the redo stack. "
             "Undo pops the top of the undo stack, reverses it and pushes it on the redo "
             "stack; redo does the opposite. An empty stack refuses."),
            ("Count what the history keeps",
             "As inverse commands, each set holds the value it replaced and each add "
             "holds nothing; as snapshots, each command on either stack holds every "
             "cell."),
            ("Do it on an application of your own",
             "Take an application you use with an undo menu and write four of its "
             "operations as commands on a small state. Run a script with an undo after a "
             "new command, and say which of the application's operations, like save, "
             "should never enter the history."),
        ],
        "worked": {
            "title": "Eight steps on an irrigation controller",
            "intro": [
                "Step the preset <code>garden-week</code>.",
            ],
            "lines": [
                "boost: front 30; undo [boost]",
                "trim: back 25; undo [boost, trim]",
                "rain: front 0; undo [boost, trim, rain]",
                "undo rain: front 30; redo [rain]",
                "undo trim: back 30; redo [rain, trim]",
                "redo trim: back 25; redo [rain]",
                "summer: back 45; rain discarded",
                "undo summer: back 25; redo [summer]",
            ],
            "after": [
                "Each undo reverses only the command on top, using what it stored when it "
                "ran: rain gives front back its 30 and summer gives back its 25. The redo "
                "stack lasts only until the next new command.",
            ],
        },
        "quiz_title": "Commands, histories and what they keep",
        "quiz": [
            {"q": "In the exercise, after the six steps, what is the state, and what is "
                  "on each stack?",
             "a": ["front 0, back 30; undo [rain]; redo [trim]",
                   "front 10, back 25; undo [rain, boost, trim]; redo empty",
                   "front 0, back 30; undo [rain]; redo [trim, boost]",
                   "front 20, back 30; undo empty; redo [trim, rain]"],
             "c": 0,
             "why": "rain sets front to 0; boost makes it 10; undo reverses boost, front 0, "
                    "redo [boost]; trim makes back 25 and discards boost from the redo "
                    "stack; redo finds the stack empty and is refused; undo reverses trim, "
                    "back 30, redo [trim]. One redo entry is discarded and one request "
                    "refused. Keeping boost on the redo stack forgets that trim discarded "
                    "it; the second answer ignores the undos, and the fourth undoes rain "
                    "as well, which only a third undo would do."},
            {"q": "Why does Section 2.7 reject giving the menu-item class a subclass for "
                  "each operation?",
             "a": ["Menu items cannot hold state",
                   "It ties each request to one kind of widget, so classes approach widget "
                   "kinds times requests",
                   "Subclasses cannot be undone",
                   "C++ does not allow subclasses of glyphs"],
             "c": 1,
             "why": "A request bound to a menu item by inheritance must be bound again to "
                    "a page button and every other widget that issues it, so the classes "
                    "grow toward the product of widget kinds and requests, and the request "
                    "is coupled to one interface. A menu item is a glyph and can hold "
                    "state; undo comes from the Command it holds, which gains Unexecute; "
                    "and MenuItem is itself a subclass of Glyph."},
            {"q": "On the preset <code>garden-week</code>, how many values does the history "
                  "hold at the end as inverse commands, and as snapshots?",
             "a": ["1 and 6", "3 and 6", "1 and 2", "2 and 4"],
             "c": 0,
             "why": "Three commands are on the stacks at the end: boost and trim on the "
                    "undo stack, summer on the redo stack. As inverse commands only the "
                    "set, summer, stores a value (adds are undone by subtracting): 1. As "
                    "snapshots each of the 3 holds both zones: 3 × 2 = 6. Three counts "
                    "commands, not values; 2 is one snapshot; 4 counts only the undo "
                    "stack's two snapshots."},
            {"q": "What is the Reversible operation in Lexi's Command interface for?",
             "a": ["To decide at run time whether a command changed anything, so a "
                   "spurious one need not be undone",
                   "To reverse the order of the command history",
                   "To redo the most recently undone command",
                   "To mark commands such as save that may be undone only once"],
             "c": 0,
             "why": "A font change to the font already there does nothing, and the "
                    "authors do not want the user to undo it; Reversible lets the command "
                    "report that at run time. Redo is Execute on the command right of the "
                    "present line, and save and quit stay out of the history entirely."},
        ],
        "mistakes": [
            ("Binding each operation to the widget that triggers it",
             "Section 2.7 rejects a menu-item subclass per operation: the request is "
             "coupled to one interface, and the classes approach widget kinds times "
             "requests. A command object is handed to any number of widgets, and each "
             "calls the same Execute."),
            ("Thinking any operation can enter the undo history",
             "The authors exclude saving and quitting, which should leave the history "
             "untouched, and add Reversible so that a command that changed nothing does "
             "not cost an undo. Which operations belong in the history is a decision "
             "about the application, not something the pattern settles."),
            ("Expecting redo to survive a new command",
             "Commands right of the present line are only candidates for redo; running a "
             "new command replaces them. On the lesson's controller the lab counts rain "
             "discarded at step 7, and the exercise loses boost the same way."),
        ],
        "standard": (
            "Finish when you can step a script of commands, undos and redos by hand.",
            "Given a small state, its commands and a script, state the state and both "
            "stacks after each step, the redo entries discarded and the requests "
            "refused, and what the history keeps as inverse commands and as snapshots."
        ),
        "note": (
            "The lab steps set and add commands on whole numbers. It does not model "
            "Reversible, commands that change nothing, or commands kept out of the "
            "history; which of an application's operations should be undoable is the "
            "designer's call, as the authors make it for Lexi."
        ),
    },
    # ---------------------------------------------------------------- 07
    # 2.8 Spelling Checking and Hyphenation (PDF pp. 84-96 of the operator's
    # copy): accessing scattered information, the traversal operations on
    # Glyph, Iterator, traversal versus traversal actions, encapsulating the
    # analysis, Visitor; 2.9 Summary (pp. 96-97). Visitor's consequences are
    # from the pattern (pp. 355-356).
    # Quote: PDF p. 96 of the operator's copy, 18 words, quotes.py OK.
    # Lesson total: 18 words.
    {
        "slug": "spelling-and-hyphenation",
        "title": "Spelling Checking and Hyphenation",
        "module": "Chapter 2 · A Case Study: Designing a Document Editor",
        "one_line": "Traversal given to iterators and each analysis given to a visitor, so that new analyses need no change to the document's classes.",
        "summary": (
            "Section 2.8 adds analyses such as spelling checking without growing the "
            "document's classes: iterators walk the structure, and a visitor carried "
            "to each part does the analysis. Read the argument and the chapter's "
            "summary, then run two analyses over the recipe book of the first lesson "
            "and count the calls, the methods, and what a new analysis and a new kind "
            "of part each change."
        ),
        "key": [
            "access is one problem, analysis another",
            "an iterator holds its own traversal",
            "separate the walk from the work",
            "accept calls back the right visit",
            "a new analysis: one new class",
            "a new kind of part: every visitor edited",
        ],
        "key_label": "Analysis in six lines",
        "concepts_intro": (
            "Two patterns, and the double call that makes the second work."
        ),
        "concepts": [
            ("Iterator",
             "An object that walks a structure: start, advance, test for the end, give "
             "the current item. Subclasses walk different containers or in different "
             "orders, and each keeps its own place, so several walks can run at once. It "
             "has a lesson of its own, Iterator, in Behavioral Patterns I."),
            ("Double dispatch",
             "The two calls that let an analysis treat each kind of part its own way "
             "without testing types: the traversal calls the part's accept with the "
             "visitor, and the part, which knows its own class, calls the visitor's "
             "method for that class."),
            ("Visitor",
             "The pattern: a Visitor declares one visit operation per ConcreteElement "
             "class, each ConcreteVisitor is one operation over the structure, and each "
             "element's accept calls the matching visit. It has a lesson of its own, "
             "Visitor, in Behavioral Patterns II."),
        ],
        "read_title": "The walk, the work, and the eight patterns",
        "read_intro": (
            "Read Section 2.8, Spelling Checking and Hyphenation, and 2.9, Summary, in "
            "your own copy first. The lesson follows the section's two steps and counts "
            "the second on the recipe book of the first lesson."
        ),
        "body": [
            # PDF p. 96 of the operator's copy
            ("p", "&ldquo;An important question to ask yourself before applying the "
                  "Visitor pattern is, Which class hierarchies change most often?&rdquo; "
                  "Section 2.8, Spelling Checking and Hyphenation, ends on that question, "
                  "and the chapter's summary, 2.9, follows. Read both in your own copy "
                  "first; 2.8 is the longest section in the chapter."),
            ("p", "The last problem is analysis. Like formatting, spelling checking and "
                  "hyphenation each have several algorithms, trading space, time and "
                  "quality; unlike formatting, they are two of many analyses Lexi will "
                  "want, searching, counting words, adding up a table, checking grammar, "
                  "and the authors do not want to change Glyph and all its subclasses for "
                  "each one. They split the problem in two: reaching the information "
                  "scattered through the structure, and doing the analysis."),
            ("p", "Reaching it is harder than it looks. Children may sit in arrays, lists "
                  "or something stranger, and analyses walk in different orders, forward, "
                  "backward for a reverse search, or in order for an expression. The "
                  "glyph's integer child index already favours arrays. A first fix puts "
                  "traversal operations on Glyph, start, next, done and current, with a "
                  "parameter naming the order. It removes the index, but a new order "
                  "means changing that parameter's type or adding operations, the "
                  "mechanism cannot be reused for other structures, and only one "
                  "traversal can be under way at a time. So the authors encapsulate the "
                  "concept that varies once more: an Iterator class hierarchy, with "
                  "subclasses for arrays and lists and for preorder and other walks. "
                  "Each glyph creates an iterator over its own children, a leaf a null "
                  "iterator that is done at once, and a preorder iterator keeps a stack "
                  "of them. The pattern is Iterator."),
            ("p", "Doing the analysis comes next. Putting it in the iterators would tie "
                  "each analysis to one walk, when many analyses share preorder. Putting "
                  "it in the glyph classes, an operation per analysis, means editing every "
                  "glyph class for each new analysis and burying the glyph's real "
                  "interface under analytical operations. So the analysis becomes an "
                  "object that the iterator carries to each glyph. It must still tell a "
                  "letter from a picture, and the authors refuse to do that with type "
                  "tests and casts, the kind of code, they say, object-oriented languages "
                  "were meant to remove. Instead each glyph gets one operation that calls "
                  "back the analyser's method for that glyph's own class. Give every "
                  "analyser the same interface, call it a Visitor and the glyph's "
                  "operation Accept, and a new analysis is a new visitor subclass with no "
                  "glyph class touched. The hyphenation visitor, for instance, inserts "
                  "discretionary glyphs, which show as a hyphen only at the end of a "
                  "line."),
            ("p", "The catalog's Visitor names the price beside the gain. Adding an "
                  "operation is easy and related behaviour is gathered in one class; "
                  "adding a new kind of element is hard, because every visitor gains a "
                  "method for it, and visitors often need elements to expose state "
                  "through public operations, which the catalog counts as a cost to "
                  "encapsulation. The authors' answer for Lexi is that new analyses are "
                  "far likelier than new kinds of glyph. The summary then lists the "
                  "chapter's eight patterns, Composite, Strategy, Decorator, Abstract "
                  "Factory, Bridge, Command, Iterator and Visitor, notes that none of "
                  "these problems belongs to editors alone, from investment portfolios "
                  "built as composites to compilers choosing register allocation as a "
                  "strategy, and sends the reader on to the catalog and to their own "
                  "designs."),
            ("code", _lines(BOOK_VISITOR_JAVA)),
            ("p", "The lab returns to the recipe book of the first lesson, 10 nodes of 3 "
                  "kinds, Section, Photo and Recipe, with two analyses as visitors, a "
                  "timer and a costing. On the preset <code>book-new-analysis</code> "
                  "every node accepts each visitor once: 10 × 2 = 20 accept calls, and "
                  "each accept makes one visit call, 20 more. There are 1 + 3 = 4 "
                  "element classes, counting the abstract element, and 1 + 2 = 3 visitor "
                  "classes. Written as visitors, the analyses take 3 × 2 + 3 = 9 methods, "
                  "a visit method per kind per visitor and an accept per kind; written as "
                  "operations on the elements, 3 × 2 = 6. The preset adds a third "
                  "analysis, a shopping list: with Visitor 1 class is added and none "
                  "changed, against 4 classes changed, the abstract element and every "
                  "element class, when each analysis is an operation of the elements."),
            ("p", "The preset <code>book-new-kind</code> adds a new kind of part instead, a "
                  "wine pairing, and the counts swap. With Visitor the new element class "
                  "is added and 3 classes change, the abstract visitor and both visitors; "
                  "with the operations on the elements, the new class is all, and nothing "
                  "else changes. Neither design is cheaper in general. The count says "
                  "which change each makes cheap, and the authors' question, which "
                  "hierarchy changes more often, decides between them."),
            ("h3", "Exercise"),
            ("code", _lines(MIXTAPE) + ["visitors: duration, artists, playcount"]),
            ("p", "The mixtape of the first lesson's exercise, with three analyses. By "
                  "hand, count the accept calls, the methods written with Visitor and "
                  "without, and the classes a new kind of node changes under each design. "
                  "Then type the records and visitors into the lab, with the addition set "
                  "to a kind."),
            ("p", "That ends the case study and its eight patterns. The next course, "
                  "Creational Patterns, opens the catalog with Abstract Factory, which "
                  "Lexi met in Supporting Multiple Look-and-Feel Standards."),
        ],
        "lab": ("gofkit", {
            "mode": "tree",
            "view": "visit",
            "preset": "book-new-analysis",
            "nodes": _records(RECIPE_BOOK),
            "visitors": "timer costing",
            "presets": [
                {"id": "book-new-analysis",
                 "label": "The recipe book, two analyses, adding a third",
                 "adding": "operation",
                 "expect": {"gtrAccepts": "20: 10 nodes × 2 visitors",
                   "gtrVisits": "20",
                   "gtrElements": "1 + 3 = 4 (the abstract element; Section, Photo, Recipe)",
                   "gtrVisitorClasses": "1 + 2 = 3 (the abstract visitor; timer, costing)",
                   "gtrMethods": "3 × 2 + 3 = 9",
                   "gtrMethodsPlain": "3 × 2 = 6",
                   "gtrAddVisitor": "1 added (the new visitor), 0 changed",
                   "gtrAddPlain": "0 added, 4 changed (the abstract element and 3 element classes)"}},
                {"id": "book-new-kind",
                 "label": "The recipe book, two analyses, adding a kind of part",
                 "adding": "kind",
                 "expect": {"gtrAccepts": "20: 10 nodes × 2 visitors",
                   "gtrVisits": "20",
                   "gtrElements": "1 + 3 = 4 (the abstract element; Section, Photo, Recipe)",
                   "gtrVisitorClasses": "1 + 2 = 3 (the abstract visitor; timer, costing)",
                   "gtrMethods": "3 × 2 + 3 = 9",
                   "gtrMethodsPlain": "3 × 2 = 6",
                   "gtrAddVisitor": "1 added (the new element class), 3 changed (the abstract visitor and 2 visitors)",
                   "gtrAddPlain": "1 added (the new element class), 0 changed"}},
            ],
            "panel_title": "Analyses as visitors, or as operations of the parts",
        }),
        "steps_title": "Counting a visitor over a structure",
        "steps_intro": "Four steps, the last of them on a structure of your own.",
        "steps": [
            ("Count the nodes, the kinds and the visitors",
             "Write N nodes, K kinds of node (each a class) and V visitors (each an "
             "analysis)."),
            ("Count the calls",
             "Each node accepts each visitor once, and each accept calls one visit "
             "method: N × V accept calls and N × V visit calls."),
            ("Count the methods and the changes",
             "With Visitor, K × V visit methods and K accepts; without, K × V "
             "operations on the elements. A new analysis adds a visitor and changes "
             "nothing, or changes the abstract element and all K classes; a new kind "
             "changes the abstract visitor and all V visitors, or nothing."),
            ("Do it on a structure of your own",
             "Take a structure in your own code that several operations walk: a syntax "
             "tree, a document model, an order with its lines. Count its kinds and "
             "operations, and say from its history which has grown more often, the kinds "
             "or the operations."),
        ],
        "worked": {
            "title": "Two analyses of a recipe book",
            "intro": [
                "Count the preset <code>book-new-analysis</code>.",
            ],
            "lines": [
                "accept calls: 10 nodes × 2 visitors = 20",
                "visit calls: 20",
                "with Visitor: 3 × 2 + 3 = 9 methods",
                "on the elements: 3 × 2 = 6 methods",
                "a third analysis, Visitor: 1 added, 0 changed",
                "a third analysis, elements: 4 changed",
            ],
            "after": [
                "Visitor costs three accept methods up front and buys an analysis that "
                "touches no element class. The bill comes due when a new kind of part "
                "arrives, as the other preset shows.",
            ],
        },
        "quiz_title": "Iterators, visitors and the classes they spare",
        "quiz": [
            {"q": "In the exercise, 9 nodes of 2 kinds and 3 visitors: how many accept "
                  "calls, how many methods with Visitor, and how many classes change "
                  "with Visitor when a new kind of node is added?",
             "a": ["27 accept calls, 8 methods, 4 classes changed",
                   "27 accept calls, 6 methods, 3 classes changed",
                   "18 accept calls, 8 methods, 4 classes changed",
                   "27 accept calls, 8 methods, 0 classes changed"],
             "c": 0,
             "why": "Each of the 9 nodes accepts each of the 3 visitors: 27. With Visitor "
                    "there are 2 × 3 = 6 visit methods and 2 accepts, 8. A new kind "
                    "changes the abstract visitor and all 3 visitors, 4. Six is the count "
                    "without Visitor; 3 changes forgets the abstract visitor; 18 multiplies "
                    "the nodes by the kinds instead of the visitors; 0 changes is what the design without Visitor "
                    "pays for a new kind."},
            {"q": "Which problem with putting traversal operations directly on Glyph does "
                  "Section 2.8 name?",
             "a": ["Glyphs could no longer draw themselves",
                   "Only one traversal can be in progress on a structure at a time",
                   "Leaves would need children",
                   "The traversal would always be in preorder"],
             "c": 1,
             "why": "With the traversal state in the glyphs, a new order means changing "
                    "the order parameter or adding operations, the mechanism cannot be "
                    "reused for other structures, and there can be only one traversal "
                    "under way. The parameter allowed several orders; iterators fix the "
                    "rest, each keeping its own state."},
            {"q": "On the preset <code>book-new-kind</code>, a new kind of part is added. "
                  "What does the lab count for each design?",
             "a": ["Visitor: 1 added, 0 changed; operations on the elements: 1 added, 4 "
                   "changed",
                   "Visitor: 1 added, 3 changed; operations on the elements: 1 added, 0 "
                   "changed",
                   "Visitor: 1 added, 2 changed; operations on the elements: 1 added, 0 "
                   "changed",
                   "Visitor: 0 added, 3 changed; operations on the elements: 1 added, 3 "
                   "changed"],
             "c": 1,
             "why": "Either way the new element class is added. With Visitor the abstract "
                    "visitor and the 2 visitors each gain a visit method for it, 3 "
                    "changed; with the analyses as operations on the elements, the new "
                    "class carries its own and nothing else changes. The first answer "
                    "swaps the designs; 2 changed forgets the abstract visitor."},
            {"q": "Why do the authors judge Visitor a good fit for Lexi?",
             "a": ["Visitors make new kinds of glyph easy to add",
                   "New kinds of analysis are much likelier than new kinds of glyph",
                   "Visitors remove the need for iterators",
                   "Visitors let each glyph check its own spelling"],
             "c": 1,
             "why": "Visitor makes new operations cheap and new element classes costly, "
                    "and the authors expect Lexi to gain analyses more often than glyph "
                    "classes. The iterator still walks the structure and carries the "
                    "visitor, and taking the analyses out of the glyph classes is the "
                    "point."},
        ],
        "mistakes": [
            ("Adding an operation to every element class for each new analysis",
             "Section 2.8 names two costs: every glyph class is edited for each analysis, "
             "and the glyph's interface fills with analytical operations until its real "
             "purpose is hard to see. On the lesson's recipe book the lab counts 4 "
             "classes changed for a third analysis, against 1 new visitor and nothing "
             "changed."),
            ("Telling kinds apart with type tests in the analysis",
             "The authors reject a checker that asks each glyph whether it is a "
             "character, a row or an image: it is hard to extend and must be edited "
             "whenever the hierarchy changes. Accept and visit let each element name "
             "its own class instead, at the cost of one accept method per kind."),
            ("Adopting Visitor without asking which hierarchy changes",
             "The catalog is explicit that new element classes are hard under Visitor: "
             "every visitor gains a method. On the lab's recipe book a new kind changes "
             "3 classes with Visitor and none without. The authors chose it for Lexi "
             "because analyses were the likelier change."),
        ],
        "standard": (
            "Finish when you can count a visitor's calls and the changes it makes cheap.",
            "Given a structure's nodes and kinds and a set of analyses, state the accept "
            "and visit calls, the methods with and without Visitor, and what a new "
            "analysis and a new kind each change, and say what Iterator contributes."
        ),
        "note": (
            "The lab counts calls, classes and methods on the structure as stated. It "
            "cannot tell you which of your hierarchies will change more often, which is "
            "the question the authors put first, and it does not count the traversal "
            "orders, which Iterator's own lesson does."
        ),
    },
]
