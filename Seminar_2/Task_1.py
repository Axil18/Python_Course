# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while


# Input:       5

# Output:    120

n = int(input('введите целое число: '))
fact = count = 1

while count <= n:
    fact = fact * count
    print(fact)
    count = count + 1
print(fact)
