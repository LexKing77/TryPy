# add task in the list
def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

# function of word by some letter count
def count_letter(word, letter):
    word = []
    list_words = input('Please, enter the list of some words: ')
    word.append(list_words)
    letter = input('Please, enter the letter: ')
