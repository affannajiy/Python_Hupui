#Variables = A container for a piece of data (string, integer, float, boolean)
#Variables behave as if it was the data it contains

#Strings: series of characters
first_name = "Affan"
food = "pasta"
email = "affan@my.com"

print(f"Hello {first_name}") #parking lot method
print(f"You like {food}")
print(f"Your email is {email}")

#Integers: whole numbers
age = 20
quantity = 10
num_of_students = 20

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Floats: floating point (decimal)
price = 10.99
gpa = 3.2
distance = 10.5

print(f"The price is RM{price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

#Booleans: True or False
is_student = True
is_teacher = False
is_admin = False
for_sale = True

print(f"Are you a student? {is_student}")
print(f"Are you a teacher? {is_teacher}")
print(f"Are you an admin? {is_admin}")

if is_student:
  print("You are a student")
else:
  print("You are not a student")

if for_sale:
  print("This item is for sale")
else:
  print("This item is not for sale")