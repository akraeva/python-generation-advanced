""" Камень, ножницы, бумага, ящерица, Спок

Проиграв 10 раз Тимуру, Руслан понял, что так дело дальше не пойдет,
и решил усложнить игру. Теперь Тимур и Руслан играют в игру
Камень, ножницы, бумага, ящерица, Спок.
Помогите ребятам вновь бросить честный жребий и определить,
кто будет делать следующий модуль в новом курсе.

Формат входных данных
На вход программе подаются две строки текста, содержащие по одному слову и
з перечня "камень", "ножницы", "бумага", "ящерица" или "Спок".
На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки:
кто победил - Тимур или Руслан, или они сыграли вничью.

Примечание. Правила игры стандартные:
ножницы режут бумагу. Бумага заворачивает камень.
Камень давит ящерицу, а ящерица травит Спока,
в то время как Спок ломает ножницы, которые,
в свою очередь, отрезают голову ящерице, которая ест бумагу,
на которой улики против Спока. Спок испаряет камень,
а камень, разумеется, затупляет ножницы."""


res = {
    'камень': ('ножницы', 'ящерица'),
    'ножницы': ('ящерица', 'бумага'),
    'бумага': ('камень', 'Спок'),
    'ящерица': ('Спок', 'бумага'),
    'Спок': ('ножницы', 'камень'),
}
t, r = input(), input()
print('ничья' if t == r else 'Тимур' if r in res.get(t) else 'Руслан')
