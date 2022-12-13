
example = "4*100-54"
answer = 346

print(f'Hello! \nLets try to solve an example: \n{example}')

solve = int(input("Please, enter your answer: "))
if solve != answer:
    print("Answer is not correct. Please, try again!")
else:
    print("Congratulations! \nYour answer is right!")
