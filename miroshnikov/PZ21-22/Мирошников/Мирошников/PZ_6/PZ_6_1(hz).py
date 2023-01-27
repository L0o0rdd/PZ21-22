import random

n = int(input())
a = []
for i in range(n):
  a.append(random.randint(0, 100))
print(f"Исходный список: {a}")

b = []
for i in range(0, (n - 1) // 2, 2):
    b.append(a[i])
    b.append(a[i + 1])
    b.append(a[- 1 - i])
    b.append(a[- i - 2])
print(b)