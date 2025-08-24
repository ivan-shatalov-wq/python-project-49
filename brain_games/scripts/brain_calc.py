from random import randint
from brain_games.cli import welcome_user
from random import choice


def calculator():
    name = welcome_user()
    counts = 0
    operators = ['+', '-', '*']
    print('What is the result of the expression?')
    for attems in range(3):
        first_num = randint(0, 100)
        second_num = randint(0, 100)
        random_operator = choice(operators)
        print(f'Question: {first_num} {random_operator} {second_num} ')
        if random_operator == '+':
            right_answer = first_num + second_num
            your_answer = int(input('Your answer: '))
            if right_answer == your_answer:
                counts += 1
                print('Correct!')
            else:
                print(f"{your_answer} is wrong answer ;(. Correct answer was {right_answer}.")
                print('Try again')


        elif random_operator == '*':
            right_answer = first_num * second_num
            your_answer = int(input('Your answer: '))
            if right_answer == your_answer:
                counts += 1
                print('Correct!')
            else:
                print(f"{your_answer} is wrong answer ;(. Correct answer was {right_answer}.")
                print('Try again')
                break


        elif random_operator == '-':
            right_answer = first_num - second_num
            your_answer = int(input('Your answer: '))
            if right_answer == your_answer:
                counts += 1
                print('Correct!')
            else:
                print(f"{your_answer} is wrong answer ;(. Correct answer was {right_answer}.")
                print('Try again')
                break

    if counts == 3:
        print(f'Congratulations, {name}!')
    else:
        print('Try again')


def main():
    calculator()


if __name__ == '__main__':
    main()
