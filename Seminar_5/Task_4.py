# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту
# последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

import random


def rev(n):
    if n == 0:
        return " ! "
    x = random.randrange(n)
    print(x, end=" ")
    return rev(n - 1) + " " + str(x)
print(rev(5))