from random import randint
from brain_games.cli import welcome_user


def game_even_odd():
    name = welcome_user()
    counts = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for attems in range(3):
        number = randint(0, 100)
        print(f'Question: {number}')
        if number % 2 == 0:
            right_answer = 'yes'
            your_answer = str(input('Your answer: '))
            if your_answer == right_answer:
                counts += 1
                print('Correct')
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name} !")

        elif number != 0:
            right_answer = 'no'
            your_answer = str(input('Your answer: '))
            if your_answer == right_answer:
                counts += 1
                print('Correct')
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name} !")

    if counts == 3:
        print(f'Congratulations, {name}!')
    else:
        print('Try again')



def main():
    game_even_odd()



if __name__ == '__main__':
    main()




