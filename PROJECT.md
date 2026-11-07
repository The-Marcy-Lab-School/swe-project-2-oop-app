# Project 2: Build an Object-Oriented System

**Table of Contents**

- [What You Are Building](#what-you-are-building)
- [AI Use on This Project](#ai-use-on-this-project)
- [Choose Your Path](#choose-your-path)
- [What Both Paths Must Have](#what-both-paths-must-have)
- [Above and Beyond](#above-and-beyond)
- [Deliverables](#deliverables)
- [Setup](#setup)
- [Git Workflow](#git-workflow)
- [Path A: Borough Food Rescue](#path-a-borough-food-rescue)
- [Path B: The Library of Things](#path-b-the-library-of-things)
- [Project Grading](#project-grading)
- [Tips / Common Mistakes to Avoid](#tips--common-mistakes-to-avoid)
- [Stuck Getting Started?](#stuck-getting-started)
- [Submitting](#submitting)

## What You Are Building

A stakeholder has a problem, and they have come to you to solve it with software.

In Mod 1 you built a program. In this project you design a *system*: several
classes that each hold their own data, protect it from invalid changes, and
talk to each other through interfaces you decide on. The hard part is no longer
getting the code to run. The hard part is deciding which object is responsible
for what, and that decision is what this project assesses.

Keep this application in a good state as you go, because you will see it again.
In January, when Mod 3 starts, you will hand your design document to an AI model, ask it to build
a new feature for the system you are about to write by hand, and your job then
will be to find what the model got wrong. A design document that is vague
produces generated code you cannot judge, so the clarity you put in now is what
makes that exercise possible later.

## AI Use on This Project

**Tutor mode is the mode for this project.** You write every line you submit.
Quarter 1 is the quarter where code is written by hand, and this is the last
project in it — in Quarter 2 the AI moves from tutor to implementer and your job
moves to specifying and verifying. The skill being built here is the one that
makes that possible: deciding which object is responsible for what.

So ask it a hundred questions. How does a `@property` setter refuse a value.
Why does your subclass's `__init__` lose the parent's attributes. Which of your
two classes should own the due date. What your diagram is missing. What it does
not do is write the feature, the class, or the diagram. Paste this at the start
of a chat and it will hold for the rest of the conversation:

> You are acting as a tutor. Your job is to explain what this coding question
> is asking, clarify confusing wording, and highlight the relevant concepts I
> need to know — but do not provide the full solution or code that directly
> answers the question. Instead, rephrase the problem in simpler terms,
> identify what is being tested, and suggest what steps or thought processes
> might help. Ask me guiding questions to make sure I am thinking critically.
> Do not write the final function, algorithm, or code implementation.

There is a further rule for `DESIGN.md`, in [Deliverables](#deliverables): you
have to be able to defend every line of it, because in January you will hand it
to a model and judge what it builds.

You own every line either way, and you will be asked to explain it.

## Choose Your Path

Choose **one** of two stakeholders. Both require the same work and are graded by
the same rubric, so pick the problem you would rather spend three weeks inside.

**Path A: Borough Food Rescue** — move surplus food to neighborhood fridges
before it spoils.

**Path B: The Library of Things** — lend tools, laptops, and instruments without
losing track of them.

Read [What Both Paths Must Have](#what-both-paths-must-have) first. Then read
your path's section and ignore the other one.

## What Both Paths Must Have

Your rubric checks these nine things. Every number below is countable, so you
can check your own work before you submit it. The *names* of your classes depend
on your path. The structures and the counts do not.

**1. Classes.** Define **at least five classes**, filling these roles:

| Role | How many |
| --- | --- |
| A coordinator that owns the collections and enforces the rules | 1 |
| A superclass whose subclasses behave differently | 1 |
| Subclasses of that superclass | at least 2 |
| An intermediary that represents a relationship between two entities | 1 |

Every class you define has **at least 3 attributes**, **at least 2 methods**, and
a `__repr__` that returns something you would want to see in a traceback.

**2. Encapsulation.** **At least 3 attributes** across your system are
non-public and reached through a `@property`. **At least 1 setter refuses an
invalid value** and tells the user why, instead of storing it.

Ask of each attribute: would your system break if this held a wrong value? A
fridge's capacity or a member's borrowing limit cannot go negative, and a loan's
status has to be one of checked out, returned, overdue, or lost. Those need
protecting. A donor's phone number or an item's description does not, because
there is no wrong value to catch.

**3. Inheritance.** One superclass and **at least 2 subclasses**. Each subclass
calls `super().__init__()`, and **at least 1 method is overridden** so that it
returns a different result in each subclass.

A subclass that only sets `self.kind = "laptop"` does not behave differently.

**4. Polymorphism.** **At least 1 loop** calls the same method on a list holding
more than one subtype. That loop contains **no `isinstance()` and no `type()`**,
so the only thing changing the behavior is the method override.
In `DESIGN.md`, list the method names that every one of those subtypes defines.
That list is the contract the loop depends on: the loop can stay the same because
every object in it answers to the same names.

**5. Collections of objects.** **At least 1 class stores a list of instances of
another class you wrote** as an attribute — a fridge holding its deliveries, a
member holding their loans — and has **at least 2 methods that search or filter
that list** and return the matches. A list of dictionaries does not count.

**6. Design strategies — all three.** You are already building all three.
Requirement 1 asks for a coordinator and an intermediary, and both paths need a
delivery or a loan that moves through states. So these are not three new things
to invent. Each one has to meet the counts in the table below, and each one has
to be named in `DESIGN.md` with the class that implements it.

| Strategy | What it takes to count |
| --- | --- |
| **Coordinator** | One class stores at least 2 collections and refuses at least 1 invalid action with a message to the user |
| **Status-Driven Behavior** | One class holds a `_status`, and at least 2 of its methods refuse to run from the wrong status |
| **Intermediary Object** | One class holds references to 2 other objects, plus at least 1 attribute that belongs to the pairing rather than to either object |

**7. A higher-order function.** Write **at least 1**, in either form:

- a **decorator** you wrote, wrapping a method that changes state — a guard named for the status the method needs, such as `@requires_in_transit` or `@requires_checked_out`, is the natural one here, or
- a **method that takes a function as a parameter** and uses it to filter or
  sort a collection.

Say in `DESIGN.md` which form you chose and what it bought you.

**8. Skills from Mod 1, still required.** Nothing you learned in Mod 1 expires.

- **At least 3 modules**, connected with `import`, with an
  `if __name__ == "__main__":` guard in the entry point
- **At least 1 dictionary** used as a lookup
- **At least 1 comprehension or built-in iteration tool** (`sorted()`, `sum()`,
  `enumerate()`, `any()`, `all()`) inside a report
- **Every `input()` validated**, with `try`/`except ValueError` or a string
  method such as `.isdigit()`, so the program never raises in front of a user
- **f-strings** for every message you print
- `requirements.txt` exists and `.venv/` is listed in `.gitignore`

**9. Tests, on the parts that refuse.** pytest is a Mod 1 skill and it does not
expire either. Write **at least 2 tests** in a `tests/` directory that pass when
you run `pytest` from the project root:

- **At least 1 test uses `pytest.raises(ValueError)`** to prove your `@property`
  setter refuses an invalid value.
- **At least 1 test proves a refusal changed nothing** — after the coordinator
  turns down an action, the collection is the same length it was, or the status
  is the one it started with.

You are not asked to test everything. These two are the hardest things in your
system to be sure of by clicking through the menu, which is why they are the two
worth a test.

Your data lives in memory while the program runs. **You are not asked to save
anything to a file**, so do not build a save system.

## Above and Beyond

Not graded, not required. This is where to go once your required work runs.

1. **An abstract base class.** Replace your documented duck-typed contract with
   an ABC and at least one `@abstractmethod`, so a subclass that forgets a method
   fails at instantiation rather than at the call site.
2. **A `@dataclass`** for a value object your system carries around and compares.
   Your `DESIGN.md` already argues about whether one belongs here — this is
   building the version you argued for.
3. **A second higher-order function**, in the form you did not use for
   requirement 7.
4. **Issue each ID from the coordinator.** The coordinator stores the next ID
   and hands it to each new record it creates, so no two records can collide.
5. **More tests than requirement 9 asks for.** Cover every status transition,
   including the ones that are supposed to fail, and use a fixture so each test
   starts from a system you did not have to build by hand.
6. **Persistence.** Save to JSON on exit and load on start.
7. **A decorator factory.** If you wrote one guard per status, replace them with a single `@requires_status("...")` that takes the status as an argument, so one function guards every transition. Put your guards side by side first: the one word that differs between them is the argument the factory takes.

## Deliverables

**1. `DESIGN.md`, due at the start of project week.** Five things:

1. A **UML class diagram**. Draw it by hand and photograph it, or write it as
   text. Mark every attribute `+` public or `-` non-public (one whose name
   begins with `_`).
2. **One line per class**: what data it owns, and what it can do.
3. **One line per relationship**: which class knows about which, whether that is
   one-way or bidirectional, and why.
4. **The three design strategies** you used, each named with its class, and one
   sentence on your higher-order function: which form you chose and what it
   bought you.
5. **One design decision you struggled with**, the options you saw, and how you
   settled it. A decision about something you chose *not* to build counts —
   "`Loan` could have been a `@dataclass`, and here is why it is not" is a good
   answer. Being able to explain the option you rejected is the point, because an
   engineer who can only defend what they built cannot be reviewed.

Write it so that another developer could build your system from it without
asking you a single question.

**Using AI on `DESIGN.md`.** Tutor mode is the right mode here, and you are
encouraged to use it. Ask a model to find a relationship your diagram is
missing, to tell you which responsibility is ambiguous, or to argue the other
side of your design decision. Do not ask it to produce the diagram. You have to
be able to defend every line, because in January you will hand this document to
a model, ask it to build a new feature from it, and find what it got wrong. A
document you did not reason through gives you nothing to judge the output
against.

Practice saying it out loud. You will be asked to explain this system and defend
the decisions inside it, and the explanation you want in that moment is the one
you already wrote here.

**2. The application**, meeting your path's requirements.

**3. `README.md`, replaced.** The file you are given tells you to replace it. Do
that: what your system does, how to run it, and a usage example, written for
someone who has never seen it. It is the first thing anyone looks at.

**4. `REFLECTIONS.md`**, two responses of 150-250 words each. Prompts are in
[Project Grading](#project-grading).

**5. A five-minute share-out**, presented on 12/16. Five steps, in this order:

1. The stakeholder's problem, in your own words, in two sentences.
2. A walk through your UML diagram, naming what each class owns.
3. **One refusal, demonstrated live.** Try the thing your system will not allow
   and let everyone see the message.
4. The design decision you struggled with, and how you settled it.
5. What you would change if you started again.

Every step except the live demo should already be written in `DESIGN.md`. You are not
preparing new material; you are saying out loud what you already decided, which
is also what the module assessment asks you to do.

## Setup

Work in `development/mod-2`.

1. Go to the `swe-project-2-oop-app` template repository and click "Use this
   template". Set yourself as the owner and give your project a descriptive name.
2. Clone your repo down to your computer.
3. Create and activate a virtual environment:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Check that `.venv/` is listed in your `.gitignore` file.
5. Install pytest and record it, because requirement 9 needs it:

   ```sh
   pip install pytest
   pip freeze > requirements.txt
   ```

6. Confirm the example test runs: `pytest`. It passes, and it is there to be
   copied and then deleted.
7. Add, commit, and push all files with the message `"initializing project"`.
8. Make a draft branch before you start: `git checkout -b draft`.

## Git Workflow

Your `main` branch holds the most recent **working** version of your
application. Build on a branch and merge when the feature runs.

```sh
git checkout -b feature-name
# write code, test it, commit
git checkout main
git merge feature-name
```

Commit every time something works. A commit you can return to is worth more
than a commit that is tidy.

## Path A: Borough Food Rescue

> **Borough Food Rescue** moves surplus food from restaurants and grocers to
> twelve neighborhood fridges. Today one coordinator runs the whole operation
> from a group chat and a spreadsheet, and two things keep going wrong. Food gets
> promised to a fridge that is already full, so a volunteer drives across the
> borough and has nowhere to leave it. And perishable food sits in the
> spreadsheet long enough to expire, so it gets thrown away at the fridge instead
> of eaten. They have asked you to build a system that tracks what food is
> available, where it is allowed to go, and what state every delivery is in.

**The entities in this domain** are donor sites, fridge locations, food items,
and deliveries. Food items come in at least two kinds: **perishable** items,
which expire, and **shelf-stable** items, which do not. How those entities are
structured, which of them owns which data, and which of them are related is your
design work.

**Required features**

1. **Register a donor site and a fridge location.** A fridge has a capacity and a delivery time, the number of days a delivery takes to reach it, and the system knows how full it is right now.
2. **Add a food item to the system**, from a donor site. Perishable and
   shelf-stable items both answer "how many days until you expire?" — and they
   answer it differently.
3. **Claim an item for a fridge.** This creates a delivery. The system **refuses**
   the claim when the fridge has no room, and when a perishable item would expire before it could be delivered: when the item has fewer days until it expires than the fridge's delivery time.
4. **Move a delivery through its states**: claimed, in transit, delivered. A
   delivery that has already been delivered cannot be delivered again, and
   attempting it gets a clear message rather than a second delivery.
5. **Report**: what food is available now, what is in transit, what each fridge is
   holding, and what expired before anyone moved it.

**Stretch features to consider**

- A volunteer entity, assigned to deliveries, with a cap on how many they carry
  at once.
- Expiry-aware prioritization: the report suggests which item to move first.
- A second fridge-level rule, such as refusing items a fridge cannot store.

## Path B: The Library of Things

> **The Library of Things** lends more than books. It lends power tools, laptops,
> and musical instruments, and it lends them on paper index cards. Two things keep
> going wrong. An item gets lent twice, because the card for the first loan is in
> a different drawer, and the second borrower arrives to collect something that
> left the building yesterday. And members walk out with eight items at once,
> because nothing stops them, and those items do not come back. They have asked
> you to build a system that tracks every item, every member, and the state of
> every loan.

**The entities in this domain** are members, catalog items, loans, and the
lending desk itself. Catalog items come in at least two kinds — tools, laptops,
instruments — and they do not all behave the same way. How those entities are
structured, which of them owns which data, and which of them are related is your
design work.

**Required features**

1. **Register a member and add items to the catalog.** A member has a borrowing
   limit, and the system knows how many items they are holding right now.
2. **Items answer two questions differently by kind**: "when are you due back?"
   and "what is the late fee per day?" A laptop is not due back on the same
   schedule as a hammer.
3. **Check an item out to a member.** This creates a loan. The system **refuses**
   the checkout when the item is already on loan, and when the member is at their
   limit.
4. **Move a loan through its states**: checked out, returned, overdue, lost. A
   loan that has been returned cannot be returned again, and attempting it gets a
   clear message rather than a second return.
5. **Report**: what is on the shelf, what is out, what each member is holding, and
   what is overdue along with the fees owed.

**Stretch features to consider**

- A hold queue: a member requests an item that is out and is notified in turn.
- A condition log on each item, recorded at checkout and return.
- A second desk-level rule, such as blocking checkout for a member who owes fees.

## Project Grading

Every line below is countable, so you can check your own project against it
before you submit. Your project is assessed out of **35 points**.

- Stakeholder Requirements (5 points)
- Core OOP Concepts (7 points)
- Design Strategies, Collections, and Higher-Order Functions (6 points)
- System Design (3 points)
- Tests (2 points)
- Skills from Mod 1 and Code Organization (3 points)
- Reflection and Presentation (4 points)
- Professionalism and Craftsmanship (5 points)

### Stakeholder Requirements (5 points)

One point per required feature in your path's brief. These lines ask only whether
the feature works, so run each one before you submit.

1. Both kinds of record can be registered, and the system reports the current
   state that limits them — how full a fridge is, or how many items a member is
   holding.
2. Both kinds of item answer their shared question, and the two kinds give
   different answers.
3. Claiming or checking out creates the delivery or the loan, and is refused in
   both of the cases your brief names, each with a message the user can read.
4. The delivery or loan moves through its states, and repeating a step that is
   already done is refused with a message rather than happening twice.
5. Every report your brief asks for runs and prints the right rows.

### Core OOP Concepts (7 points)

1. At least 5 classes are defined, each with at least 3 attributes and at least 2
   methods, covering coordinator, superclass, 2 subclasses, and intermediary.
2. Every class returns a useful string from `__repr__`.
3. At least 3 attributes are non-public and reached through a `@property`.
4. At least 1 `@property` setter refuses an invalid value and says why.
5. Every subclass calls `super().__init__()`.
6. At least 1 method is overridden and returns a different result per subclass.
7. At least 1 loop calls a shared method on mixed subtypes, with no `isinstance()`
   and no `type()` inside it, and `DESIGN.md` lists the method names every
   subtype defines.

### Design Strategies, Collections, and Higher-Order Functions (6 points)

1. Coordinator, Status-Driven Behavior, and Intermediary Object all appear in
   the code and are named in `DESIGN.md` with their class.
2. The coordinator stores at least 2 collections and refuses at least 1 invalid
   action, with a message to the user rather than a silent failure.
3. The status-driven class holds a `_status`, and at least 2 of its methods
   refuse to run from the wrong status.
4. The intermediary holds references to 2 other objects and at least 1 attribute
   that belongs to the pairing rather than to either object.
5. At least 1 class stores a list of instances of another class, not
   dictionaries, and has at least 2 methods that search or filter it.
6. At least 1 higher-order function is written, and `DESIGN.md` says which form
   it takes and what it bought.

### System Design (3 points)

1. `DESIGN.md` contains a UML class diagram that marks every attribute public or
   non-public, every class in the diagram exists in the code, and each class has
   a line saying what data it owns and what it can do.
2. Every relationship is listed with a direction and a reason.
3. One design decision is written up with the options considered and the
   reasoning that settled it.

### Tests (2 points)

1. At least 1 test uses `pytest.raises(ValueError)` to prove a `@property` setter
   refuses an invalid value.
2. At least 1 test proves a refused action changed nothing: after the refusal the
   collection is the same length, or the status is unchanged.

Both live in `tests/` and pass when `pytest` is run from the project root.

### Skills from Mod 1 and Code Organization (3 points)

1. Code is split across at least 3 modules, connected with `import`, with an
   `if __name__ == "__main__":` guard in the entry point.
2. At least 1 dictionary lookup and at least 1 comprehension or built-in
   iteration tool appear in a report, and every printed message uses an f-string.
3. Every `input()` is validated, the program never raises in normal use,
   `requirements.txt` exists, and `.venv/` is in `.gitignore`.

### Reflection and Presentation (4 points)

In `REFLECTIONS.md`, respond to both prompts in 150-250 words each.

1. Describe one design decision where you chose between two reasonable
   structures. What did you choose, what did you give up, and what would make you
   choose differently next time?
2. Explain one Mod 2 concept you understand more deeply after building this, in
   plain terms, and point to the place in your code where it earns its keep.

In the share-out on 12/16:

3. All five steps are covered in five minutes, and the refusal is demonstrated
   live rather than described.
4. Every class named in the walkthrough matches a class in the code, and every
   question about why a decision was made gets an answer.

### Professionalism and Craftsmanship (5 points)

1. Code is functional and raises no errors under expected use.
2. Code is well organized, names are descriptive, comments are purposeful, and no
   unused code remains.
3. Commits are small, frequent, and meaningfully described.
4. A branch is used for development, and `main` always runs.
5. `README.md` explains setup, usage, and functionality. Writing in `README.md`,
   `DESIGN.md`, and `REFLECTIONS.md` is polished.

## Tips / Common Mistakes to Avoid

| Mistake | What to Do Instead |
| --- | --- |
| Designing at the keyboard | Draw the UML first. Thirty minutes on paper saves a day of restructuring. |
| One class that does everything | If a class's name needs "and" in it, it is two classes. |
| Storing relationship data on an entity | A loan's due date belongs to the loan, not to the item and not to the member. That is what the intermediary object is for. |
| Making every attribute public | Ask of each one: would the system break if this held a wrong value? If yes, protect it. |
| Subclasses that differ only by a string | A subclass earns its place by behaving differently. If every method is identical, you wanted an attribute. |
| Asking AI to draw your UML | Ask it to find what your diagram is missing. You cannot defend a design you did not reason through, and in January you will have to. |
| `if isinstance(...)` branching on subtype | Move the differing behavior into the subclasses and call the method. That is polymorphism doing the work. |
| Letting any object change another's status | Status changes go through a method on the object that owns the status, so the rules run every time. |
| Building all five features, then testing | Build one feature, run it, commit, move on. |

## Stuck Getting Started?

Five build days, and the share-out on the sixth. Commit at the end of every step,
not at the end of every day.

**Before Day 1: `DESIGN.md` is already done.** It was due at the start of the
week. Keep it open beside your editor, and when the code disagrees with the
diagram, change the diagram.

**Day 1 — the entities, running.** Pick the simplest entity. Write `__init__` and
`__repr__`, create two instances in `main.py`, and print them. Then write the
superclass and its two subclasses, give them the one method each subclass answers
differently, and loop over a mixed list calling it. By the end of today, objects
exist and print.

**Day 2 — protect the data, then connect it.** Make the attributes that could
hold wrong values non-public with a `@property`, and make one setter raise
`ValueError`. **Write your first test now**, while the setter is fresh: one
`pytest.raises(ValueError)`. Then write the intermediary — the class that
connects two entities, holding a `_status` and the methods that move it from one
status to the next, each refusing to act from the wrong status.

**Day 3 — the coordinator and the rules.** Write the class that owns the
collections. Put the refusals in it: the capacity or limit check, and the
already-out check. Add the methods that search or filter its lists, because the
reports are going to need them. **Write your second test**: refuse an action,
then assert the collection is the same length it was.

**Day 4 — the menu and the reports.** Wire the features to numbered choices and
validate every input. Build the reports out of the search methods you wrote
yesterday. Split the code across at least three modules if you have not already,
and put the `if __name__ == "__main__":` guard in the entry point. Write your
higher-order function today — if you chose the decorator, it wraps the transition
methods from Day 2.

**Day 5 — polish and rehearse.** The project is due at the end of today. Make
`DESIGN.md` match the code you actually wrote, write `REFLECTIONS.md`, run
`pytest` one more time, and reread every message your program prints for
spelling. Then run your five steps out loud once, with a timer.

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

1. Push your work to `main` and confirm the application runs from a fresh clone.
2. Run `pytest` from the project root and confirm both required tests pass.
3. Confirm `DESIGN.md`, `REFLECTIONS.md`, and `README.md` are all present and
   polished.
4. Open a pull request to your instructor for feedback.
5. Bring your five steps to the share-out on 12/16, ready to demonstrate a
   refusal live.
