# Simple To-Do List Application

# Initialize an empty to-do list
todo_list = []

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter the task to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added successfully.")

def remove_task():
    if not todo_list:
        print("\nYour to-do list is empty. Nothing to remove.")
        return
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                remove_task()
            elif choice == 4:
                print("\nGoodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
