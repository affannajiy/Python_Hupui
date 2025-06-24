print("----------------------------------------")
print("☕︎☕︎☕︎☕︎ Little Star Coffee ☕︎☕︎☕︎☕︎")
print("いらっしゃいませ～")
print()

#medium coffee cup
print("----------------------------------------")
inquiry_med = str(input("Do you want a medium cup coffee? (Yes/No) "))
if inquiry_med == "Yes":
  quantitymed = int(input("How many medium cups would you like?: "))
  pricemed = 15 * quantitymed

  membership = str(input("Do you have a membership? (Platinum/Gold/No) "))
  if membership == "Platinum":
    pricemed *= 0.95
  elif membership == "Gold":
    pricemed *= 0.98
  elif membership == "No":
    pricemed = pricemed
  else:
    print("Please input membership status (Platinum/Gold/No) ")
elif inquiry_med == "No":
  print("No medium cup coffee ordered.")
  pricemed = 0
else:
  print("Please complete your order status (Yes/No) ")
print()

#large coffee cup
print("----------------------------------------")
inquiry_large = str(input("Do you want a large cup coffee? (Yes/No) "))
if inquiry_large == "Yes":
  quantitylarge = int(input("How many large cups would you like?: "))
  pricelarge = 20 * quantitylarge
  
  if quantitylarge >= 3:
    pricelarge *= 0.9
  else:
    pricelarge = pricelarge
elif inquiry_med == "No":
  print("No large cup coffee ordered. ")
  pricemed = 0
else:
  print("Please complete your order status (Yes/No) ")
print()

#calculation
print("----------------------------------------")
totalprice = pricemed + pricelarge
UOI = str(input("Do you have a UOI Card? (Yes/No) "))
if UOI == "Yes":
  totalprice *= 0.97
elif UOI == "No":
  print("Cash Payment.")
  totalprice = totalprice
else:
  print("Please answer the question (Yes/No) ")
print()

#output
print("----------------------------------------")
print("Total Price: RM ", "%.2f" % totalprice)
print("Thank you! Please come again!")
print("ありがとうございました")
print("----------------------------------------")