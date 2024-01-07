class ToDoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_task(self):
        if not self.tasks:
            print('No tasks in the to do list')

        else:
            print('tasks: ')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task} ')

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            print("deleting task----")
            task_name = self.tasks.pop(task_index - 1)
            print(f'{task_name} deleted successfully')
        else:
            print(f'{task_index}. not a valid task to delete')

    def save_tasks_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def load_tasks_from_file(self, filename="tasks.txt"):
        try:
            with open(filename, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("No saved tasks found")

    def user_interface(self):
        while True:
            print("\n1. View Tasks\n2. Add Tasks\n3. Delete Tasks\n4. Save Tasks\n5. Load Tasks\n0. Exit")
            choice = input("Enter your choice ..")

            if choice == "0":
                print("Exiting the to do list app!! GoodBye")
                break
            elif choice == "1":
                self.view_task()
            elif choice == "2":
                task = input("please enter task :")
                self.add_task(task)
                print(f"Task {task} added successfully")
            elif choice == "3":
                index = int(input("please enter the task index to delete"))
                self.delete_task(index)
            elif choice == "4":
                self.save_tasks_to_file()
                print("Tasks saved to the file")
            elif choice == "5":
                self.load_tasks_from_file()
                print("Task loaded from the file")
            else:
                print("Invalid choice. Please try gain")


if __name__ == "__main__":
    to_do_list = ToDoList()

    to_do_list.add_task("Create Python Project")
    to_do_list.add_task("Push to github")
    to_do_list.add_task("Run in docker")
    to_do_list.view_task()

    # to_do_list.user_interface()


