# ; 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# ; Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов
# ; слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# ; Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных
# ; на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# ; Input:	5 -> 5 1 6 5 9
# ; Output:	1 9

import random
n = int(input('kolvo arb'))
min = 20
max = 1

for _ in range(n):
    arb = random.randint(1, 20)
    print(arb)
    if arb < min:
        min = arb
    if arb > max:
        max = arb
print(min, max)