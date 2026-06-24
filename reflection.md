# PawPal+ Project Reflection

## 1. System Design

**Core user actions**

Based on the PawPal+ scenario, a user should be able to perform these three core actions:

1. **Add or edit a pet care task.** The owner can enter a care task (such as a walk, feeding, medication, or grooming) along with details like how long it takes (duration) and how important it is (priority). They can also update or remove a task as their needs change.

2. **Generate a daily plan.** The owner asks the app to build a schedule for the day. The scheduler looks at all the tasks together with the owner's constraints — how much time is available, each task's priority, and personal preferences — and arranges the tasks into a workable daily plan.

3. **View today's plan and reasoning.** The owner can see the generated schedule laid out clearly (which tasks happen, in what order, and roughly when), along with an explanation of why the app chose that plan — for example, which high-priority tasks were kept and which lower-priority tasks were dropped when time ran short.

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

**Building blocks (objects, attributes, methods)**

These are the main objects I expect the system to need. Each lists the information it holds (attributes) and the actions it can perform (methods).

1. **Owner** — represents the person caring for the pet and their scheduling preferences.
   - *Attributes:* `name`, `available_minutes` (time budget for the day), `preferences` (e.g., preferred order, blackout times, favorite task types).
   - *Methods:* `add_pet(pet)`, `set_available_time(minutes)`, `set_preference(key, value)`.

2. **Pet** — represents an animal that needs care.
   - *Attributes:* `name`, `species`, `notes` (e.g., age, medical info).
   - *Methods:* `describe()` (returns a short summary used in the UI/plan).

3. **CareTask** — represents one thing that needs to happen (walk, feeding, meds, grooming, enrichment).
   - *Attributes:* `title`, `duration_minutes`, `priority` (low/medium/high), `recurrence` (e.g., daily/weekly), optional `preferred_time`.
   - *Methods:* `priority_rank()` (turns priority into a sortable number), `update(...)` (edit fields), `is_due_today()`.

4. **Scheduler / Planner** — the brain that turns a list of tasks plus constraints into a plan.
   - *Attributes:* `tasks` (list of CareTask), `available_minutes`, `preferences`.
   - *Methods:* `add_task(task)`, `remove_task(task)`, `sort_tasks()` (by priority, then duration), `build_plan()` (selects/orders tasks that fit the time budget), `explain()` (describes why tasks were kept or dropped).

5. **DailyPlan** — the result the scheduler produces and the UI displays.
   - *Attributes:* `entries` (ordered list of scheduled tasks with start times), `total_minutes`, `skipped_tasks`, `reasoning` (text explanation).
   - *Methods:* `add_entry(task, start_time)`, `summary()`, `to_table()` (rows for the Streamlit display).

6. **ScheduledTask / PlanEntry** *(helper)* — pairs a CareTask with a concrete time slot inside a DailyPlan.
   - *Attributes:* `task` (CareTask), `start_time`, `end_time`.
   - *Methods:* `formatted()` (e.g., `"08:00 — Morning walk (20 min) [high]"`).

*Relationships:* an Owner has one or more Pets; the Scheduler holds many CareTasks and produces one DailyPlan; a DailyPlan contains many PlanEntries, each wrapping one CareTask.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

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
