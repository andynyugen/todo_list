import csv
from datetime import datetime

def print_title(star):
    print(star * 50)
    title = "TASK LIST"
    centered_title = title.center(50)
    print(centered_title)
    print(star * 50)

def view_tasks(star, tasks):
    print("\n") # For cleanliness
    # Print task list title
    print_title(star)

    # Read tasks from file
    with open("task.txt", "r") as file:
        tasks = [line.strip() for line in file]

    # Display current tasks
    for i, task in enumerate(tasks, start=1): 
            print(f"{i}. {task}")

    input("\nEnter 'return' key to return to menu ")
    print("\n")
    return

def add_task(star, tasks):
    print("\nWhat task you like to add?")
    task = input("Task: ")

    # Read tasks from file
    with open("task.txt", "a") as file:
        file.write(f"{task}\n")

    # Display current tasks
    print(f"\n{task} has been added to the To-Do List\n")

    input("Enter 'return' key to return to menu ")
    return

def delete_task(star, tasks):
    print("\n") # For cleanliness
    # Print task list title
    print_title(star)

    # Read tasks from file
    with open("task.txt", "r") as file:
        tasks = [line.strip() for line in file]

    # Display current tasks
    for i, task in enumerate(tasks, start=1): 
            print(f"{i}. {task}")

    while (True):
        print("\nWhat task would you like to remove?")
        # Handle invalid integer input
        try:
            task_int = int(input("Enter number: ")) - 1 # Subtract 1 because index 0
        except ValueError: 
            # Ask user for input again
            print("ERROR: Invalid number. Please try again")
            continue
        
        # Check that user number is within valid range
        if 0 <= task_int < len(tasks):
            task_to_remove = tasks[task_int]
            print(f"\nAre you sure you want to remove Task #{task_int + 1}: '{tasks[task_int]}'?")
            print("* Removing a task will permanently delete it from the To-Do List *")
            while (True):
                user_confirm = input("Enter Y/N: ")
                if user_confirm == "Y":
                    # Rewrite the task file without the deleted task
                    with open("task.txt", "w") as file:
                        for i, task in enumerate(tasks):
                            if i != task_int:  # Skip the task to be removed
                                file.write(f"{task}\n")
                    print(f"\n{task_to_remove} has been removed from the To-Do List\n")
                    break
                elif user_confirm == "N":
                    print("Task removal was canceled.\n")
                    break
                else:
                    print("ERROR: Invalid task number. Please try again")
                    continue
            break # Break out of the task removal loop
        else: 
            # Reprompt user
            print("ERROR: Invalid number. Please try again")
            continue
    return


def complete_task(star, tasks):
    # Print task list title
    print_title(star)

    # Read tasks from file
    with open("task.txt", "r") as file:
        tasks = [line.strip() for line in file]

    # Display current tasks
    for i, task in enumerate(tasks, start=1): 
            print(f"{i}. {task}")

    while (True):
        print("\nWhat task would you like to mark as complete?")
        # Handle invalid integer input
        try:
            task_int = int(input("Enter number: ")) - 1 # Subtract 1 because index 0
        except ValueError: 
            # Ask user for input again
            print("ERROR: Invalid number. Please try again")
            continue

        # Check that user number is within valid range
        if 0 <= task_int < len(tasks):
            task_to_complete= tasks[task_int]
            print(f"\nAre you sure you want to mark Task #{task_int + 1}: '{task_to_complete}' as complete?")
            print("* Marking a task as complete will add '(Completed)' to the task *")

            while (True):
                user_confirm = input("Enter Y/N: ")
                if user_confirm == "Y":
                     # Mark task as complete by appending "(Completed)"
                    tasks[task_int] = f"{task_to_complete} (Completed)"

                    # Rewrite the task file with the updated task list
                    with open("task.txt", "w") as file:
                        for task in tasks:
                                file.write(f"{task}\n")

                    print(f"\n'{task_to_complete}' has been marked as complete!\n")
                    break
                elif user_confirm == "N":
                    print("Task marking as complete was canceled.\n")
                    break
                else:
                    print("ERROR: Invalid task number. Please try again")
                    continue
            break # Break out of the task marking loop
        else: 
            # Reprompt user
            print("ERROR: Invalid number. Please try again")
            continue
    return

def help_menu(star):
    print("\n") # For cleanliness
    # Print help title
    print(star * 50)
    title = "HELP"
    centered_title = title.center(50)
    print(centered_title)
    print(star * 50)

    print("\nTo view tasks: Enter '1' at the menu\n")
    print("To add task: Enter '2' at the menu and enter task\n")
    print("To remove task: Enter '3' at the menu and enter Task # to remove\n")
    print("To mark task as complete: Enter '4' at the menu and enter Task # to mark off\n")
    print("Questions? Email nguyea28@oregonstate.edu\n")

    input("Enter 'return' key to return to menu ")
    return

def main():
    # Create task list
    tasks = []
    while (True):
        # Print title
        star = "*"
        print(star * 50)
        title = "TO-DO LIST"
        centered_title = title.center(50)
        print(centered_title)

        # Print time
        current_time = datetime.now().strftime("%I:%M %p")
        time = "Time: " + current_time
        centered_time = time.center(50)
        print(centered_time)
        print(star * 50)

        # Print options
        print("Manage your personal To-Do List!")
        print("Commands:")
        print("  Enter '1' to View Tasks")
        print("  Enter '2' to Add Task")
        print("  Enter '3' to Remove Task")
        print("  Enter '4' to Mark Task as Complete")
        print("  Enter '5' to navigate to Help")
        print("  Enter 'Q' or 'q' to Exit Program")
        # Prompt user for int
        print("\nWhat would you like to do?")
        option = (input("Enter input: "))

        # Option 1: View Tasks
        if option == "1":
            view_tasks(star, tasks)
        # Option 2: Add Task
        elif option == "2":
            add_task(star, tasks)
        # Option 3: Remove Task
        elif option == "3":
            delete_task(star, tasks)
        # Option 4: Mark Task as Complete
        elif option == "4":
            complete_task(star, tasks)
        # Option 5: Help
        elif option == "5":
            help_menu(star)
        # Option 6: Quit
        elif option == "Q" or option == "q":
            print("\nGoodbye!")
            break
        else:
            print("ERROR: Invalid number. Please try again")
            continue

if __name__ == "__main__":
    main()