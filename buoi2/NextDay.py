# Input: d, m, y (3 dòng)
d = int(input())
m = int(input())
y = int(input())

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def dim(month, year):
    if month in (1,3,5,7,8,10,12): return 31
    if month in (4,6,9,11): return 30
    return 29 if is_leap(year) else 28

def next_day(d, m, y):
    if d < dim(m, y):
        return d + 1, m, y
    if m < 12:
        return 1, m + 1, y
    return 1, 12, y + 1

nd, nm, ny = next_day(d, m, y)
print(f"{nd}/{nm}/{ny}")
