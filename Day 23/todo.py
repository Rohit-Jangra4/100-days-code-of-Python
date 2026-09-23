def add_task(tasks, task):
    tasks.append(task)


def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)


def show_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def main():
    tasks = []

    add_task(tasks, "Learn Python")
    add_task(tasks, "Practice modules")
    add_task(tasks, "Build project")

    print("My Tasks:")
    show_tasks(tasks)

    remove_task(tasks, "Practice modules")

    print("\nAfter removing task:")
    show_tasks(tasks)


if __name__ == "__main__":
    main()