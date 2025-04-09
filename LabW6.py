#Lab Week 6 'Affan
import math
r = 1
n = 1
t = 1
V = 1
c = 1
pi = 3.142
b = 1 
a = 1
#a)
d_n = 1 / (1 + r)**n
#b)
t_prime = t * (math.sqrt(1-(V**2 / c**2)))
#c)
V = 4/3 * pi * r**3
#d)
x = -b + (math.sqrt(b**2 - 4 * a * c)) / 2 * a

x = 2.5
y = -1.5
m = 18
n = 4
s = "Life"
t = "Honey"
print(x + n * y - (x + n) * y)
print(m / n + m % n)
print(5 * x - n / 5)
print(math.sqrt (math. sqrt(n)))
print(s + t)
print(s + 'is sweet as'+ ' ' + t)


d1 = float(input("Insert distance in meters: "))
d2 = float(input("Insert distance in meters: "))

if d1 < d2:
  d1,d2 = d2,d1 
diff = (d1 - d2) / 1000
print("The difference in kilometers is:", diff)