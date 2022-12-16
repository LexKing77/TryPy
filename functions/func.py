# add task in the list
def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

# function of word by some letter count
def count_letter(word_list, letter):
    result = 0
    for word in word_list:
        if letter in word:
            result += 1
    return  result
print(count_letter(['python', 'c++', 'c', 'scala', 'java'], 'c'))