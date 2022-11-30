# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
numbers = list(map(int, input('Введите числа через пробела: ').split()))
# ^^^ функция map, которая применяет определенную функцию (в нашем случае int) ко всем элементам списка ^^^
print(numbers)
# print(type(numbers[0]))
summ = 0
for i in range(0, len(numbers)):
    if (i % 2) != 0:
        summ = summ + numbers[i]
        print(f'на нечетных позициях элементы {numbers[i]}')
print(summ)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];  - [2, 3, 5, 6] => [12, 15]
numbers = list(map(int, input('Введите числа через пробел: ').split()))
print(numbers)
res = []
for i in range(0, len(numbers)):
    # print(f'i - {i}')
    # print(type(i))
    lastItem = numbers[len(numbers) - 1]
    index = numbers.index(lastItem) - i
    # print(index)
    # print(type(index))
    if i <= index:
        product = numbers[i] * numbers[index]
        res.append(product)
print(res)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.197
numbers = list(
    map(float, input('Введите вещественные числа через пробел: ').split()))
print(numbers)
drobi = []
for i in range(0, len(numbers)):
    dr = numbers[i] % 1
    drobi.append(dr)
# print(drobi)
maxDrob = drobi[0]
minDrob = drobi[0]
for j in range(0, len(drobi)):
    if drobi[j] > maxDrob:
        maxDrob = drobi[j]
        # print(f'Max {maxDrob}')
for k in range(0, len(drobi)):
    if drobi[k] < minDrob and drobi[k] != 0:
        minDrob = drobi[k]
        # print(f'Min {minDrob}')
difference = maxDrob - minDrob
print(difference)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример:- 45 -> 101101  - 3 -> 11 - 2 -> 10
num = int(input('Введите число: '))
listOst = []
while int(num/2) > 0:
    ost = num % 2
    num = int(num / 2)
    listOst.append(ost)
else:
    ost = 1
    listOst.append(ost)
# print(listOst)
res = []
for i in listOst[::-1]:
    #    print(i)
    res.append(i)
# print(res)
number = res[0]
for d in res[1:]:
    number = 10 * number + d
print(number)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
n = int(input('Введите число: '))


def fib(n):
    a, b = 0, 1
    result = [0, ]
    for i in range(n):
        a, b = b, a + b
        result.append(a)
    return result
# print(fib(n))


def fib1(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        a, b = b, a - b
        result.append(a)
    return result


# print(fib1(n))
# print(list(reversed(fib1(n))))
res = list(reversed(fib1(n))) + fib(n)
print(res)
