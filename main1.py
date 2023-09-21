import math
def fun1 (a, b):
    if a >= 15:
     z = (math.sin(2*a)+math.cos(2*b))
    else:
        z = ((a+(b**(2)))**(1/2))

    return z

from mod import fun2

x = int(input("Введіть значення числа (x): "))

y = int(input("Введіть значення числа (y): "))

print("Значення виразу z = ", fun1(x, y))

n = int(input("Введіть значення числа (n): "))
while n < 1:
    n = int(input("Введіть значення числа (n) ще раз: "))
print("Результат обчислень до n = ", fun2(n))