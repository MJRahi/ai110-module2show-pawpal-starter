"""PawPal+ logic layer.

Backend classes for the pet care planning assistant. This is the "skeleton"
generated from the UML draft (diagrams/uml.mmd): class names, attributes, and
empty method stubs. Scheduling logic is implemented in a later step.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Pet:
    """An animal that needs care."""

    name: str
    species: str
    notes: str = ""

    def describe(self) -> str:
        """Return a short summary used in the UI/plan."""
        raise NotImplementedError


@dataclass
class CareTask:
    """One thing that needs to happen (walk, feeding, meds, grooming, ...)."""

    title: str
    duration_minutes: int
    priority: str = "medium"  # low | medium | high
    recurrence: str = "daily"  # e.g., daily | weekly
    preferred_time: str | None = None

    def priority_rank(self) -> int:
        """Turn the priority string into a sortable number."""
        raise NotImplementedError

    def update(self, **fields) -> None:
        """Edit one or more task fields in place."""
        raise NotImplementedError

    def is_due_today(self) -> bool:
        """Whether this task should be scheduled today."""
        raise NotImplementedError


@dataclass
class Owner:
    """The person caring for the pet(s) and their scheduling preferences."""

    name: str
    available_minutes: int = 0
    pets: list[Pet] = field(default_factory=list)
    preferences: dict = field(default_factory=dict)

    def add_pet(self, pet: Pet) -> None:
        """Attach a pet to this owner."""
        raise NotImplementedError

    def set_available_time(self, minutes: int) -> None:
        """Set the time budget available for care tasks today."""
        raise NotImplementedError

    def set_preference(self, key: str, value) -> None:
        """Record an owner preference (e.g., preferred order, blackout times)."""
        raise NotImplementedError


@dataclass
class PlanEntry:
    """Pairs a CareTask with a concrete time slot inside a DailyPlan."""

    task: CareTask
    start_time: str
    end_time: str

    def formatted(self) -> str:
        """e.g., '08:00 - Morning walk (20 min) [high]'."""
        raise NotImplementedError


@dataclass
class DailyPlan:
    """The result the scheduler produces and the UI displays."""

    entries: list[PlanEntry] = field(default_factory=list)
    total_minutes: int = 0
    skipped_tasks: list[CareTask] = field(default_factory=list)
    reasoning: str = ""

    def add_entry(self, task: CareTask, start_time: str) -> None:
        """Place a task at a start time and append it to the plan."""
        raise NotImplementedError

    def summary(self) -> str:
        """Human-readable summary of the plan."""
        raise NotImplementedError

    def to_table(self) -> list:
        """Rows for the Streamlit table display."""
        raise NotImplementedError


class Scheduler:
    """Turns a list of tasks plus constraints into a DailyPlan."""

    def __init__(
        self,
        tasks: list[CareTask] | None = None,
        available_minutes: int = 0,
        preferences: dict | None = None,
    ) -> None:
        self.tasks: list[CareTask] = tasks or []
        self.available_minutes = available_minutes
        self.preferences: dict = preferences or {}

    def add_task(self, task: CareTask) -> None:
        """Add a task to be scheduled."""
        raise NotImplementedError

    def remove_task(self, task: CareTask) -> None:
        """Remove a task from the schedule."""
        raise NotImplementedError

    def sort_tasks(self) -> list[CareTask]:
        """Order tasks by priority, then duration."""
        raise NotImplementedError

    def build_plan(self) -> DailyPlan:
        """Select and order tasks that fit the time budget into a DailyPlan."""
        raise NotImplementedError

    def explain(self) -> str:
        """Describe why tasks were kept or dropped."""
        raise NotImplementedError
