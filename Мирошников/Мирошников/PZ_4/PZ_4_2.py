a = float(input("Введите первое число: "))
b = int(input("Введите второе число: "))
i = 0

while a >= b:
    a -= b
    i += 1
print(i)
