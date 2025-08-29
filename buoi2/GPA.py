# Input: Toan, Ly, Hoa (điểm 0..10)
toan = float(input())
ly   = float(input())
hoa  = float(input())

avg = (toan*2 + ly*3 + hoa) / 6

if 8 <= avg <= 10:
    rating = "Good"
elif 6.5 <= avg < 8:
    rating = "Pretty"
elif 5 <= avg < 6.5:
    rating = "Average"
else:
    rating = "Weak"

print("Average point = %.2f, rating %s." % (avg, rating))
