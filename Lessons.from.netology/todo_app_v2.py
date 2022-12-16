import random

HELP = """
help - print a program guide.
add - add a task to the list (we ask the user for the task name).
show - print all of saved tasks.
exit - stop the bot.
random - add in the list a random task on today date.
"""

tasks = {}
random_tasks = ['Shake your ass', 'Fuck your mom', 'Lake your pussy']

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

run = True

while run:
    command = input("Please, enter the command: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input('Which date to show?: ')
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print('Entered date is missing.')
    elif command == "add":
       date = input('Please, enter the date of task: ')
       task = input('And now enter the name of task: ')
       add_todo(date, task)
       print(f'The task "{task}" is added on "{date}" date.')
    elif command == "exit":
        run = False
        print("Bot is disabled. \nThanks for using me! Goodbye!")
    elif command == "random":
        add_todo('Today', random_tasks)
        task = random.choice(random_tasks)
        print(f'The "{task}" added on Today date')
    else:
        print("Unexpected command.")
        print("Bye!")
        break



