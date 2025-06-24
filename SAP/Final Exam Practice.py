#Repetition Testing
'''
i = 0
while i < 10:
  print("TXT")
  i += 1

sum = 0
w = 0
while w < 10:
  sum = sum + w
  w = w + 1
print("Sum is %d"%(sum))

data = eval(input("Enter a number or 0 to exit: "))
sum1 = 0
while data != 0:
  sum1 = sum1 + data
  data = eval(input("Enter a number or 0 to exit: "))
print("Sum is %d"%(sum1))

weather = input("Please enter weather: ")
lap = 0
while weather != "raining": #it will stop if raining
  lap = lap + 1
  weather = input("Please enter weather: ")
print("Number of lap(s):", lap)

for i in range(1,11):
  print("Lee Dong Wook")

for z in range(10,0,-1):
  print(z)

s = 0
j = 3
k = 8
t = 2
for j in range(1,6):
  print(j, end = "")
  s = s + j
print(s)
for k in range(2):
  print(k, end = "")
for i in range(10, 0, -1):
  print(i)
for i in range(j,k+1):
  print(i+t)

lap = 0
weather = input("Enter weather: ")
while weather != "rain":
  lap = lap + 1
  weather = input("Enter weather: ")
  if lap == 4:
    break
print("Number of lap(s):", lap)

j = 5
while j > 0:
  for i in range(1,j+1):
    if i == j:
      print("#")
    else:
      print("#", end = "")
  j = j -1
z = 1
while z <= 5:
  for i in range(z,-1,-1):
    if i == z:
      print("*")
    elif z < 5:
      print("*", end = "")
  z = z + 1

def main():
  number = 0
  numbers = [10]
  m(number, numbers)
  print("number is", number, "and numbers[0] is", numbers[0])

def m(x,y):
  x = 3
  y[0] = 3
  return x

main()

def factorial(n):
  product = 1
  for i in range(1,n+1):
    product *= i
    print(product)

factorial(5)'''

def factorial(n):
  if n < 1:
    result = 1
  else:
    result = n * factorial(n-1)
    print(result)
  return result

factorial(5)