# Дан список A размера N и целое число K (1 < K < 4, K < N ). Осуществить
# циклический сдвиг элементов списка вправо на K позиций (при этом A1 перейдет в
# AK+1, A2 — в AK+2, ..., AN — в AK). Допускается использовать вспомогательный
# список из 4 элементов.
import random
n = list()
for i in range(random.randint(3, 15)):
  n.append(random.randint(0, 100))
print(n)
def check(strg):
    num = input(strg)
    while type(num) != int:
        try:
            return int(num)
        except Exception as e:
            print(f"Вы ввели строку, хотя ожидалось число. Ошибка: {e}")
        num = input(strg)
k = check("Введите шаг для переноса: ")
if k>4 or k > len(n) or k<1:
  raise ValueError("Введите другое число К!")
for i in range(k):
  n.insert(0, n.pop())
print(n)
