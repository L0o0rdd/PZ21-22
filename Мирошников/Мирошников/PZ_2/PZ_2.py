try:
    n = int(input("Введите трехначное число: "))
    if n < 100:
        print('Некорректное значчение')
    else:
        d1 = n % 10
        d2 = n % 100 // 10
        d3 = n // 100
        print("Сумма цифр числа: ", d1 + d2 + d3)
        print("Произведение цифр числа: ", d1 * d2 * d3)
except:
    print('Error')
