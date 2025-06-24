def crude_oil_list = []

def refinery_system(crude_oil_list):
    total_crude_oil = sum(crude_oil_list) #sum of oil
    percent_crude_oil = []

    for i in crude_oil_list: #calc the percentage
        percent_crude_oil.append(i / total_crude_oil * 100)

    gasoline = 0.45 * total_crude_oil
    diesel = 0.35 * total_crude_oil
    jet_fuel = 0.20 * total_crude_oil

    return total_crude_oil, percent_crude_oil, gasoline, diesel, jet_fuel

num = int(input("Please enter total number of refinery units: "))

for j in range(num):
    unit = eval(input("Please enter the amount of crude oil in unit {}: ".format(j+1)))
    crude_oil_list.append(unit)

total_crude_oil, percent_crude_oil, gasoline, diesel, jet_fuel = refinery_system(crude_oil_list)

print("\nTotal crude oil processed:", total_crude_oil)

for x in range(num):
    print("Percent of crude oil processed by unit", str(x + 1), ": ", round(percent_crude_oil[x], 2), "%")

print("Gasoline Produced:", round(gasoline, 2))
print("Diesel Produced:", round(diesel, 2))
print("Jet Fuel Produced:", round(jet_fuel, 2))