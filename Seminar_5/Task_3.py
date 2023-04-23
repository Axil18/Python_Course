# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)


# Input: 5

# Output: yes

def check(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "No"
    return "Yes"


num = int(input("Введите число: "))
print(check(num))