import math
x = float(input('Nhap so thuc x:'))
#y1 co dieu kien : x>=0
y1 = 4*(x**2 + 10*x*math.sqrt(x) + 3*x +1)
if x < 0 :
    print(f"y1 khong the xac dinh boi x<0")
else :
    print(f"y1={y1:.2f}")
#y2 co dieu kien: demoninator !=0
numerator = math.sin(math.pi*(x**2)) + math.sqrt(x**2 + 1)
denominator = math.exp(2*x) + math.cos(math.pi/4 * x)
y2 = numerator/denominator
if denominator==0 :
    print(f"y2 khong the xac dinh boi demoninatior = 0")
else :
    print(f"y2={y2:.2f}")
