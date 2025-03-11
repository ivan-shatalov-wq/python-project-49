from random import randint
from brain_games.cli import welcome_user
from random import choice


def brain_progression():
    name = welcome_user()
    counts = 0
    print('What number is missing in the progression?')
    for attems in range(3):
        result = []
        num = randint(0,100)
        step = randint(1,6)
        for elem in range(10):
            num += step
            result.append(num)
        quastion_elem = choice(result)
        right_answer = quastion_elem
        question_elem_index = result.index(quastion_elem)  # метод списков .index() позволяет найти индекс элемента
        result[question_elem_index] = '..'
        print(f'Question: {result}')
        your_answer = int(input('Your answer: '))
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
    brain_progression()


if __name__ == '__main__':
    main()
