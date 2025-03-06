from brain_games.cli import welcome_user
from random import randint


def brain_prime():
    name = welcome_user()
    counts = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for attems in range(3):
        number = randint(0, 100)
        print(f'Quastion: {number}')
        prime_numbers = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,61,67,71,73,83,87,89,91,97]
        if number in prime_numbers:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        your_answer = (input('Your answer: '))
        if right_answer == your_answer:
            counts += 1
            print('Correct!')
        else:
            print(f"{your_answer} is wrong answer ;(. Correct answer was {right_answer}.")
            print('Try again')
    if counts == 3:
        print(f'Congratulations, {name}')
    else:
        print('Try again')


def main():
    brain_prime()


if __name__ == '__main__':
    main()
