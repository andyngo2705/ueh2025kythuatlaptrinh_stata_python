# Input: a, b, c (độ dài 3 cạnh)
a = float(input())
b = float(input())
c = float(input())

def fmt(x):
    # in gọn gàng: 5.0 -> 5 ; 5.25 -> 5.25
    return f"{x:g}"

def is_triangle(a, b, c):
    # Sắp xếp tăng dần rồi kiểm tra bất đẳng thức tam giác
    x, y, z = sorted([a, b, c])  # x <= y <= z
    return x > 0 and x + y > z

# Tính cạnh lớn nhất
m = max(a, b, c)

# Output
print(f"Max({fmt(a)}, {fmt(b)}, {fmt(c)}) = {fmt(m)}.")
print("Triangle: YES" if is_triangle(a, b, c) else "Triangle: NO")
