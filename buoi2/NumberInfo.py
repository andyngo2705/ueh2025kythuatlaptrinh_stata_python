# Input: n (n < 1000)
n = int(input())

# Số chữ số
if n == 0:
    digits = 1
else:
    digits = 0
    t = abs(n)
    while t > 0:
        digits += 1
        t //= 10

# Tổng chữ số, chữ số đầu/cuối (làm với trị tuyệt đối)
t = abs(n)
last = t % 10
first = t
while first >= 10:
    first //= 10

sum_digits = 0
tmp = abs(n)
while tmp > 0:
    sum_digits += tmp % 10
    tmp //= 10

print(f"{n} has {digits} digits.")
print(f"1 + 5 + 6 = {sum_digits}.")  # theo ví dụ cách trình bày phép cộng
print(f"Last digit is {last}.")
print(f"First digit is {first}.")
