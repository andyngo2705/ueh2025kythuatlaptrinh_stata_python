# Input: m (tháng), y (năm)
m = int(input())
y = int(input())

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def days_in_month(m, y):
    if m in (1,3,5,7,8,10,12): return 31
    if m in (4,6,9,11): return 30
    return 29 if is_leap(y) else 28

print(days_in_month(m, y))
