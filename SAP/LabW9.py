#Lab Activity W9

#Activity 1
#1
'''
countEmp = 0
while countEmp <5:
  hour = int(input('Please Enter Hours of Working: '))
  rate = float(input('Please Enter Rate for each Hours: '))
  print('Weekly payment is RM', hour * rate)
  countEmp = countEmp + 1
print('All employees salary are processed.')
'''
#2
'''
CountStar = 0
Num = eval(input('Please enter a number: '))
while CountStar < Num:
  print('*', end= '\t')
  CountStar += 1

#3
X = 3
Count = 0
while Count < 3:
  X = X * X
  print(X)
print(Count)

#Activity 2
#a

for NextCh in range ('A','Z'):
  print(NextCh)
print( )
'''

#b
'''
A,Z = 2,8
for NextCh in range (A,Z,4):
  print(NextCh)
print( )

#c
for num in range(4):
  for i in range(num):
    print (num, end=" ")
  print("\n")
'''

#Activity3
#Initialise variable
largest = None
counter = 0

num = int(input("Enter an integer to start the program: "))
if num == -32767:
  print("No integers entered!")
else:
  largest = num
  counter += 1

while num != -32767:
  num = int(input("Enter another integer. (Enter -32767 to stop the program): "))
  if num != -32767:
    counter += 1
    if num > largest:
      largest = num

if largest != None:
  print("The largest number among", counter, "numbers of integers entered is", largest)