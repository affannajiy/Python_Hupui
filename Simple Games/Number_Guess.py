import random

#declare all variable
number = random.randint(0,10000000)
guess = 0
numguess = 0

#intro
print("Hello there!")
print("Welcome to the number guessing game!")
print("I've generated a random number between 0 and 10000000.")
print("Try to guess it in as few tries as possible.")
print("------------------------------------------------")

#choice to playSSSAA  
choice = str(input("Do you want to play?")).lower()
if choice == "yes":
    name = input("What is your name?")
    print("Hello", name, "let us begin!")
elif choice == "no":
    print("Alright! Come back when you want to play")
    exit()

#looping
while guess!= number:
  guess = int(input("Enter Guess: "))
  #if num is higher
  if (guess < number):
    print("Guess Higher!")
    numguess += 1
  #if num is lower
  elif (guess > number):
    print("Guess Lower!")
    numguess += 1
  #if correct guess
  else:
    print("---------------------------------")
    print("You've won! Well done",name+"!")
    print("You have guessed",numguess,"time(s)!")
    exit()

#ask if they want to proceed
if numguess == 10 or numguess == 20 or numguess == 30 or numguess == 40:
    ask = input("Do you want to continue? ").lower()
    if ask == "no":
        print("Good luck", name + "!")
    elif ask == "yes":
        print("Alright! Come back when you want to play again")
        exit()