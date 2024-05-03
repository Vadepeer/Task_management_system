class Task:
    def __init__(self, task_id, title, description, priority, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

def add_task(tasks):
    task_id = len(tasks) + 1
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    priority = input("Enter task priority (High/Medium/Low): ")
    status = input("Enter task status (Pending/In Progress/Completed): ")
    tasks.append(Task(task_id, title, description, priority, status))
    print("Task added successfully.")
    print()

def view_all_tasks(tasks):
    for task in tasks:
        print(f"Task ID: {task.task_id}, Title: {task.title}, Description: {task.description}, Priority: {task.priority}, Status: {task.status}")

def edit_task(tasks):
    task_id = int(input("Enter task ID to edit: "))
    for task in tasks:
        if task.task_id == task_id:
            task.title = input("Enter new title (leave blank to keep existing): ") or task.title
            task.description = input("Enter new description (leave blank to keep existing): ") or task.description
            task.priority = input("Enter new priority (leave blank to keep existing): ") or task.priority
            task.status = input("Enter new status (leave blank to keep existing): ") or task.status
            print("Task edited successfully.")
            return
    print("Task not found.")

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("Task deleted successfully.")
            return
    print("Task not found.")

def filter_tasks_by_priority(tasks):
    priority = input("Enter priority to filter tasks (High/Medium/Low): ")
    filtered_tasks = [task for task in tasks if task.priority.lower() == priority.lower()]
    if filtered_tasks:
        view_all_tasks(filtered_tasks)
    else:
        print("No tasks found with the specified priority.")

def main():
    tasks = []
    while True:
        print("\n1. Add Task\n2. Edit Task\n3. Delete Task\n4. View All Tasks\n5. Filter Tasks by Priority\n6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            edit_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            view_all_tasks(tasks)
        elif choice == "5":
            filter_tasks_by_priority(tasks)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":

    main()
