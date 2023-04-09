username = input('Введите ваше имя: ')

x = int(input('Введите трехзначное число: '))
a = int(x//100)
b = int(x/10%10)
c = int(x%10)
if x < 100:
    print(username, 'вы ввели менее 3х чисел!')

elif x >= 1000:
    print(username, 'вы ввели более 3х чисел!')

else:
    print(a+b+c)
