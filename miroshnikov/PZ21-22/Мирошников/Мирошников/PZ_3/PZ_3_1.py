def check(poyas):
    num = input(poyas)
    while type(num) != int:
        try:
            return int(num)
        except ValueError:
            print("Введи число снова!")
        num = input(poyas)


a, b, c = check("Введите число А: "), check("Введите число В: "), check("Введите число С: ")

if a > 0 and b > 0 and c > 0:
    print(False)
elif a > 0 and b > 0:
    print(True)
elif a > 0 and c > 0:
    print(a, c)
elif b > 0 and c > 0:
    print(True)
else:
    print(False)
