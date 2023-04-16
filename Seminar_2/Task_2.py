# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите 
# число -1.

# Input:     5

# Output:  6

num = int(input('Введите число: '))

fib1, fib2 = 0, 1
count = 1

while fib1 < num:
    fib1, fib2 = fib2, fib1 + fib2
    count += 1
if fib1 == num:
    print(count)
else:
    print('-1')



