import random
count = 0
lst = [random.randint(-9, 9) for i in range(5)]
i = 1
print(lst)
for i in range(1, len(lst)):
    if lst[i - 1] < lst[i]:
        count += 1
        print(count)
