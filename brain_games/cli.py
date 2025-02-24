def welcome_user():
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
        print ('Hello,'+ name + '!')