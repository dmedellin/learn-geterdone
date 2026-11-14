"""Persons and the Generation of a Commonwealth, lessons 1-3 -- Chapters 16 and 17.

Every quotation is copied from the operator's copy of the 1651 text (Tuck's
Cambridge edition) and checked against the page image; the comment beside each
lesson gives the chapter, the 1651 page where the margin shows it, and the PDF
page. Hobbes's spelling, capitals and punctuation stand inside quotation marks;
the lesson's own prose is modern.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Leviathan ch. 16, 1651 p. 81; PDF p. 208 of the operator's copy
    # (opening sentence block and the covenant by authority); PDF p. 209 (the
    # limits of authority).
    {
        "slug": "persons-authors-and-actors",
        "title": "Persons, Authors and Actors",
        "module": "Chapter 16 · Of Persons, Authors, and things Personated",
        "one_line": "A person is anyone whose words or actions are owned, and a covenant made by an actor within his authority binds the author as if the author had made it.",
        "summary": (
            "Chapter 16 gives the commonwealth its machinery before Chapter 17 uses it: a "
            "person is a mask, an actor wears it, an author owns what the actor does, and "
            "authority is the right to do the act. Check the argument that an author is bound "
            "by what his actor covenants as a set of premises about a stated case, and see "
            "what happens to the conclusion when the authority is missing or the covenant "
            "goes beyond it."
        ),
        "key": [
            "a person: words or actions, owned or lent",
            "actor acts; author owns the act",
            "authority: the right of doing the act",
            "inside the commission, the author is bound",
            "beyond it, only the actor is bound",
        ],
        "key_label": "The chapter's apparatus in five lines",
        "concepts_intro": (
            "Chapter 16 sits on the hinge between Part I and Part II. Nothing in it is about "
            "kings, yet the commonwealth of the next chapter is defined with its three words."
        ),
        "concepts": [
            ("A person is a role",
             "Hobbes takes the word from the theatre. A person is someone whose words or "
             "actions are considered either as his own, a natural person, or as representing "
             "the words or actions of another, a feigned or artificial person. A man can bear "
             "his own person or someone else's, and several at once."),
            ("Actor and author",
             "Where an artificial person's words and actions are owned by the one he "
             "represents, he is the actor and the owner is the author. The word comes from "
             "property: as the owner of goods is their master, the author is the owner of "
             "the action."),
            ("Authority, and its commission",
             "Authority is the right of doing an act, and an act done by authority is done "
             "by commission or licence from the one whose right it is. A covenant made by "
             "the actor binds the author, but only as far as the commission goes."),
        ],
        "read_title": "The passage first, then the chapter's first half in order",
        "read_intro": (
            "The sentences that define actor, author and authority come first. The "
            "paragraphs after them say what the definitions allow, and where they stop."
        ),
        "body": [
            ("p", "<strong>Chapter 16.</strong> &ldquo;Of Persons Artificiall, some have "
                  "their words and actions Owned by those whom they represent. And then the "
                  "Person is the Actor; and he that owneth his words and actions, is the "
                  "AUTHOR: In which case the Actor acteth by Authority.&rdquo;"),
            ("p", "Think of the last time someone signed for you: a parcel, a lease, a form "
                  "at the doctor's. Whoever signed was acting, and you were the one whose "
                  "name the signature carried. Hobbes builds a political theory out of that "
                  "ordinary arrangement, and he starts, as he often does, with the word. "
                  "&ldquo;Person&rdquo; is Latin, he says, and in Latin <em>persona</em> was "
                  "&ldquo;the disguise, or outward appearance of a man, counterfeited on the "
                  "Stage&rdquo;, and more particularly the mask. From the stage the word "
                  "travelled into the law courts, so that &ldquo;a Person, is the same that "
                  "an Actor is, both on the Stage and in common Conversation&rdquo;."),
            ("p", "His definition comes first, and it is wide: a person is &ldquo;he, whose "
                  "words or actions are considered, either as his own, or as representing "
                  "the words or actions of an other man&rdquo;, or of any other thing, whether "
                  "truly or by fiction. When they are considered as his own, he is a natural "
                  "person; when they stand for another's, he is feigned or artificial. "
                  "Nothing in the definition requires a human being to be the one represented, "
                  "which is why a bridge can have a person, as you will see."),
            ("p", "The actor is the one who acts. The author is the one who owns the act. "
                  "Hobbes borrows the word from property: what in goods is called the "
                  "owner, in Latin <em>dominus</em>, is in actions called an author, and "
                  "&ldquo;the Right of doing any Action, is called AUTHORITY&rdquo;. So to "
                  "act by authority is to act with the commission or licence of the one "
                  "whose right it is."),
            ("p", "Now the consequence that makes the machinery worth having: &ldquo;when "
                  "the Actor maketh a Covenant by Authority, he bindeth thereby the Author, "
                  "no lesse than if he had made it himselfe; and no lesse subjecteth him to "
                  "all the consequences of the same.&rdquo; Everything Hobbes said about "
                  "covenants in Chapter 14 holds, he adds, when they are made by "
                  "representatives, &ldquo;so far-forth as is in their Commission, but no "
                  "farther&rdquo;. A letting agent who signs a lease for the owner makes the "
                  "owner a landlord. An agent who signs away the owner's house, with no "
                  "authority to sell it, has bound nobody but himself."),
            ("p", "That limit works in two directions, and Hobbes spells both. A man who "
                  "covenants with an actor and does not know his authority acts &ldquo;at "
                  "his own perill&rdquo;, because &ldquo;no man is obliged by a Covenant, "
                  "whereof he is not Author&rdquo;. If he asks to see the authority and it "
                  "is not shown, he is no longer bound. But if he knew beforehand that he "
                  "would have nothing but the actor's word, then the actor has made himself "
                  "the author, and the covenant stands against the actor. Hobbes sums it up: "
                  "when the authority is evident the covenant obliges the author, not the "
                  "actor, and when the authority is feigned it obliges the actor only."),
            ("p", "The lab turns this into three small arguments. Let `p` be <em>the "
                  "actor had authority</em>, `q` be <em>the covenant was within his "
                  "commission</em> and `r` be <em>the author is bound</em>. The first "
                  "premise in every argument is Hobbes's rule, <em>if authority and "
                  "within commission, then bound</em>. In the preset <em>full</em> the "
                  "other premises are `p` and `q`, and the conclusion `r` follows: the lab "
                  "finds no row in which the premises are true and the conclusion false. In "
                  "<em>no-authority</em> the actor had none, `p` is false, and the lab finds "
                  "exactly one such row, the case in which `q` is true and `r` false: the "
                  "rule alone cannot make the author bound, because there was no "
                  "commission. In <em>beyond-commission</em> "
                  "the authority was real and the covenant went past it, so `q` is false, and "
                  "again there is exactly one row in which the conclusion fails. These two "
                  "presets show only that the rule cannot make him bound. That he is "
                  "<em>not</em> bound needs Hobbes's other sentence, that no man is "
                  "obliged by a covenant of which he is not author, written `r -> p & q`. "
                  "In the preset <em>not-author</em> that sentence and `~p` give `~r`, and "
                  "the lab finds the argument valid."),
            ("p", "Hobbes carries the point one step further, and it is worth noticing why. "
                  "If the actor does something against the law of nature on the author's "
                  "command, and the actor was already obliged by covenant to obey him, "
                  "&ldquo;not he, "
                  "but the Author breaketh the Law of Nature&rdquo;: the act is the author's, "
                  "and refusing it would break the covenant that forbids breach. The same "
                  "idea reaches the other end. Things that cannot own an act, such as a "
                  "church, a hospital or a bridge, may be personated by a master or "
                  "overseer, but &ldquo;things Inanimate, cannot be Authors&rdquo;, and so "
                  "the authority comes from their owners or governors. Children and the "
                  "mad can be represented by guardians, but are authors of the guardian's acts only when, "
                  "recovering reason, &ldquo;they shall judge the same reasonable&rdquo;. All of that, he adds, has no place before "
                  "there is a civil state, &ldquo;because before such estate, there is no "
                  "Dominion of Persons&rdquo;."),
            ("p", "You may wonder what this has to do with a commonwealth. The answer is in "
                  "the second half of the chapter, where Hobbes asks how a multitude can "
                  "be one person, and in Chapter 19, where he complains that in England "
                  "the men who carried petitions to a king of six hundred years' descent "
                  "were called the people's representatives, and the king, who had the "
                  "sovereignty, was not. Hobbes wrote with a civil war in front of him in "
                  "which the question of who spoke for the people was not an academic one. "
                  "Read Chapter 16 as the chapter that decides what it would take to "
                  "answer it."),
            ("p", "One boundary on what the lab does. It checks that the conclusion "
                  "follows from the premises about a stated case; whether the agent had "
                  "authority is a fact about the case, and no lab can tell you whether a "
                  "real signature was authorised. The next lesson, &ldquo;A Multitude Made "
                  "One Person&rdquo;, takes the second half of Chapter 16: what happens when "
                  "the author is not one man but a crowd."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "show": "all",
            "preset": "full",
            "presets": [
                {"id": "full", "label": "Authority and within the commission",
                 "premises": ["p & q -> r", "p", "q"], "conclusion": "r",
                 "expect": {"vaVerdict": "Valid", "vaCounter": "0"}},
                {"id": "no-authority", "label": "The actor had no authority",
                 "premises": ["p & q -> r", "~p", "q"], "conclusion": "r",
                 "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
                {"id": "beyond-commission", "label": "Authority, but the covenant goes beyond it",
                 "premises": ["p & q -> r", "p", "~q"], "conclusion": "r",
                 "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
                {"id": "not-author", "label": "Hobbes's converse: no man is bound who is not author",
                 "premises": ["r -> p & q", "~p"], "conclusion": "~r",
                 "expect": {"vaVerdict": "Valid", "vaCounter": "0"}},
            ],
            "panel_title": "Is the author bound?",
            "panel_intro": (
                "Premise one is Hobbes's rule, written `p & q -> r` (the box shows the "
                "arrow and the wedge, and accepts either spelling). The other premises "
                "state the case, and in the last preset the rule is turned round. "
                "Choose each preset and find the row, if there is one, in which every premise "
                "is true and the conclusion false."
            ),
        }),
        "steps_title": "Deciding who is bound by a covenant an actor made",
        "steps_intro": "Four questions, in this order.",
        "steps": [
            ("Name the actor and the author",
             "The actor is the one who made the covenant. The author is the one whose "
             "right it was to make it. If the actor made it on his own account, he is both."),
            ("Find the commission",
             "Look for the authority: the words or writing by which the author gave the "
             "actor the right. A commission may be stated without limit, or with a limit "
             "on what and how far."),
            ("Compare the covenant with the commission",
             "Ask whether the covenant lies inside what the commission covers. Inside, "
             "the author owns it. Outside, it is not his, and he is not obliged by it."),
            ("Say who is bound, and who took the risk",
             "If the authority was shown, or evident, the author is bound and the actor is "
             "not. If it was feigned, only the actor is bound. If the other party knew "
             "beforehand that he had only the actor's word, the actor made himself the "
             "author."),
        ],
        "worked": {
            "title": "An agent, a lease and a flat",
            "intro": [
                "Ines owns a flat and tells her agent Omar he may let it for a year. Omar "
                "signs a lease with Tobias. Then he signs a second paper selling Tobias the "
                "flat. This is an example written for the lesson, and the question is who is "
                "bound by each paper.",
            ],
            "lines": [
                "actor: Omar.  author: Ines.  commission: let for a year",
                "lease: inside the commission, so Ines is bound",
                "sale: outside it, so Ines is not bound",
                "Tobias knew only Omar's word on the sale",
                "so, on Hobbes's rule, the sale binds Omar alone",
            ],
            "after": [
                "The lease is the preset <em>full</em>: authority, within the commission, "
                "and the author bound. The sale is <em>beyond-commission</em>: real "
                "authority, a covenant that goes past it, and nothing to bind Ines. If Tobias "
                "had asked to see Ines's authority for the sale and been refused, he would no "
                "longer have been obliged at all.",
            ],
        },
        "quiz_title": "Who owns the act",
        "quiz": [
            {"q": "An actor makes a covenant with a buyer, the authority is evident, and the "
                  "covenant is inside the commission. On Hobbes's account, who is obliged?",
             "a": ["The author, and not the actor",
                   "The actor, and not the author",
                   "Both the actor and the author, equally",
                   "Neither, until the buyer has paid"],
             "c": 0,
             "why": "Hobbes: &ldquo;when the Authority is evident, the Covenant obligeth "
                    "the Author, not the Actor&rdquo;. The actor is the one who acts, and "
                    "the author owns what he does. Nothing in the chapter makes the "
                    "obligation wait for payment."},
            {"q": "In the lab, why does `p` and `q` and the rule together give `r`, while "
                  "`p` and the rule alone do not?",
             "a": ["The rule needs `q` as well: authority is not enough if the covenant "
                   "goes beyond the commission",
                   "Authority matters only when the actor is a natural person",
                   "Because `p` and `q` always have the same truth value",
                   "Because a rule with two conditions can never be used"],
             "c": 0,
             "why": "The rule is `p & q -> r`: both conditions must hold. With `p` alone "
                    "the lab finds a row with `q` false and `r` false, in which the covenant "
                    "went beyond the commission. The other options claim something the "
                    "table does not show."},
            {"q": "A man covenants with someone who says he acts for another. He did not "
                  "know beforehand that the actor's word would be all he got, and on "
                  "demand no authority is shown. What follows on the chapter?",
             "a": ["He is bound to the actor personally",
                   "He is bound to the supposed author all the same",
                   "He is no longer obliged, since such a covenant is not valid without "
                   "the author's counter-assurance",
                   "He is bound to both, jointly"],
             "c": 2,
             "why": "Hobbes: if the authority &ldquo;be not made manifest unto him upon "
                    "demand, is no longer obliged&rdquo;. He would be bound to the actor "
                    "only had he known beforehand that he was to expect &ldquo;no other "
                    "assurance, than the Actors word&rdquo;, which the question rules out."},
            {"q": "Which of these, on Hobbes's chapter, can be personated by an overseer but "
                  "cannot be an author?",
             "a": ["A merchant who sends a factor abroad",
                   "A landlord who hires an agent",
                   "A bridge",
                   "A shipowner who appoints a master"],
             "c": 2,
             "why": "&ldquo;things Inanimate, cannot be Authors&rdquo;, though an overseer may "
                    "be given authority by those who own or govern them. The other three "
                    "are natural persons who can own what their agents do."},
        ],
        "mistakes": [
            ("Thinking that only the one who signed is bound",
             "The actor signs, and the author is bound. In the lease preset Ines is bound by "
             "what Omar signed, &ldquo;no lesse than if he had made it himselfe&rdquo;. "
             "The question the chapter asks is whose right the act was, not whose hand made "
             "it."),
            ("Thinking that authority has no edge",
             "An actor can bind his author only &ldquo;so far-forth as is in their "
             "Commission, but no farther&rdquo;. In the beyond-commission preset the lab finds "
             "a row in which the authority is real, the covenant is made, and the rule "
             "alone does not bind the author. A man who deals with an actor without checking is "
             "at his own risk."),
            ("Taking &ldquo;person&rdquo; to mean a human being",
             "For Hobbes a person is a role: the one whose words or actions are considered "
             "as his own or as another's. A man may bear his own person, another's, or "
             "several, and a thing that is not a man may be personated, though it cannot "
             "own an act."),
        ],
        "standard": (
            "Finish when you can say who is bound by a covenant made through an agent.",
            "Given a case with an actor, a commission and a covenant, say who is the author, "
            "whether the covenant lies inside the commission, who is bound, and which "
            "premise of the argument the case denies."
        ),
        "note": (
            "The lab checks an argument you set out; it cannot tell you whether the "
            "agent in a real case had authority, or whether the other party knew. Hobbes "
            "also treats authority as a right given freely by the author, and the "
            "next chapters show how much he lets that idea carry. Whether it can carry the "
            "weight of a commonwealth is what the rest of Part II argues, and the lab "
            "does not decide it."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Leviathan ch. 16, 1651 p. 83; PDF p. 210 (the multitude made one person,
    # the voice of the greater number, the even number); PDF p. 211 (equal
    # voices in a trial and in a deliberation, the negative voice).
    {
        "slug": "one-person-by-consent",
        "title": "A Multitude Made One Person",
        "module": "Chapter 16 · Of Persons, Authors, and things Personated",
        "one_line": "A crowd becomes one person when one representer is authorised by each, and an assembly that represents it speaks by the greater number or, when the voices are equal, not at all.",
        "summary": (
            "Hobbes's multitude is many; it becomes one only in its representer. When the "
            "representer is itself an assembly, its voice is the voice of the greater "
            "number, and an even assembly can be mute. Compute what a set of voices decides, "
            "and work out by hand how often an assembly of each size splits evenly if each "
            "member is as likely to say yes as no, on a model that is not Hobbes's."
        ),
        "key": [
            "one person: the unity of the representer",
            "each is author of what he says or does",
            "the voice of the greater number is the voice",
            "equal voices: mute, with two exceptions",
            "split chance = C(n, n/2) / 2^n",
        ],
        "key_label": "A multitude, one voice",
        "concepts_intro": (
            "The second half of Chapter 16 answers a question Chapter 17 will need: how can "
            "many people be a single party to a covenant?"
        ),
        "concepts": [
            ("Unity is in the representer",
             "A multitude is naturally many. It is made one person when it is represented by "
             "one man or one person, with the consent of every one of it in particular. "
             "&ldquo;it is the Unity of the Representer, not the Unity of the Represented, "
             "that maketh the Person One.&rdquo;"),
            ("Many authors, one actor",
             "Every member gives the representer authority from himself, and owns what he "
             "does in the multitude's name, without limit if the authority was given without "
             "limit. If the authority was limited, each owns only what he gave."),
            ("An assembly speaks by the greater number",
             "When the representer is made of many men, the voice of the greater number "
             "counts as the voice of all. If the voices are equal, an even assembly is mute, "
             "except where equality itself settles the question."),
        ],
        "read_title": "The passage first, then the assembly's voices",
        "read_intro": (
            "The passage that makes a crowd one person comes first. The rules for "
            "counting an assembly's voices follow in the next three paragraphs of "
            "the chapter."
        ),
        "body": [
            ("p", "<strong>Chapter 16.</strong> &ldquo;A Multitude of men, are made One "
                  "Person, when they are by one man, or one Person, Represented; so that it "
                  "be done with the consent of every one of that Multitude in particular. For "
                  "it is the Unity of the Representer, not the Unity of the Represented, that "
                  "maketh the Person One.&rdquo;"),
            ("p", "Picture a crowd at a station platform. Ask what the crowd intends and "
                  "you have asked a question with no answer: each person has an errand, and "
                  "<em>the crowd</em> has none. Hobbes says the same of a multitude. "
                  "Because &ldquo;the Multitude naturally is not One, but Many&rdquo;, it "
                  "cannot be understood as one, and &ldquo;Unity, cannot otherwise be "
                  "understood in Multitude&rdquo; than through someone who bears its "
                  "person. Put a representer in front of the crowd, with each member's "
                  "consent, and there is now one person who can speak, covenant and be "
                  "held to account."),
            ("p", "Each member then stands to that representer as an author does to an "
                  "actor. Every man gives the common representer authority from himself in "
                  "particular, and owns what he does, &ldquo;in case they give him Authority "
                  "without stint&rdquo;. If they limit him, then &ldquo;none of them owneth "
                  "more, than they gave him commission to Act&rdquo;. That is Chapter 16's "
                  "first half applied to a crowd, and the rest of this half of the chapter is about "
                  "the case where the representer is not one man but a body of them."),
            ("p", "Then the voices must be counted, and Hobbes's first rule is simple. "
                  "&ldquo;if the Representative consist of many men, the voyce of the greater "
                  "number, must be considered as the voyce of them all.&rdquo; His reason "
                  "is an argument about what is left over. If the lesser number says yes "
                  "and the greater says no, &ldquo;there will be Negatives more than enough "
                  "to destroy the Affirmatives&rdquo;, and the excess of negatives, "
                  "uncontradicted, is the only voice the assembly has."),
            ("p", "The second rule is about what the first leaves out. A representative "
                  "of even number, he says, especially when the number is not great, is "
                  "&ldquo;oftentimes mute, and uncapable of Action&rdquo;, because the "
                  "contradictory voices are often equal. There are two cases in which "
                  "equality itself decides. In a trial, &ldquo;equality of votes, even in that "
                  "they condemne not, do absolve&rdquo;, because not to condemn is to "
                  "absolve, though the reverse is not true. And in a deliberation whether "
                  "to execute now or later, the equal voices not to decree execution are "
                  "&ldquo;a decree of Dilation&rdquo;, which means delay."),
            ("p", "The third rule is the odd one. If the number is odd, three or more, and "
                  "every member has &ldquo;a Negative Voice&rdquo;, the power to take away "
                  "the effect of all the affirmative voices of the rest, then the body is "
                  "&ldquo;no Representative&rdquo;, because by the diversity of opinions it "
                  "&ldquo;becomes oftentimes, and in cases of the greatest consequence, a "
                  "mute Person&rdquo;. On a stated model, you can say how mute. Take three "
                  "members each with a veto, each as likely to say yes as no, independently. "
                  "A motion passes only if all three say yes, which happens one time in "
                  "eight, against four in eight under the greater number. The model is "
                  "this lesson's; Hobbes gives no figure."),
            ("p", "The lab works the voices. Each "
                  "member says yes, no or abstain, and the lab reports the decision under the "
                  "greater-number rule or under a rule that needs more than half of all the "
                  "members. The preset <em>six-even</em> has three yes and three no, and "
                  "the lab calls the assembly mute. The preset <em>seven</em> adds a seventh "
                  "member who says yes, and the motion passes four to three. The preset "
                  "<em>one-abstains</em> has six members, three yes, two no and one abstaining: "
                  "under the greater number it passes, and under the rule of more than half "
                  "of all the members it does not, because three is not more than half of six. "
                  "Hobbes's text counts voices given, and the second rule is the lab's "
                  "addition, to show that a rule has to be chosen."),
            ("p", "How often? The lab on this page does not compute it, but the count "
                  "is short, and you can do it by hand. If each member is as likely to say yes as "
                  "no, independently, the chance of an even split in an assembly of "
                  "`n` members, for even `n`, is the number of ways to choose which half say "
                  "yes, divided by all the ways to vote. For `n` equal to 4 that is `6/16`, "
                  "which is `3/8`. For 6 it is `20/64`, `5/16`; for 10 it is `63/256`; for 20 "
                  "it is `46189/262144`, about 17.62 per cent. The chance falls as the assembly "
                  "grows, which agrees with Hobbes's &ldquo;especially when the number is "
                  "not great&rdquo;, and an odd assembly cannot split evenly at all. Real "
                  "members are not coins, and a body that is divided into parties will "
                  "split more often than this model says."),
            ("p", "Hobbes's account has a standard difficulty, and it is old. Locke, "
                  "writing in 1689, accepts that the act of the majority is the act of the "
                  "whole, since a community has to move one way, and Rousseau later asked "
                  "what remains of a dissenter's freedom when he is bound by a "
                  "decision he voted against. Hobbes's answer is the one this chapter "
                  "started with: the dissenter is an author of what the representer does, "
                  "because he gave the authority. Whether giving it was something a "
                  "person can do for good is argued in the next two chapters, and the "
                  "lab cannot argue it."),
            ("p", "So far the multitude has a representer and the representer has a "
                  "voice. The next lesson, &ldquo;The Generation of a Commonwealth&rdquo;, "
                  "asks why anyone would give the authority at all."),
        ],
        "lab": ("levkit", {
            "mode": "assembly",
            "view": "voices",
            "preset": "six-even",
            "presets": [
                {"id": "six-even", "label": "Six members, three yes and three no",
                 "members": "ann, yes; ben, yes; cal, yes; dee, no; eve, no; fay, no",
                 "expect": {"lasDecision": "mute: 3 to 3, an even split of the voices", "lasMargin": "0"}},
                {"id": "seven", "label": "A seventh member joins and says yes",
                 "members": "ann, yes; ben, yes; cal, yes; dee, no; eve, no; fay, no; gil, yes",
                 "expect": {"lasDecision": "passes: 4 to 3 by the greater number of voices given", "lasMargin": "+1"}},
                {"id": "one-abstains", "label": "Six members, one abstains",
                 "members": "ann, yes; ben, yes; cal, yes; dee, no; eve, no; fay, abstain",
                 "expect": {"lasDecision": "passes: 3 to 2 by the greater number of voices given", "lasMargin": "+1", "lasAbstain": "1"}},
            ],
            "panel_title": "What an assembly's voices decide",
            "panel_intro": (
                "Each member says yes, no or abstain. The lab counts the voices and reports "
                "whether the motion passes, fails, or is mute because the voices are equal. "
                "Change one member's voice at a time and watch the margin."
            ),
        }),
        "steps_title": "Reading an assembly's voice",
        "steps_intro": "Four steps, whatever the size of the assembly.",
        "steps": [
            ("Count the voices given",
             "Count the yes and the no. An abstention is not a voice for either, and a "
             "rule that counts all the members should say so."),
            ("Apply the rule",
             "Under the greater number, the larger side wins. If the sides are equal, "
             "the assembly is mute unless the question is of the two kinds Hobbes names."),
            ("Ask whether equality decides",
             "In a trial, equal voices absolve. In a question of executing now or "
             "later, equal voices defer. In any other question, equality means no act."),
            ("Check for a negative voice",
             "If each member can cancel the rest, the assembly acts only when all agree, "
             "and a diverse assembly is often mute."),
        ],
        "worked": {
            "title": "Six councillors and a seventh",
            "intro": [
                "A town council of six votes on a motion to repair the bridge. This is an "
                "example written for the lesson.",
            ],
            "lines": [
                "voices: 3 yes, 3 no, 0 abstain",
                "greater number: no side is greater, so mute",
                "a seventh joins and says yes: 4 against 3",
                "the motion passes with a margin of 1",
                "chance of an even split among 6: C(6,3)/2^6 = 20/64",
                "= 5/16, about 31.25 per cent",
            ],
            "after": [
                "The first two lines are the preset <em>six-even</em> and the next two are "
                "<em>seven</em>. The last two lines are worked by hand, not by the lab: they price "
                "Hobbes's &ldquo;oftentimes&rdquo; for an assembly of six on the coin-"
                "flipping model, nearly a third of the time.",
            ],
        },
        "quiz_title": "Counting voices",
        "quiz": [
            {"q": "An assembly of eleven has five yes, four no and two abstaining. On the lab's "
                  "default rule, the greater number of voices given, what is the decision?",
             "a": ["Fails, because five is fewer than half of eleven",
                   "Mute, because two members did not vote",
                   "Passes, by a margin of one",
                   "Passes, by a margin of three"],
             "c": 2,
             "why": "The lab counts voices given: five yes against four no is a margin of "
                    "one, and the two abstentions are not a voice for either side. A rule "
                    "that needs more than half of all eleven would fail the motion, but "
                    "that is the other rule, not the default."},
            {"q": "On Hobbes's account, what do equal voices decide when an assembly is "
                  "trying a man?",
             "a": ["The man is condemned",
                   "The man is absolved",
                   "The assembly is mute and the trial cannot end",
                   "The trial is begun again before a larger assembly"],
             "c": 1,
             "why": "&ldquo;equality of votes, even in that they condemne not, do "
                    "absolve&rdquo;, because &ldquo;not to condemne, is to absolve&rdquo;. "
                    "Hobbes lists this as a case in which equality settles the matter, "
                    "and the reverse, that not to absolve is to condemn, he says is not "
                    "true."},
            {"q": "Each of the four members of an assembly is as likely to say yes as no, "
                  "independently. What is the chance of an even split?",
             "a": ["1/2", "1/4", "3/8", "1/16"],
             "c": 2,
             "why": "Of the sixteen ways to vote, six have two yes and two no, since "
                    "C(4,2) = 6. Six sixteenths is `3/8`. One half is the chance for an "
                    "assembly of two, and the others do not count any set of voters."},
            {"q": "Why does Hobbes say that three or more members each holding a negative "
                  "voice are no representative?",
             "a": ["An odd number of members always splits evenly",
                   "Any one member can cancel the others, so by diversity of opinions "
                   "the body is often a mute person",
                   "A negative voice counts only in an assembly of even number",
                   "Three members can never agree on anything"],
             "c": 1,
             "why": "Hobbes: a body whose every member can take away the effect of the "
                    "rest &ldquo;becomes oftentimes, and in cases of the greatest "
                    "consequence, a mute Person&rdquo;. An odd number cannot split "
                    "evenly, so the first option is false, and the others state "
                    "things Hobbes does not say."},
        ],
        "mistakes": [
            ("Thinking an even assembly is always mute",
             "Hobbes says it is &ldquo;oftentimes&rdquo; mute, not always, and says that "
             "in a trial or in a question of delay, equal voices decide. On the "
             "coin-flipping model an assembly of six splits evenly `5/16` of the time, "
             "which is often and nowhere near always."),
            ("Thinking the crowd itself is one person",
             "The multitude stays many. What is one is the representer, and the crowd "
             "is one person only through it. If no one has been authorised by each, "
             "there is no person there to covenant with."),
            ("Reading an odd assembly as one that cannot go wrong",
             "An odd number cannot split evenly, and Hobbes still denies that three or "
             "more members who each hold a negative voice make a representative, because "
             "any one of them can undo the rest. The trouble there is the veto and not "
             "the evenness."),
        ],
        "standard": (
            "Finish when you can decide what a set of voices carries.",
            "Given an assembly's yes, no and abstaining voices and a rule, say whether "
            "the motion passes, fails or is mute, and give the chance of an even split "
            "for an assembly of a stated size on the coin model."
        ),
        "note": (
            "The ties figure assumes every member votes independently with equal chance "
            "of yes and no, which is a model of this lesson and not Hobbes's, and real "
            "assemblies are rarely like that. The lab also cannot say whether a minority "
            "is rightly called an author of what it voted against; that is what Hobbes "
            "claims and Rousseau and others question."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Leviathan ch. 17, 1651 p. 85; PDF p. 213 (covenants without the sword and the
    # end of a commonwealth); PDF p. 214-215 (small numbers, great multitudes,
    # bees and ants); PDF p. 216 (the generation); PDF p. 217 (the definition).
    {
        "slug": "the-generation-of-a-commonwealth",
        "title": "The Generation of a Commonwealth",
        "module": "Chapter 17 · Of the Causes, Generation, and Definition of a Common-wealth",
        "one_line": "Peace between many people needs more than their agreement: without a common power breaking pays each of them, and a penalty large enough to change the payoffs is what the covenant of every man with every man creates.",
        "summary": (
            "Hobbes asks what would make the laws of nature keep, answers that covenants "
            "without the sword are but words, and defines a commonwealth as one person "
            "authorised by every man with every man. Write ten people choosing between "
            "keeping and breaking a peace as a payoff table, find the equilibrium with no "
            "sovereign, and find the penalty at which keeping pays whatever the others do."
        ),
        "key": [
            "no sword: breaking pays whatever others do",
            "all breaking: worse for each than all keeping",
            "a penalty is subtracted from breaking",
            "border penalty: breaking just ties keeping",
            "commonwealth: every man with every man",
        ],
        "key_label": "A peace that has to be enforced",
        "concepts_intro": (
            "Chapter 17 is the first chapter of Part II, and it goes from a diagnosis to "
            "a definition in five pages."
        ),
        "concepts": [
            ("The laws of nature are not enough",
             "The laws of nature, such as justice, equity and mercy, are contrary to "
             "natural passions that carry us to partiality, pride and revenge. Without "
             "a power to make them observed, every man relies on his own strength, and "
             "&ldquo;Covenants, without the Sword, are but Words&rdquo;."),
            ("Numbers and agreement do not supply it",
             "A few men joined together are not secure, because small additions on either "
             "side decide the victory. A great multitude whose actions are directed by "
             "each one's judgement hinders itself. Even a single judgement for a limited "
             "time, as in one war, dissolves when the common enemy goes."),
            ("The covenant of every man with every man",
             "The one way to erect a common power is to confer all power and strength "
             "upon one man or one assembly, that may reduce all their wills to one will, "
             "each owning what that person does. The multitude so united in one person "
             "is a commonwealth."),
        ],
        "read_title": "The passage first, then the argument in order",
        "read_intro": (
            "The sentence on covenants and the sword comes first. The chapter then "
            "rejects three ways of getting peace without a sovereign, answers the "
            "question of the bees, and defines the commonwealth."
        ),
        "body": [
            ("p", "<strong>Chapter 17.</strong> &ldquo;Covenants, without the Sword, are "
                  "but Words, and of no strength to secure a man at all.&rdquo;"),
            ("p", "Before it, Hobbes says what commonwealths are for. The end of men, who "
                  "naturally love liberty and dominion over others, in putting that "
                  "restraint on themselves is &ldquo;the foresight of their own "
                  "preservation, and of a more contented life thereby&rdquo;: to get out of "
                  "the miserable condition of war that Chapter 13 derived from their "
                  "passions. The Philosophy course &ldquo;Games and the Social "
                  "Contract&rdquo; has a lesson, &ldquo;Hobbes and the State of "
                  "Nature&rdquo;, that writes that war as a game between two people; this "
                  "lesson takes the question that comes next, what a large number of "
                  "people need to be secure, and does not repeat it."),
            ("p", "The laws of nature, Hobbes has argued, bind a man to want peace; they do "
                  "not make it safe to act peacefully while others do not. Taken alone "
                  "they &ldquo;are contrary to our naturall Passions, that carry us to "
                  "Partiality, Pride, Revenge, and the like&rdquo;. So if there is no power "
                  "erected, or not great enough, every man may rely on his own strength "
                  "and art, and Hobbes adds that in his own day cities and kingdoms do the "
                  "same, for want of other caution, and are remembered for it with honour."),
            ("p", "Then three tempting answers. Is it enough to join a small number "
                  "together? No: &ldquo;small additions on the one side or the other, make "
                  "the advantage of strength so great, as is sufficient to carry the "
                  "Victory&rdquo;, and the multitude to confide in is fixed &ldquo;by "
                  "comparison with the Enemy we feare&rdquo;. Is a very large multitude "
                  "enough? Not if each acts on his own judgement, because then &ldquo;they "
                  "do not help, but hinder one another; and reduce their strength by "
                  "mutuall opposition to nothing&rdquo;, and a very few who agree can "
                  "subdue them. If a great multitude could keep the laws of nature without a "
                  "common power, he says, we might as well suppose all mankind could, and "
                  "then there would be no need of government at all, &ldquo;because there "
                  "would be Peace without subjection&rdquo;. Is one "
                  "judgement for a limited time enough, as in one battle or one war? No: "
                  "when the enemy goes, the differences of interest remain, and they "
                  "fall back into war among themselves."),
            ("p", "Then the objection every reader makes. Bees and ants live sociably, "
                  "&ldquo;certain living creatures, as Bees, and Ants, live sociably one "
                  "with another&rdquo;, and Aristotle called them political creatures; why "
                  "cannot mankind? Hobbes gives six answers, and the lesson gives the "
                  "first two and the last. First, &ldquo;men are continually in competition "
                  "for Honour and Dignity&rdquo;, which they are not. Secondly, for them "
                  "&ldquo;the Common good differeth not from the Private&rdquo;, whereas "
                  "man, whose joy consists in comparing himself with other men, &ldquo;can "
                  "relish nothing but what is eminent&rdquo;. The middle three are about "
                  "reason, the art of words and the difference between injury and damage. "
                  "And lastly: &ldquo;the agreement of these creatures is Naturall; that of "
                  "men, is by Covenant only, which is Artificiall&rdquo;, so something more "
                  "is needed, &ldquo;a Common Power, to keep them in awe, and to direct "
                  "their actions to the Common Benefit&rdquo;."),
            ("p", "Write the bee's case as a table and it is what Hobbes says it is. The "
                  "lab's ten people each choose to keep the peace or to break it. Let "
                  "`k` be the number of the other nine who keep it. A keeper gets `1 + k`: "
                  "each other keeper adds one to his security. A breaker gets `5 + k`: the "
                  "same, plus a plunder of four. In the preset <em>men</em> breaking pays four "
                  "more than keeping, whatever `k` is, so each does better to break "
                  "whatever the rest do, and the one equilibrium is that nobody keeps. Each "
                  "then gets 5, against 10 each if all had kept it. This is the "
                  "multitude of the chapter, no worse than it would be at peace in what each "
                  "wants, and ruined by what each does."),
            ("p", "Now the sword. The one way to erect such a power, Hobbes says, is to "
                  "&ldquo;conferre all their power and strength upon one Man, or upon one "
                  "Assembly of men, that may reduce all their Wills, by plurality of "
                  "voices, unto one Will&rdquo;. He gives it as a formula: &ldquo;I "
                  "Authorise and give up my Right of Governing my selfe, to this Man, or to "
                  "this Assembly of men, on this condition, that thou give up thy Right to "
                  "him, and Authorise all his Actions in like manner.&rdquo; Chapter 16's "
                  "machinery is doing the work: each is author of what the one person acts. "
                  "&ldquo;This is more than Consent, or Concord; it is a reall Unitie of "
                  "them all, in one and the same Person, made by Covenant of every man "
                  "with every man&rdquo;. The multitude so united is called a "
                  "commonwealth, and this is &ldquo;the Generation of that great "
                  "LEVIATHAN&rdquo;, or, to speak more reverently, of that &ldquo;Mortall "
                  "God&rdquo;, to which we owe, under the Immortal God, our peace and defence."),
            ("p", "The three penalty presets show what such a power does to the table "
                  "and nothing more. A penalty `p` on breaking is subtracted from the "
                  "breaker's payoff. At <em>penalty-3</em> breaking still pays one more than "
                  "keeping at every `k`, and the equilibrium is unchanged. At "
                  "<em>penalty-4</em> the two are exactly equal at every `k`, the border at "
                  "which the lab can no longer say that breaking dominates. At "
                  "<em>penalty-5</em> keeping pays one more than breaking, whatever "
                  "the others do, and the one equilibrium is that all ten keep the peace. "
                  "The table has now become the bees' table, in which the private "
                  "good and the common good coincide."),
            ("p", "What the lab does not show is where the penalty comes from, and "
                  "that is the chapter's definition. The sovereign is not a tenth player "
                  "who happens to punish. He is the person every one has authorised, and "
                  "&ldquo;by terror&rdquo; of the strength that each has conferred on him he "
                  "can bring the wills of all to peace at home and mutual aid abroad. The "
                  "commonwealth is &ldquo;One Person, of whose Acts a great Multitude, by "
                  "mutuall Covenants one with another, have made themselves every one the "
                  "Author, to the end he may use the strength and means of them all, as he "
                  "shall think expedient, for their Peace and Common Defence&rdquo;. "
                  "Critics of Hobbes ask whether the sovereign himself needs a sword over "
                  "him, and how a table with a penalty ever got its penalty; the next "
                  "lesson is Hobbes's side of that argument."),
            ("p", "The next lesson, &ldquo;The Rights of Sovereigns by Institution&rdquo;, "
                  "turns to Chapter 18 and asks what the one person so made may do, and "
                  "what his subjects may not."),
        ],
        "lab": ("choicekit", {
            "mode": "commons",
            "gens": 0,
            "preset": "men",
            "presets": [
                {"id": "men", "label": "Ten people with no sovereign",
                 "n": 10, "payC": "1 + k", "payD": "5 + k", "x0": "1/2", "gens": 0,
                 "expect": {"cmDom": "Defect dominates", "cmEq": "k* = 0", "cmOpt": "all 10 cooperate: total 100", "cmUniv": "alone +4, everyone −5"}},
                {"id": "penalty-3", "label": "A penalty of 3 on breaking",
                 "n": 10, "payC": "1 + k", "payD": "5 + k - 3", "x0": "1/2", "gens": 0,
                 "expect": {"cmDom": "Defect dominates", "cmEq": "k* = 0", "cmUniv": "alone +1, everyone −8"}},
                {"id": "penalty-4", "label": "A penalty of 4, the border",
                 "n": 10, "payC": "1 + k", "payD": "5 + k - 4", "x0": "1/2", "gens": 0,
                 "expect": {"cmDom": "neither", "cmEq": "k* = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"}},
                {"id": "penalty-5", "label": "A penalty of 5 on breaking",
                 "n": 10, "payC": "1 + k", "payD": "5 + k - 5", "x0": "1/2", "gens": 0,
                 "expect": {"cmDom": "Cooperate dominates", "cmEq": "k* = 10"}},
            ],
            "panel_title": "A peace of ten, with and without a sword",
            "panel_intro": (
                "Keeping the peace is cooperating and breaking it is defecting. Payoffs "
                "are written in k, the number of the other people who keep the peace. "
                "Subtract a penalty from the breaker's payoff and find the smallest whole "
                "penalty at which keeping dominates."
            ),
        }),
        "steps_title": "Writing a peace as a table",
        "steps_intro": "Four steps, ending in the comparison Hobbes's argument rests on.",
        "steps": [
            ("Fix one person and count the others who keep the peace",
             "Call the count `k`. The only thing one person needs to know about the others "
             "is how many keep it."),
            ("Write what keeping and breaking pay at each k",
             "A keeper's payoff is the security that the other keepers supply. A breaker "
             "gets the same security and whatever he can plunder."),
            ("Compare the two lists",
             "If breaking pays more at every `k`, nobody keeps, and the table has the "
             "multitude in the condition of war. Add up each person's payoff to see "
             "what is lost."),
            ("Subtract the penalty and find the border",
             "Take the penalty from the breaker's side and find where keeping stops "
             "being worse and becomes better. The first whole penalty at which keeping "
             "is strictly better at every `k` is where the peace holds."),
        ],
        "worked": {
            "title": "Ten people and a penalty of five",
            "intro": [
                "Keeping pays `1 + k` and breaking pays `5 + k`, with ten people. The numbers "
                "are an example written for the lesson, not Hobbes's.",
            ],
            "lines": [
                "k others keep: keep 1 + k, break 5 + k",
                "break minus keep = 4, whatever k is",
                "nobody keeps: each gets 5, in all 50",
                "all ten keep: each gets 1 + 9 = 10, in all 100",
                "with penalty p: break minus keep = 4 - p",
                "p = 4 ties; p = 5 makes keeping better by 1",
            ],
            "after": [
                "The difference does not depend on `k`, which is why a single penalty "
                "turns the whole table at once. A penalty of 4 leaves the person "
                "indifferent, and one of 5 makes keeping better whatever the others do.",
            ],
        },
        "quiz_title": "Gain, penalty and border",
        "quiz": [
            {"q": "Nine of the ten keep the peace in the preset men. What does the tenth get "
                  "by keeping and by breaking?",
             "a": ["10 by keeping and 14 by breaking",
                   "14 by keeping and 10 by breaking",
                   "1 by keeping and 5 by breaking",
                   "10 by keeping and 10 by breaking"],
             "c": 0,
             "why": "With `k = 9`, keeping pays `1 + 9 = 10` and breaking pays `5 + 9 = 14`. "
                    "One and five are the payoffs when nobody else keeps, the second option "
                    "swaps the two, and the fourth is the case with the penalty of four."},
            {"q": "What is the smallest whole penalty on breaking at which keeping pays "
                  "strictly more than breaking, whatever the others do?",
             "a": ["3", "4", "5", "10"],
             "c": 2,
             "why": "Breaking minus keeping is `4 - p`. At 3 it is still 1 in favour of "
                    "breaking, and at 4 it is 0, a tie. At 5 it is -1, so keeping is better "
                    "at every `k`. Ten works but is not the smallest."},
            {"q": "Which of these is one of Hobbes's answers to why mankind cannot live "
                  "peaceably without a common power as bees and ants do?",
             "a": ["Bees and ants are fewer in number than men",
                   "Men are continually in competition for honour and dignity, and "
                   "these creatures are not",
                   "Bees and ants obey a queen, who is their sovereign",
                   "Bees and ants have no need of food"],
             "c": 1,
             "why": "It is his first answer: &ldquo;men are continually in competition "
                    "for Honour and Dignity&rdquo;. The chapter does not say bees are "
                    "fewer, does not give them a queen, and does not say they need no food."},
            {"q": "On Hobbes's argument, why is a very great multitude, with no one to direct "
                  "it, still not secure?",
             "a": ["No number of people is ever large enough",
                   "A great multitude cannot make covenants at all",
                   "Directed by each one's own judgement, they hinder one another and "
                   "reduce their strength by mutual opposition to nothing",
                   "The laws of nature forbid large numbers from acting together"],
             "c": 2,
             "why": "&ldquo;they do not help, but hinder one another; and reduce their "
                    "strength by mutuall opposition to nothing&rdquo;. Hobbes says the number "
                    "enough to confide in is fixed by comparison with the enemy, not by "
                    "any count, and he does not say that a multitude cannot covenant "
                    "or that the laws of nature forbid it."},
        ],
        "mistakes": [
            ("Thinking that a covenant of peace keeps itself",
             "In the preset <em>men</em> every person would prefer everyone's keeping "
             "(10 each) to everyone's breaking (5 each), and each still does better "
             "to break whatever the others do. Hobbes's &ldquo;Covenants, without the "
             "Sword, are but Words&rdquo; is a claim about that table, not about anyone "
             "being wicked."),
            ("Thinking a large enough multitude needs no sovereign",
             "Hobbes says the multitude to confide in is fixed by comparison with the "
             "enemy and not by a number, and that a great multitude whose actions are "
             "directed by each man's judgement is no defence. Size alone does not change "
             "the payoffs."),
            ("Reading the commonwealth as a covenant between the people and a ruler",
             "The definition says the multitude, &ldquo;by mutuall Covenants one with "
             "another&rdquo;, have each become the author of the one person's acts. The "
             "covenant is of every man with every man, and the sovereign is the one "
             "person so authorised, not a party to it."),
        ],
        "standard": (
            "Finish when you can show why a peace needs a power and what the power must do.",
            "Given a table of keeping and breaking payoffs for several people, say "
            "whether breaking dominates, what the equilibrium and the best total are, and "
            "find the smallest penalty at which keeping is strictly better."
        ),
        "note": (
            "The payoffs are chosen for the lesson, and the penalty is simply subtracted; "
            "the lab does not say who imposes it, whether he can be trusted to, or "
            "what he costs. Those are the questions Chapter 17's definition answers "
            "and the next chapters press, and critics who think a commonwealth could "
            "stand on less, or that this one is worse than the war, argue them with "
            "reasons the lab cannot weigh."
        ),
    },
]
