class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("\n1. Show all tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append(task)
        print("Task added successfully!")

    def update_task(self):
        self.show_tasks()
        task_number = int(input("Enter the task number to update: "))
        if 1 <= task_number <= len(self.tasks):
            new_task = input("Enter the updated task: ")
            self.tasks[task_number - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    def delete_task(self):
        self.show_tasks()
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    while True:
        todo_list.show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            todo_list.show_tasks()
        elif choice == "2":
            todo_list.add_task()
        elif choice == "3":
            todo_list.update_task()
        elif choice == "4":
            todo_list.delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
