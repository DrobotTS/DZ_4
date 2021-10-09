print(
    '1) У вас есть список my_list с значениями типа int.Распечатать те значения, которые больше 100 Задание выполнить с помощью цикла for.')

my_list = [5, 2, 10, 120, 250, 3, 360]
for elements in my_list:
    print(elements) if elements > 100 else my_list.pop(elements)

print(
    '2) У вас есть список my_list с значениями типа int, и пустой список my_results.Добавить в my_results те значения, которые больше 100.Распечатать список my_results.Задание выполнить с помощью цикла for.')

print("1 вариант")

my_list = [5, 2, 10, 120, 250, 3, 360]
my_results = []
for elements in my_list:
    if elements > 100:
        my_results.append(elements)
print(my_results)

print("2 вариант")

from random import randint

my_list = []
my_results = []
for elements in range(10):
    my_list.append(randint(0, 200))
print(f"Your list: {my_list}")
for end in my_list[:]:
    if end > 100:
        my_results.append(end)
print(f"Your result: {my_results}")

print(
    '3) У вас есть список my_list с значениями типа int. Если в my_list количество элементов меньше 2, то в конец добавить значение 0. Если количество элементов больше или равно 2, то добавить сумму последних двух элементов. Количество элементов в списке можно получить с помощью функции len(my_list)')

print("1 вариант")

my_list = [10]
if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
elif len(my_list) < 2:
    my_list.append(0)
print(f"Your list: {my_list}")

print("2 вариант")

from random import randint

n = randint(1, 10)
print(f"List range: {n}")
my_list = []
for elements in range(n):
    print("Enter list element [" "] : ")
    numb = int(input())
    my_list.append(numb)
    print(f"Current length: {len(my_list)}")

if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
elif len(my_list) < 2:
    my_list.append(0)
print(f"Your list: {my_list}")

print(
    '4) У вас есть строка my_string .Сгенерировать ц елые числа (тип int) от 0 до 99 и поместить в список.Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.')

my_string = '0123456789'
my_list = []
for numbers in my_string:
    for elements in my_string:
        my_list.append(int(numbers + elements))
print(my_list)