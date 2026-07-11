from datetime import datetime

from pawpal_system import (
    Priority, 
    CompletionStatus, 
    Pet, 
    Task, 
    Owner, 
    Schedule, 
    Scheduler
)


def main():
    # Create an Owner
    o = Owner('owner1', [])

    # Create at least 2 Pets
    p1 = Pet('pet1', [])
    p2 = Pet('pet2', [])
    
    # Add at least 3 Tasks with different times to those Pets
    t1 = Task('Morning walk', datetime(2026, 7, 11, 7, 0), datetime(2026, 7, 11, 7, 30), Priority.HIGH)
    t2 = Task('Breakfast', datetime(2026, 7, 11, 8, 0), datetime(2026, 7, 11, 8, 15), Priority.MEDIUM)
    t3 = Task('Vet appointment', datetime(2026, 7, 11, 10, 0), datetime(2026, 7, 11, 11, 0), Priority.HIGH)
    t4 = Task('Playtime', datetime(2026, 7, 11, 12, 0), datetime(2026, 7, 11, 12, 45), Priority.LOW)
    t5 = Task('Grooming', datetime(2026, 7, 11, 14, 0), datetime(2026, 7, 11, 14, 30), Priority.MEDIUM)
    t6 = Task('Evening walk', datetime(2026, 7, 11, 18, 0), datetime(2026, 7, 11, 18, 30), Priority.HIGH)

    p1.addTask(t1)
    p1.addTask(t2)
    p1.addTask(t3)

    p2.addTask(t4)
    p2.addTask(t5)
    p2.addTask(t6)

    # Add the pets to the Owner
    o.addPet(p1)
    o.addPet(p2)

    # Create a schedule for the day
    scheduler = Scheduler()
    schedule = scheduler.createSchedule(tasks=o.allTasks, 
                                        minutesAvailable=(24 * 60))

    # Print a "Today's Schedule" to the terminal
    print(schedule)


if __name__ == "__main__":
    main()