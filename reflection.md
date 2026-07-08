# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

In my initial UML design, I included the classes
- Pet, to represent a real-life pet. This class did not hold any information beyond the pet's name, but it could be expanded in the future if necessary.
- Owner, to represent the owner of various pets. This class held the owner's name and their list of pets.
- Task, to represent a task that an owner would need to complete. This class held a large amount of information, from the title of the task, to the pets involved, to the duration, start time, end time, and priority.
- Schedule, which would contain a collection of tasks and when they would be completed. Tasks could be added, removed, and searched.
- Scheduler, to handle the logic of sorting and scheduling tasks.
- Priority, an enumeration that would determine the priority of a task.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

My design did change during implementation. I asked Claude for feedback on my implementation using the prompt, `"Do you notice any missing relationships or potential logic bottlenecks in @pawpal_system.py  ? I am attaching @diagrams/uml_draft.mmd  for reference"`. In response, Claude made a few suggestions:
- It pointed out that my initial UML contained mutator functions for certain fields, such as `name` in the `Pet` class. Because the actual implementation used a Python dataclass that was not frozen, I decided that it would be possible to set the name directly without accessing it through a function. I similarly deleted the mutators in the `Owner` and `Task` classes.
- Claude pointed out that a Schedule did not have an owner, so I added an owner field to the `Schedule` class.
- Based on Claude's feedback, I also made `Priority` an enumeration.

**c. Three core actions a user should be able to perform**

- See a schedule of all events for the day
- See a list of all pets
- Schedule an event

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
