# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.



list = list(map(int, input("Введите числа через пробел:\n").split()))
# list1 = [i for i in list if i != list1]

list1 = []
for i in list:
    if i not in list1:
        list1.append(i)

print(list1)

