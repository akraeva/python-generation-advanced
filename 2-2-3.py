""" Назад, вперёд и наоборот

На вход программе подается строка текста из натуральных чисел.
Из элементов строки формируется список чисел. Напишите программу,
которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3]).
Если в списке нечетное количество элементов,
то последний остается на своем месте.

Формат входных данных
На вход программе подается строка текста,
содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести измененный список,
разделяя его элементы одним пробелом. """

nums = [i for i in input().split()]
for i in range(1, len(nums), 2):
    nums[i], nums[i-1] = nums[i-1], nums[i]
print(' '.join(nums))
