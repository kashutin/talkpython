import random

print('---------------------------------')
print('           Ванговальня ')
print('---------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('Как звать тебя, дружок? ')

while guess != the_number:
    guess_text = input('Вангуй между 0 и 100: ')
    guess = int(guess_text)

    if guess < the_number:
        # print('Your guess of ' + guess + ' was too LOW.')
        print('Сорян {}, {} это ты МЕЛКОВАТО ванганул.'.format(name, guess))
    elif guess > the_number:
        print('Сорян {}, {} это ты МНОГОВАТО ванганул.'.format(name, guess))
    else:
        print('Отлично наванговал {}, комп таки загадал {}!'.format(name, guess))

    print('Всё давай, досвидания.')

