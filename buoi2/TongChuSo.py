# Input: số nguyên n có 4 chữ số
n = int(input("Moi ban nhap so nguyen n (co bon chu so): "))

# Tách các chữ số
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10

tong = a + b + c + d

# Output đúng format đề bài
print(f"{n} = {a} + {b} + {c} + {d} = {tong}.")
