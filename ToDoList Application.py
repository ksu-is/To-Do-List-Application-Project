# For reference I used aosojkic's Github Repository as well as a Youtube video tutorial.
# Code Change 1: Rewrite The To Do List Menu by adding more options
def show_menu():
    print("----To-Do-List Application----")
    print("1. View To-Do-List ")
    print("2. Add Task ")
    print("3. Delete a Task ")
    print("4. Set a Reminder ")
    print("5. View Reminders ")
    print("6. Mark Task as complete ")
    print("7. Set a deadline ")
    print("8. View Deadlines")
    print("9. View Completed Tasks")
    print("10. Exit")
# The list where the tasks, reminders, Competed Tasks and Deadlines are stored
tasks = []
reminders = []
completedtasks = []
deadlines = []

# Here is the function for viewing the Tasks
def task_view():
    if len(tasks) == 0:
        print("Your to-do list is empty")
    else:
        print("list of tasks:")
        for i, task in enumerate(tasks):
            print(str(i) + "." + task)

# This is where we Adding Task
def add_task():
    task = input("Enter a new Task: ")
    tasks.append(task)
    print("Task has been added successfully ")  


deadline_input = input("Enter th")

# The User has the ability to mark a task as complete
def complete_task():
    completedtask = input( "Enter The number for the task that you want to complete. ")
    completedtasks.append(completedtasks)
    print("Task is complete:" + completedtasks)


# Code Change 2: Here is where you can view the tasks that you have completed 
def view_completedTasks():
    if len(completedtasks) == 0:
        print("Your Completed Tasks list is empty ")
    else:
        print("These are all the tasks that you have completed: ")
        for i, reminder in enumerate(reminders):
            print(str(i) + "." + reminder)

# When the Task is complete we remove it from the task list    
def delete_tasks():
    if len(tasks) == 0:
        print("there are no tasks to delete. ")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(str(i) + "." + task)
        choice = int(input("Enter the task that you want to delete:"))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task is deleted")
        else:
            print("Invalid Task number")


# Code Change 3: Here is where The User can set reminders for the tasks       
def set_reminder():
    task_number = int(input("Enter the number of the task you want to set a reminder for: "))
    if 1 <= task_number <= len(tasks):
        reminder = input("Enter a new Reminder: ")
        reminders.append((tasks[task_number - 1], reminder))

    
# Code Change 4: here is where The user can view the reminders
def view_reminders():
    if len(reminders) == 0:
        print("Your Reminder list is empty")
    else:
        print("list of Reminders:")
        for i, reminder in enumerate(reminders):
            print(str(i) + "." + reminder)

# Code Change 5: Here is where you add Deadlines to a Task
def add_deadline():
        task_number = int(input("Enter the number if the task you want to set a deadline for"))
        print(tasks)
        if 1 <= task_number <= len(tasks):
            deadline = input("Enter a new Deadline: ")
            deadlines.append((tasks[task_number - 1], deadline))
            print("deadline set. ")
        else:
            print("Invalid Task number.")

# Code Change 6: This is where you can view your deadlines for your tasks. 
def view_deadlines():
    if len(deadlines) == 0:
        print("Your deadline list is empty")
    else:
        print("list of deadline:")
        for i, (task, deadline) in enumerate(deadlines, start=1):
            print(str(i) + ".Task" + task +" have this task done by: " + deadline)

def main():
    while True:
        show_menu()

       # These are The menu options, where you can select what you want to do
        choice = input("Enter a your choice 1-10: ")
        if choice == "1":
            task_view()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_tasks()
        elif choice == "4":
            set_reminder()
        elif choice == "5":
            view_reminders()
        elif choice == "6":
            complete_task()
        elif choice == "7":
            add_deadline()
        elif choice == "8":
            view_deadlines()
        elif choice == "9":
            view_completedTasks()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10")


if __name__ == "__main__":
    main()    



   


