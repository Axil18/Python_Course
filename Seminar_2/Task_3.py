import random

n = int(input('obsheee kolvo rasmatrivat dnei'))
count = 0
res = 0
for i in range(n):
    temp = random.randint(-50, 50)
    print(temp, end=" ")
    if temp > 0:
        count += 1
    else:
        count = 0
    if count > res:
        res = count
print(f'\n {res}')
