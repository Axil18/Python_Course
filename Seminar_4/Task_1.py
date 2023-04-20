# №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый 
# символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

# stroka = input('vvedite stroku: ').split()

# dic = {}

# for i in stroka:
#     dic[i] = 0
# spis = []
# for i in stroka:
#     if dic[i] == 0:
#         spis.append(i)
#         dic[i] +=1
#     else:
#         spis.append(f'{i}_{dic[i]}')
#         dic[i] +=1
# print(spis)



text = input('Введите строку: ').split()

count = {}

for letter in text:
    if letter not in count: 
        print(f'{letter}', end=" ")
    else: 
        print(f'{letter}_{count[letter]}', end=" ")

    count[letter] = count.get(letter, 0) + 1