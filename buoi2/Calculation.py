# Input: two numbers a, b and an operator op (+, -, *, /)
a = float(input())
b = float(input())
op = input().strip()

def calculation(a, b, op):
    """
    Perform calculation: a (op) b
    """
    if op == '+':
        return "%.2f + %.2f = %.2f" % (a, b, a + b)
    elif op == '-':
        return "%.2f - %.2f = %.2f" % (a, b, a - b)
    elif op == '*':
        return "%.2f * %.2f = %.2f" % (a, b, a * b)
    elif op == '/':
        if b == 0:
            return "%.2f / %.2f = Cannot divide by zero" % (a, b)
        else:
            return "%.2f / %.2f = %.2f" % (a, b, a / b)
    else:
        return "Invalid operator"

# Output
print(calculation(a, b, op))
