import math
x1 = int(input('Nhap so nguyen x1:'))
x2 = int(input('Nhap so nguyen x2:'))
y1 = int(input('Nhap so nguyen y1:'))
y2 = int(input('Nhap so nguyen y1:'))
dis= math.sqrt(((x2-x1)**2) * ((y2-y1)**2))
print(f"khoang cach giua 2 diem A({x1},{x2}) va B({y1},{y2}) la {dis}")
