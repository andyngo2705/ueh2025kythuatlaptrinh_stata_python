# Input: số tự nhiên 4 chữ số n
n = int(input())
# Lấy từng chữ số
a = (n // 1000) % 10
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
print(max(a,b,c,d))
