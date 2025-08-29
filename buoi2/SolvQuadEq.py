# ax^2 + bx + c = 0
a = float(input())
b = float(input())
c = float(input())

def solve_quadratic(a,b,c):
    if a == 0:
        # bx + c = 0
        if b == 0:
            return "Unlimited solutions" if c == 0 else "No solution"
        x = -c / b
        return "x1=%.2f" % (x)
    else:
        d = b*b - 4*a*c
        if d < 0:
            return "No solution"
        elif d == 0:
            x = -b / (2*a)
            return "x1=%.2f" % (x)
        else:
            sqrt_d = d**0.5
            x1 = (-b - sqrt_d) / (2*a)
            x2 = (-b + sqrt_d) / (2*a)
            # in theo thứ tự tăng
            if x1 > x2: x1, x2 = x2, x1
            return "x1=%.2f, x2=%.2f" % (x1, x2)

print(solve_quadratic(a,b,c))
