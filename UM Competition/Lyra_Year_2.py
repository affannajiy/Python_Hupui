#Year Lists
years = [2024, 2025, 2026, 2027]

#For Loop for Checking Years
for year in years:
  print(f"\nChecking year {year}:") #Placeholder Method

  #Griffin Year
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year}: Griffin will appear.")
    
  #Phoenix Year
  digit_sum = sum(int(digit) for digit in str(year)) #sum: calc sum of digits
  if digit_sum % 9 == 0:
    print(f"{year}: Phoenix will appear.")
    
  #Dragon Year
  is_prime = True
  if year > 1:  #Prime numbers are greater than 1
    for i in range(2, int(year**0.5) + 1):
      if year % i == 0:
        is_prime = False
        break
  else:
    is_prime = False  #Any number <= 1 is not prime
    
  if is_prime:
    print(f"{year}: Dragon will appear.")
    
  #No Creature Year
  if not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and digit_sum % 9 != 0 and not is_prime:
    print(f"{year}: No creature will appear.")
