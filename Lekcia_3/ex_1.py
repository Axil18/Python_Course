def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)
    print(n)
    print(range(1, n + 1))
    print(i)

sumNumbers(6)

def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

a = sumNumbers(5)
print(a)