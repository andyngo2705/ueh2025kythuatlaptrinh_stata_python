# Input: old_m3, new_m3  (2 dòng)
old_m3 = int(input())
new_m3 = int(input())

# Bậc thang theo m3/tháng (giả định hộ 1 người, theo ví dụ đề)
RATES = [(4, 4400), (2, 8300), (float('inf'), 10500)]

def bill(used):
    total, remain = 0, used
    for block, price in RATES:
        take = min(remain, block)
        if take <= 0:
            break
        total += take * price
        remain -= take
    return total

if new_m3 < old_m3:
    print("Input error: new index < old index")
else:
    used = new_m3 - old_m3
    amount = bill(used)
    # Định dạng kiểu 8.800 đ như ví dụ
    fmt_amount = f"{amount:,}".replace(",", ".")
    print(f"Payment for {used} m^3 in month is {fmt_amount} đ.")
