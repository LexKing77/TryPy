
HELP = """
help - напечатать справку о программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []

command = input("Please, enter the command: ")
if command == "help":
    print(HELP)
elif command == "show":
    print(tasks)
elif command == "add":
    task = input("Please, enter the task name: ")
    tasks.append(task)
    print("Task is added")
else:
    print("Unexpected command. \nPlease, try again.")
