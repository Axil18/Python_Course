# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные 
# оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1


import random
n = int(input('Введите количество элементов в массиве: '))
lst = []
for _ in range(n):
    lst.append(random.randint(1, 5))
print(*lst)
minn = lst[0]
maxx = lst[0]
ind_maxx = []
# i = 1
for val in lst:
    if maxx < val:
        maxx = val
    if minn > val:
        minn = val
for i in range(n):
    if maxx == lst[i]:
        ind_maxx.append(i)
    else:
# for i in range(len(ind_maxx)):
        lst[ind_maxx[i]] = minn        
        
print(f'максимальное число: {maxx}')
print(f'максимальный индексы: {ind_maxx}')
print(f'минимальное число: {minn}')
print(*lst)


import random
n = int(input("Введите число "))
arr = [random.randint(1, 5) for x in range(0,n)]
print(arr)
maxx = max(arr)
minn = min(arr)
for i,k in enumerate(arr):
    if k == maxx:
        arr[i] = minn
print(arr)