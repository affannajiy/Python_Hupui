#Lab Week 7
import math

#P&G User Input
choice = "A"
while choice != "Q":
  height = eval(input("Please enter height in cm: "))
  weight = eval(input("Please enter weight in kg: "))
  height_meter = height / 100
  bmi = weight / math.pow(height_meter, 2)
  
#BMI status
  if bmi < 18.5:
    category = "Underweight"
  elif bmi >= 18.5 and bmi < 25:
    category = "Normal"
  elif bmi >= 25 and bmi < 30:
    category = "Overweight"
  else:
    category = "Obesity"

#Output
  print("Your BMI value is% .2f"%bmi)
  print("You are in the", category, "category")
  print("")
  choice = input("Enter Q to end or any character to continue: ")