total = int(input('Nhap vao tong so giay:'))
h = total//3600
total_h = total - 3600*h
m = (total_h)//60
s = total - h*3600 - m*60
print(f"{total} giay co dang {h}:{m}:{s}")
