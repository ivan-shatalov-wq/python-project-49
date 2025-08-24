from brain_games.cli import welcome_user
from random import randint


def brain_gcd():
    name = welcome_user()
    counts = 0
    print("Find the greatest common divisor of given numbers.")
    for attems in range(3):
        first_num = randint(0, 100)
        second_num = randint(0, 100)
        print(f'Question: {first_num} {second_num}')
        while first_num != 0 and second_num != 0:
            if first_num > second_num:
                first_num = first_num % second_num
            else:
                second_num = second_num % first_num
        right_answer = first_num + second_num
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



def main():
    brain_gcd()


if __name__ == '__main__':
    main()
