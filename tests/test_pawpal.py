"""Tests for pawpal_system."""

from datetime import datetime

from pawpal_system import CompletionStatus, Pet, Priority, Task


def make_task() -> Task:
    return Task(
        title="Walk the dog",
        startTime=datetime(2026, 7, 11, 9, 0),
        endTime=datetime(2026, 7, 11, 9, 30),
        priority=Priority.MEDIUM,
    )


def test_mark_done_changes_status():
    task = make_task()

    # Sanity check: task starts out not completed.
    assert task.completion_status is CompletionStatus.NOT_STARTED
    assert task.isDone() is False

    task.markDone()

    # Marking the task done must actually flip its status.
    assert task.completion_status is CompletionStatus.DONE
    assert task.isDone() is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Rex")

    # A new pet starts with no tasks.
    assert len(pet.tasks) == 0

    pet.addTask(make_task())

    # Adding a task must increase the pet's task count.
    assert len(pet.tasks) == 1

    second = make_task()
    second.title = "Feed the dog"
    pet.addTask(second)
    assert len(pet.tasks) == 2
