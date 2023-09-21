import math
def fun1 (a, b):
    if a >= 15:
     z = (math.sin(2*a)+math.cos(2*b))
    else:
        z = ((a+(b**(2)))**(1/2))

    return z
def fun2 (n):
    S = 0
    for i in range (1, n+1):
        S = (S + (i+1)/i)
    return S

x = int(input("Введіть значення числа (x): "))

y = int(input("Введіть значення числа (y): "))

print("Значення виразу z = ", fun1(x, y))

n = int(input("Введіть значення числа (n): "))

print("Результат обчислень до n = ", fun2(n))