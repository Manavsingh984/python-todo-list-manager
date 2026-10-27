# Personal To-Do List Manager

tasks = []
try:
    with open("todo_tasks.txt", "r") as file:
        content = file.read()
        tasks = content.splitlines()

except FileNotFoundError:
    pass

def save_tasks():
    with open("todo_tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

while True:
    print("\n========== TO-DO LIST MANAGER ==========")

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
            new_task = input("Enter a new task: ")
            tasks.append(new_task)
            save_tasks()

            print("Successfully added!")

    elif choice == "2":
        if tasks == []:
            print("No Tasks are here!")
        else:
            print("\nYour Tasks:")
            for number, task in enumerate(tasks, start=1):
                print(number, ".", task)

    
    elif choice == "3":
        try:
            index = int(input("Enter task number: ")) - 1
        except ValueError:
            print("Please enter a valid number!")
            continue

        if 0 <= index < len(tasks):
            if tasks[index].startswith("[Done] "):
                print("This task is already completed!")
            else:
                tasks[index] = "[Done] " + tasks[index]
                save_tasks()
                print("Task marked as completed!")
        else:
            print("Invalid task number!")

    
    
    elif choice == "4":
        try:
            index = int(input("Enter a task to be deleted: ")) - 1
        except ValueError:
            print("Please enter a valid number!")
            continue

        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks()
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")
            

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")
