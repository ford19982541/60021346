import cmath
import math
print("======== โปรแกรมสมาการกำลังสอง ========")
print("======= a^2 x + b x + c =0 ======")

a = int(input("ป้อนค่าสัมประสิทธิ์ของ a: "))
b = int(input("ป้อนค่าสัมประสิทธิ์ของ b: "))
c = int(input("ป้อนค่าสัมประสิทธิ์ของ c: "))

d = b**2-4*a*c # discriminant

if d < 0:
    print ("สมการนี้ ไม่มีคำตอบ")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print ("สมการนี้ มีคำตอบเดียว: "), x
else:
    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    print ("สมาการนี้มีสองคำตอบ: ", x1, " or", x2)