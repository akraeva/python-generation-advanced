from random import sample


def generate_password(cnt, abc):
    if cnt == 0 or len(abc) == 0:
        return 'ОШИБКА'
    if len(abc) < cnt:
        abc *= (cnt // len(abc) + 1)
    return ''.join(sample(abc, cnt))


DIGITS = '0123456789'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''

count = int(input('Количество паролей для генерации: '))
length = int(input('Длинa одного пароля: '))
if input('Включать ли цифры 0123456789? (да / нет): ').lower() in ('да', 'lf'):
    chars += DIGITS    
if input('Включать ли цифры ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да / нет): ').lower() in ('да', 'lf'):
    chars += UPPER_LETTERS
if input('Включать ли цифры abcdefghijklmnopqrstuvwxyz? (да / нет): ').lower() in ('да', 'lf'):
    chars += LOWER_LETTERS
if input('Включать ли символы !#$%&*+-=?@^_? (да / нет): ').lower() in ('да', 'lf'):
    chars += PUNCTUATION
if input('Исключать ли неоднозначные символы il1Lo0O? (да / нет): ').lower() in ('да', 'lf'):
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

for i in range(count):
    print(generate_password(length, chars))

