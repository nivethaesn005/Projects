class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed successfully!")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your To-Do List is empty.")

todo_list = ToDoList()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.add_task(task)
    elif choice == '2':
        task_index = int(input("Enter task index to remove: ")) - 1
        todo_list.remove_task(task_index)
    elif choice == '3':
        todo_list.display_tasks()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")