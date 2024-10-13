from random import randint


def is_valid(s, max_s):
    return s.isdigit() and 0 < int(s) < max_s + 1


def game():
    max_n = int(input('Какое самое большое число будет в игре? '))
    num = randint(1, max_n)
    trys = 0

    while True:
        input_n = input('Введите число: ')
        if is_valid(input_n, max_n):
            n = int(input_n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        trys += 1
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print(f'Вам потребовал{"a" if trys % 10 == 1 else "o"}сь {trys} попыт{"кa" if trys%10 == 1 else "ки" if trys % 10 < 5 else "ок"}.')
            break


print('Добро пожаловать в числовую угадайку\n')
anser = ''
while anser != 'нет':
    game()
    anser = input('Сыграем еще раз? (да/нет)\n')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
