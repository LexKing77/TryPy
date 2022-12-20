import telebot
import random

TOKEN = "5863966426:AAHyn1waL4OJoN2REAU2bg4OsB8JYYND00A"

bot = telebot.TeleBot(TOKEN)

tasks = {}
random_tasks = ['Shake your ass', 'Fuck your mom', 'Lake your pussy']

HELP = """
/help - print a program guide.
/add - add a task to the list (we ask the user for the task name).
/show - print all of saved tasks.
/exit - stop the bot.
/random - add in the list a random task on today date.
"""

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = f'Task "{task}" added on the date "{date}"'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "today"
    task = random.choice(random_tasks)
    add_todo(date, task)
    text = f'Task "{task}" added on the date "{date}"'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    date = message.text.split()[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Task list is empty on this date"
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)