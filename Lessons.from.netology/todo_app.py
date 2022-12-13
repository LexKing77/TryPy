
HELP = """
help - напечатать справку о программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - прекращение работы бота."""

tasks = []
today = []
tomorrow = []
other_days = []

run = True

while run:
    command = input("Please, enter the command: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        list = input('Which list to show?: \n1. Tasks \n2. Today \n3. Tomorrow \n4. Other Days \n')
        if list == "tasks" or "Tasks" or "1":
            print(tasks)
        elif list == "today" or "Today" or "2":
            print(today)
        elif list == "tomorrow" or "Tomorrow" or "3":
            print(tomorrow)
        elif list == "other days" or "Other days" or "4":
            print(other_days)
        else:
            print('Please, enter the one of available lists')
    elif command == "add":
        task = input('Please, enter the task name: ')
        date = input('What date is the task due?: ')
        if date == "today" or "Today":
            today.append(task)
        elif date == "tomorrow" or "Tomorrow":
            tomorrow.append(task)
        else:
            other_days.append(task)
        # tasks.append(task)
        print("Task is added")
    elif command == "exit":
        run = False
        print("Bot is disabled. \nThanks for using me! Goodbye!")
    else:
        print("Unexpected command.")
        print("Bye!")
        break



