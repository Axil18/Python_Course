import random

n_num = int(input("Введите размер массива: "))
my_array = [random.randint(1, 100) for i in range(n_num)]
print(f" {my_array}")
count = 0
for i in range(1, n_num -1):
    if my_array[i - 1] < my_array[i] > my_array[i + 1]:
        count += 1

print(count)