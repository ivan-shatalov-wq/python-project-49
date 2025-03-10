from brain_games.cli import welcome_user
from random import randint


def brain_prime():
    name = welcome_user()
    counts = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for attems in range(3):
        number = randint(0, 100)
        print(f'Question: {number}')

        def is_prime(number):
            if number <= 1:
                return False
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    return False
            return True
        if is_prime(number):
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
