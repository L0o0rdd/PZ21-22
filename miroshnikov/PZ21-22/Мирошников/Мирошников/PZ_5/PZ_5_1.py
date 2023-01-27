# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить
# функцией с параметрами. Значения n и m программа должна запрашивать.
def check(strg):
    num = input(strg)
    while type(num) != int:
        try:
            return int(num)
        except Exception as e:
            print(f"Вы ввели строку, хотя ожидалось число. Ошибка: {e}")
        num = input(strg)


def summing(n, m):
    sum = 0
    for i in range(n, m + 1):
        sum += i
    return sum


n, m = check(""), check("")
sum = summing(n, m)

print(sum)
