class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_complete = False

    def get_description(self):
        return self.description

    def get_due_date(self):
        return self.due_date

    def is_task_complete(self):
        return self.is_complete

    def mark_as_complete(self):
        self.is_complete = True


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def mark_task_complete(self, task_index):
        if task_index >= 0 and task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.mark_as_complete()
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if task_index >= 0 and task_index < len(self.tasks):
            self.tasks.pop(task_index)
            print("Task removed successfully.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                status = "Complete" if task.is_task_complete() else "Incomplete"
                print(f"{index+1}. {task.get_description()} - Due: {task.get_due_date()} - Status: {status}")


def main():
    todo_list = ToDoList()

    while True:
        print("To-Do List App")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. Remove Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(description, due_date)
            todo_list.add_task(task)

        elif choice == "2":
            task_index = int(input("Enter the index of the task to mark as complete: ")) - 1
            todo_list.mark_task_complete(task_index)

        elif choice == "3":
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(task_index)

        elif choice == "4":
            todo_list.display_tasks()

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
