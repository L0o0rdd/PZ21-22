# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Положительные числа:
# Количество положительных чисел:
# Отрицательные числа:
# Количество отрицательных чисел:
l = '-56 5 12 -391 11 195 -124 -15 124 -1 52 -3 -4 88 31'
f1 = open('file.txt', 'w')
f1.writelines(l)
f1.close
f1 = open('file.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()
f1 = open('file.txt', 'w')
max, t = 0, 0
for i in range(len(k)):
    max = max if max > k[i] else k[i]
    if k[i] < 0:
        t += 1
print('Количество элементов: ', len(k), 'Максимальный элемент: ', max, file=f1)

f1.close()
f1 = open('file.txt', 'a')
for i in l.split(' '):
    if int(i) > 0:
        print(i, file=f1)
f1.close()

f1 = open('file.txt', 'a')
for i in l.split(' '):
    if int(i) < 0:
        print(i, file=f1)
f1.close()

f1 = open('file.txt', 'a')
count = 0
for i in l:
    if i > 0:
         count += 1
print("Количество положительных чисел: ", count, file=f1)
f1.close()
