# №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# Output: 6


# Примечание: Пользователь может вводить значения списка или список задан изначально.

import random

lst = [random.randint(-9, 9) for _ in range(10)]

lst_ = []

for item in lst:
    if not item in lst_:          # если не содержаться знаения в новом списке то перемещаем без пвторов
        lst_.append(item)
print(lst)
print(lst_)
print(len(lst_))

