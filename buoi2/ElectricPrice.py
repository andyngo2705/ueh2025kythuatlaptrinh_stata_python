# Input: old_index, new_index (electric meter readings)
old_idx = int(input())
new_idx = int(input())

# Bảng giá (VND/kWh) theo bậc thang
RATES = [
    (100, 1242),   # 0–100
    (50, 1304),    # 101–150
    (50, 1651),    # 151–200
    (100, 1788),   # 201–300
    (100, 1912),   # 301–400
    (float('inf'), 1962)  # 401+
]

def calc_bill(kwh):
    """Tính tiền điện theo bậc thang cho kWh >= 0, trả về tổng tiền (VND)."""
    total = 0
    remaining = kwh
    for block_kwh, price in RATES:
        take = min(remaining, block_kwh)
        if take <= 0:
            break
        total += take * price
        remaining -= take
    return total

# Xử lý
if new_idx < old_idx:
    print("Input error: new index < old index")
else:
    used = new_idx - old_idx
    money = calc_bill(used)*1.1
    # Output
    print(f"Old={old_idx}, New={new_idx}, kWh={used}, Amount={money} VND")
