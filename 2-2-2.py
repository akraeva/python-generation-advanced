""" Больше предыдущего

На вход программе подается строка текста из натуральных чисел
Из неё формируется список чисел. Напишите программу подсчета количества чисел,
которые больше предшествующего им в этом списке числа,
то есть, стоят вслед за меньшим числом.

Формат входных данных
На вход программе подается строка текста
из разделенных пробелами натуральных чисел.

Формат выходных данных
Программа должна вывести одно число –
количество элементов списка, больших предыдущего. """

nums = [int(i) for i in input().split()]
res = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        res += 1
print(res)
