import math
a = int(input('Nhap do dai canh a:'))
b = int(input('Nhap do dai canh b:'))
c = int(input('Nhap do dai canh c:'))
p = (a+b+c)/2
S = (math.sqrt(p*(p-a)*(p-b)*(p-c)))
print('Dien tich tam giac S=',f"{S:.2f}")
