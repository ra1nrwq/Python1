import random

numbers = []

for _ in range(10):
    numbers.append(random.randint(1, 10))

print("Список случайных чисел:", numbers)

user_number = int(input("Введите число от 1 до 10: "))

if user_number in numbers:
    print("Число находится в списке.")
else:
    print("Число отсутствует в списке.")