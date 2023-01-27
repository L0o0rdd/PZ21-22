# Описать функцию Power1(A, B) вещественного типа, находящую величину AB по
# формуле AB = exp(B*ln(A)) (параметры A и B — вещественные). В случае нулевого
# или отрицательного параметра A функция возвращает 0. С помощью этой функции
# найти степени AP
# , BP
# , если даны числа P, A, B, C.
import math

def check(strg):
    num = input(strg)
    while type(num) != float:
        try:
            return float(num)
        except Exception as e:
            print(f"Вы ввели строку, хотя ожидалось число. Ошибка: {e}")
        num = input(strg)

def Power1(a,b):
  if a<=0:
    return 0
  ab = math.exp(b*math.log(a))
  return ab

def main():
  p, a,b,c = check(""), check(""), check(""), check("")
  ap,bp,cp = Power1(a,p),Power1(b,p),Power1(c,p)
  print(ap,bp,cp)

main()