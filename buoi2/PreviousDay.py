# Input: d, m, y (3 dòng)
d = int(input())
m = int(input())
y = int(input())

def is_leap(year: int) -> bool:
    """Năm nhuận theo lịch Gregory."""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def days_in_month(month: int, year: int) -> int:
    """Số ngày của tháng 'month' trong năm 'year'."""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    # month == 2
    return 29 if is_leap(year) else 28

def previous_day(d: int, m: int, y: int):
    """Trả về ngày trước đó (D, M, Y)."""
    if d > 1:
        return d - 1, m, y
    # d == 1
    if m == 1:
        return days_in_month(12, y - 1), 12, y - 1
    prev_m = m - 1
    return days_in_month(prev_m, y), prev_m, y

pd, pm, py = previous_day(d, m, y)
print(f"Previous day of {d}/{m}/{y} is {pd}/{pm}/{py}.")
