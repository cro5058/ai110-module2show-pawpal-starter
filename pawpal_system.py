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


@dataclass
class Task:
    title: str
    petsInvolved: List[Pet]
    duration: float
    startTime: datetime
    endTime: datetime
    priority: Priority
    completion_status: CompletionStatus


class Owner:
    def __init__(self, name: str, pets: Optional[List[Pet]] = None) -> None:
        self.name = name
        self.pets: List[Pet] = pets if pets is not None else []


class Scheduler:
    def sortTasks(self, tasks: List[Task], key: Callable) -> None:
        ...

    def createSchedule(
        self, tasks: List[Task], minutesAvailable: int
    ) -> Tuple[Schedule, str]:
        ...
