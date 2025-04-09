# Function to check if the year is a leap year (Griffin condition)
def griffin_year(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

# Function to check if the sum of digits of the year is divisible by 9 (Phoenix condition)
def phoenix_year(year):
    return sum(int(digit) for digit in str(year)) % 9 == 0

# Function to check if the year is a prime number (Dragon condition)
def prime_year(year):
    if year <= 1:
        return False
    for i in range(2, int(year**0.5) + 1):
        if year % i == 0:
            return False
    return True

def dragon_year(year):
    return prime_year(year)

# Function to find the three years that summon the creatures
def find_summoning_years():
    # Loop through the years from 2023 to 2028
    for year in range(2023, 2029):
        if griffin_year(year):
            print(f"{year}: Griffin will appear.")
        if phoenix_year(year):
            print(f"{year}: Phoenix will appear.")
        if dragon_year(year):
            print(f"{year}: Dragon will appear.")

# Call the function to find the summoning years
find_summoning_years()
