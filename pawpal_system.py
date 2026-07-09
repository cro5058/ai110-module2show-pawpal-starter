"""PawPal+ — pet care task scheduling system."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Callable, List, Optional, Tuple


class Priority(Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class CompletionStatus(Enum):
    NOT_STARTED = "NOT STARTED"
    IN_PROGRESS = "IN PROGRESS"
    DONE = "DONE"


@dataclass
class Pet:
    name: str
    tasks: List[Task]

    def __str__(self) -> str:
        return "Pet: " + self.name


@dataclass
class Task:
    title: str
    duration: float
    startTime: datetime
    endTime: datetime
    priority: Priority
    completion_status: CompletionStatus = CompletionStatus.NOT_STARTED

    def markInProgress(self) -> None:
        self.completion_status = CompletionStatus.IN_PROGRESS

    def markDone(self) -> None:
        self.completion_status = CompletionStatus.DONE

    def isDone(self) -> bool:
        return self.completion_status is CompletionStatus.DONE

    def __str__(self) -> str:
        return (
            f"Task {self.title} [{self.priority.value}] "
            f"(Estimated duration {self.duration}) — {self.completion_status.value}"
        )


class Owner:
    def __init__(self, name: str, pets: Optional[List[Pet]] = None) -> None:
        self.name = name
        self.pets: List[Pet] = pets if pets is not None else []

    def addPet(self, pet: Pet) -> None:
        if pet not in self.pets:
            self.pets.append(pet)

    def removePet(self, pet: Pet) -> None:
        if pet in self.pets:
            self.pets.remove(pet)

    def allTasks(self) -> List[Task]:
        """Gather every task across all of this owner's pets."""
        return [task for pet in self.pets for task in pet.tasks]

    def __str__(self) -> str:
        pets = ", ".join(str(pet) for pet in self.pets) or "no pets"
        return f"Owner {self.name} (pets: {pets})"


class Schedule:
    def __init__(self, owner: Owner, tasks: Optional[List[Task]] = None) -> None:
        self.owner = owner
        self.tasks: List[Task] = tasks if tasks is not None else []

    def addTask(self, newTask: Task) -> None:
        self.tasks.append(newTask)

    def removeTask(self, task: Task) -> None:
        if task in self.tasks:
            self.tasks.remove(task)

    def searchTasks(self, query: str) -> Optional[List[Task]]:
        needle = query.strip().lower()
        if not needle:
            return None
        matches = [task for task in self.tasks if needle in task.title.lower()]
        return matches or None

    def totalDuration(self) -> float:
        return sum(task.duration for task in self.tasks)

    def __str__(self) -> str:
        if not self.tasks:
            return f"Schedule for {self.owner.name}: (empty)"
        lines = [f"Schedule for {self.owner.name}:"]
        lines.extend(f"  - {task}" for task in self.tasks)
        return "\n".join(lines)


class Scheduler:
    def sortTasks(self, tasks: List[Task], key: Callable) -> None:
        """Sort tasks in place by the given key function."""
        tasks.sort(key=key)

    def createSchedule(
        self, tasks: List[Task], minutesAvailable: int
    ) -> Tuple[Schedule, str]:
        """Greedily pack the highest-priority tasks that fit in the time budget.

        Returns the built schedule and a human-readable summary message.
        """
        priority_rank = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}

        # Highest priority first, then shortest task to fit more in.
        ordered = sorted(
            tasks,
            key=lambda task: (priority_rank[task.priority], task.duration),
        )

        schedule = Schedule(owner=Owner("Unassigned"))
        remaining = minutesAvailable
        skipped: List[Task] = []

        for task in ordered:
            if task.duration <= remaining:
                schedule.addTask(task)
                remaining -= task.duration
            else:
                skipped.append(task)

        message = (
            f"Scheduled {len(schedule.tasks)} of {len(tasks)} task(s); "
            f"{remaining} of {minutesAvailable} minute(s) unused."
        )
        if skipped:
            message += f" Skipped {len(skipped)} task(s) that did not fit."

        return schedule, message
