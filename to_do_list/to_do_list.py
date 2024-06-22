from colorama import init, Fore, Style
import os

init(autoreset=True)

FILE_NAME = "todo_list.txt"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = file.read().splitlines()
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_menu():
    print(Fore.GREEN + "==============================")
    print("      To-Do List Menu:")
    print("==============================")
    print("1. " + Fore.YELLOW + "Add a task")
    print("2. " + Fore.YELLOW + "View tasks")
    print("3. " + Fore.YELLOW + "Delete a task")
    print("4. " + Fore.RED + "Exit")
    print("==============================")

def add_task(tasks):
    print("\n" + Fore.GREEN + "Adding a Task")
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(Fore.GREEN + f"Task '{task}' added.")

def view_tasks(tasks):
    print("\n" + Fore.GREEN + "To-Do List:")
    if not tasks:
        print(Fore.YELLOW + "No tasks found.")
    for idx, task in enumerate(tasks, start=1):
        print(Fore.YELLOW + f"{idx}. {task}")

def delete_task(tasks):
    print("\n" + Fore.GREEN + "Deleting a Task")
    view_tasks(tasks)
    task_num = input(Fore.YELLOW + "Enter the task number to delete (0 to cancel): ")
    if task_num.isdigit():
        task_num = int(task_num)
        if 1 <= task_num <= len(tasks):
            task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(Fore.GREEN + f"Task '{task}' deleted.")
        elif task_num == 0:
            print(Fore.RED + "Delete operation cancelled.")
        else:
            print(Fore.RED + "Invalid task number.")
    else:
        print(Fore.RED + "Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input(Fore.CYAN + "Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print(Fore.RED + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")

if __name__ == "__main__":
    main()
