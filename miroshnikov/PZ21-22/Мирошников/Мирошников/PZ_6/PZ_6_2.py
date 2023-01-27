# Дан целочисленный список размера N, содержащий ровно два одинаковых элемента.
# Найти номера одинаковых элементов и вывести эти номера в порядке возрастания.
n = [1, 65, 12,136, 136, 131254]
indexes = []
for i in range(0, len(n)-1):
  for j in range(i):
    if n[i] == n[j]:
      indexes.append(i)
      indexes.append(j)
print(sorted(indexes))