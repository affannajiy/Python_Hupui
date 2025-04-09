print("_____________________________________")
print("ඞඞඞඞ Mileage Calculator ඞඞඞඞ") 
print("_____________________________________")
print()

#input
print()
currentreading = float(input("Current Reading(km): "))
previousreading = float(input("Previous Reading(km): "))
petrolamount = float(input("Amount of Petrol(L): "))
petrolprice = float(input("Petrol Price per Liter(RM/L): "))

#calculation
petrolmileage = (currentreading - previousreading) / petrolamount
unitcost = petrolmileage / petrolprice

#output
print()
print("_____________________________________")
print("Petrol Mileage: RM", petrolmileage)
print("Unit Cost: RM", unitcost)
