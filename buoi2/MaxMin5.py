# Input: 5 số a, b, c, d, e
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

# Gom vào list để dễ xử lý
nums = [a, b, c, d, e]

mn = min(nums)
mx = max(nums)

# Output theo đề: in min trước rồi đến max
print(f"{int(mn)} {int(mx)}")
