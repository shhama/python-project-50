import prompt
import random


def calc_games():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(f'What is the result of the expression?')
    count = 0
    while count < 3:
        operand_frst = random.randint(0, 10)
        operand_scnd = random.randint(0, 10)
        operator = ["+", "-", "*"]
        rand_op = random.choice(operator)
        expression = f'{operand_frst} {rand_op} {operand_scnd}'
        dict = {
            "+": operand_frst + operand_scnd,
            "-": operand_frst - operand_scnd,
            "*": operand_frst * operand_scnd
        }
        correct_answ = dict[rand_op]
        print(f'Question: {expression}')
        your_answ = prompt.string("Your answer: ")
        if int(your_answ) == (correct_answ):
            print("Correct!")
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'''"{your_answ}" is wrong answer ;(. Correct answer was "{correct_answ}". \nLet's try again, {name}!''')
            break


