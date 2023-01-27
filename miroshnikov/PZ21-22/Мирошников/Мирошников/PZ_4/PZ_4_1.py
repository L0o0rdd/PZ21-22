def check(poyas):
    num = input(poyas)
    while type(num) != int:
        try:
            return int(num)
        except ValueError:
            print("Введи число снова!")
        num = input(poyas)

def check_f(poyas):
    num = input(poyas)
    while type(num) != float:
        try:
            return float(num)
        except ValueError:
            print("Введи число снова!")
        num = input(poyas)


a, N = check_f(""), check("")
res = 0
for i in range(N+1):
    print(i)
    res += ((-1) ** i) * (a ** i)
    
print(res)
