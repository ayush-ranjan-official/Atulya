import math
a = int(input("First parameter :"))
b = input('Second parameter(+,-,/,.) :')
c = int(input('Third parameter :'))
if b == '+':
    print(a+c)
elif b == '-':
    print(a - c)
elif b == '/':
    print(a / c)
elif b == '.':
    print(a*c)