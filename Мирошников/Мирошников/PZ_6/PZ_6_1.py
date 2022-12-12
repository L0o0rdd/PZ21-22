# Дан список A размера N. Вывести его элементы в следующем порядке: A1, A2, AN,
# AN-1, A3, A4, AN-2, AN-3, … .
import random
n = list()
for i in range(random.randint(0, 100)):
  n.append(random.randint(0, 100))
k = int(len(n)/4)

a = []
for i in range(0,len(n)-4*k):
    a.append(n[2*k+i])
print(sorted(a))