# № 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 2

# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# n = int(input('chislo'))
# k = int(input('chislo'))

# lst = [i for i in range(1, n + 1)]
# i = 0
# while i < k:
#     lst.insert(0, lst.pop())
#     i += 1
# print(lst)

lst = [1, 2, 3, 4, 5]

k = int(input('sdvig '))

for _ in range(k):
    lst.insert(0, lst.pop())
print(lst)