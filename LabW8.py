#Lab Week 8
#Activity 2
#1
#A
if 12 < 12:
  print('Less')
else:
  print('Not Less')

#B
Var1,Var2 = 25.12,15.00
if Var1 <= Var2:
  print('Less or equal')
else:
  print ('Greater than')

#2
#A
Y,X = 15.0,25.0
if Y != (X - 10.0):
  X = X - 10
else:
  X = X / 2.0

#B
Y = 10.0
X = 25.0
if Y != (X - 10.0):
  X = X - 10
else:
  X = X / 2.0

#C
Y = 15.0
if (Y < 15.0) and (Y >= 0.0):
  X = 5 * Y
else:
  X = 2 * Y

#D
Y = 10.0
if (Y < 15.0) and (Y >= 0.0):
  X = 5 * Y
else:
  X = 2 * Y

#E
Y = 36.0
if (Y < 15.0) and (Y >= 0.0):
  X = 5 * Y
elif Y >20 :
  X = 4 * Y
else:
  X = 2 * Y

#F
Y = -5
if (Y < 15.0) and (Y >= 0.0):
  X = 5 * Y
elif Y >20:
  X = 4 * Y
else:
  X = 2 * Y

#G
Y = 67
if (Y < 15.0) and (Y >= 0.0):
  X = 5 * Y
elif Y >20:
  if Y<30:
    X = 4 * Y
  else:
    X = 0 * Y
else:
  X = 2 * Y

#Activity 3
#Teenager Internet Addiction

print("!!Teenager Internet Addiction!!")

minute = eval(input("Number of minutes spent on the Internet in a day: "))
hour = minute / 60

if hour >= 2:
  print("You are might be addicted to the Net")
  answer = 0
  q1 = input("Do you stay online longer than you intended? ").lower()
  if q1 == "yes":
    answer += 1
  q2 = input("Do you hear other people in your life complain about how much time you spend online? ").lower()
  if q2 == "yes":
    answer += 1
  q3 = input("Do you say or think, 'Just a few more minutes' when online? ").lower()
  if q3 == "yes":
    answer += 1
  q4 = input("Do you try and fail to cut down on how much time you spend online? ").lower()
  if q4 == "yes":
    answer += 1
  q5 = input("Do you hide how long you’ve been online? ").lower()
  if q5 == "yes":
    answer += 1

  if answer >= 3:
    print("You are an INTERNET ADDICT")
  else:
    print("Control your Internet usage. You might become an ADDICT")
else:
  print("Keep up the good habit")