s = float(input ("Сумма чисел: "))
p = float(input ("Произведение чисел: "))
import math
x1 = (-s + math.sqrt((s**2) - (4 * -1 * -p))) / (-2)
x2 = (-s - math.sqrt((s**2) - (4 * -1 * -p))) / (-2)
print (x1)
print (x2)