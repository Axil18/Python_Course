# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, 
# что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод:			Вывод:
# 1 2 3 2 3			2

import random 
n_num = int(input("Введите размер массива: "))
my_array = [random.randint(1, 10) for i in range(n_num)]
print(my_array)
counter = 0
for i in range(len(my_array )):
    for j in range(i + 1, len(my_array )):
        if my_array [i] == my_array [j]:
            counter += 1
print(counter)