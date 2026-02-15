FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!")
    else:
        print("❌ Task cannot be empty")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to remove: ")) - 1
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print(f"🗑 Removed: {removed}")
    except (ValueError, IndexError):
        print("❌ Invalid task number")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Bye 👋")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
