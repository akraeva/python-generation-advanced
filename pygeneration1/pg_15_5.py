def caesar_cipher(str, s, lang):
    UPPER_ABC = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' if lang == 'ru' else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER_ABC = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' if lang == 'ru' else 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for c in str:
        if c in UPPER_ABC:
            i = (UPPER_ABC.index(c) + s) % len(UPPER_ABC)
            res += UPPER_ABC[i]
        elif c in LOWER_ABC:
            i = (LOWER_ABC.index(c) + s) % len(LOWER_ABC)
            res += LOWER_ABC[i]
        else:
            res += c
    return res

#1
text = 'Блажен, кто верует, тепло ему на свете!'
shift = 10

print(caesar_cipher(text, shift, 'ru'))

#2
text = 'To be, or not to be, that is the question!'
shift = 17

print(caesar_cipher(text, shift, 'en'))

3
text = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
shift = -7

print(caesar_cipher(text, shift, 'ru'))

#4
text = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
shift = -25

print(caesar_cipher(text, shift, 'en'))

#5
text = 'Hawnj pk swhg xabkna ukq nqj.'

for i in range(1,25):
    print(caesar_cipher(text, i, 'en'))

#6
text = ('Day, mice. "Year" is a mistake!').split()
res = [caesar_cipher(w, len([True for i in w if i.isalpha()]), 'en') for w in text]
print(' '.join(res))
