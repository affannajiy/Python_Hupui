#Password Login

print("Password Login")

password = input("Enter password: ")

while password != None:
  print("Password is incorrect")
  password = input("Enter password: ")
  if password == "incorrect":
    print("Try again")
  password = input("Enter password: ")
  if password == "again":
    print("Try again later")
  password = input("Enter password: ")
  if password == "again later":
    print("Login Successful")
    break