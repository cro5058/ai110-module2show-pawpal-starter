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


@dataclass
class Pet:
    name: str


@dataclass
class Task:
    title: str
    petsInvolved: List[Pet]
    duration: float
    startTime: datetime
    endTime: datetime
    priority: Priority


class Owner:
    def __init__(self, name: str, pets: Optional[List[Pet]] = None) -> None:
        self.name = name
        self.pets: List[Pet] = pets if pets is not None else []


class Schedule:
    def __init__(self, owner: Owner, tasks: Optional[List[Task]] = None) -> None:
        self.owner = owner
        self.tasks: List[Task] = tasks if tasks is not None else []

    def addTask(self, newTask: Task) -> None:
        ...

    def removeTask(self, task: Task) -> None:
        ...

    def searchTasks(self, query: str) -> Optional[List[Task]]:
        ...


class Scheduler:
    def sortTasks(self, tasks: List[Task], key: Callable) -> None:
        ...

    def createSchedule(
        self, tasks: List[Task], minutesAvailable: int
    ) -> Tuple[Schedule, str]:
        ...
