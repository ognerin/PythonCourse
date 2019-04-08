a = int(input())
b = int(input())
c = int(input())
from math import sqrt
d = b**2 - 4*a*c 
if a == 0 or b == 0 or c == 0:
    d = -1
if a == b == c == 0:
    print("x - любое число")
elif a == c == 0 or b == c == 0:
    x = 0
    print(f'x = {x}')
elif a == b == 0:
    print("Корней нет")    
elif a == 0 and b != 0 and c != 0:
    x = (c * (-1)) / b
    print(f'x = {x}')
elif b == 0 and a != 0 and c != 0:
    x1 = sqrt(c*(-1)/a)
    x2 = sqrt(c*(-1)/a)*(-1)
    print(f'x1 = {x1}, x2 = {x2}')
elif c == 0 and a != 0 and b != 0:
    x = b*(-1)/a    
    print(f'x = {x}')
elif d > 0:
    x1 = (b*(-1) - sqrt(d))/(2*a)
    x2 = (b*(-1) + sqrt(d))/(2*a)
    print(f'x1 = {x1}, x2 = {x2}')
elif d == 0:
    x = (b*(-1))/(2*a)
    print(f'x = {x}')
else:
    print("Корней нет")









