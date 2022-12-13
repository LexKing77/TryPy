
HELP = """
help - напечатать справку о программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - прекращение работы бота."""

today = []
tomorrow = []
other_days = []

run = True

while run:
    command = input("Please, enter the command: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print('Today')
        print(today)
        print('Tomorrow')
        print(tomorrow)
        print('Others')
        print(other_days)
    elif command == "add":
        task = input('Please, enter the task name: ')
        date = input('What date is the task due?: ')
        if date == "today" or "Today":
            today.append(task)
        elif date == "tomorrow" or "Tomorrow":
            tomorrow.append(task)
        else:
            other_days.append(task)
        print(f'Task {task} is added on the {date} date')
    elif command == "exit":
        run = False
        print("Bot is disabled. \nThanks for using me! Goodbye!")
    else:
        print("Unexpected command.")
        print("Bye!")
        break



