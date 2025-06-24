intro = "Welcome to the Formula 1 Free Practice Lap Recorder"
print(intro)
print("=" * len(intro)) #calc num of char to provide number of "="

driver = int(input("Enter the number of driver(s): "))
lap = int(input("Enter the number of lap(s): "))
drivers = [] #list for drivers name
total_times = [] #list for total lap all drivers

for x in range(driver):
    driver_name = input("Enter the name of Driver {}: ".format(x + 1)) #use parking lots
    drivers.append(driver_name) #add driver name
    lap_time = 0

    for y in range(lap):
        lap_time += float(input("Enter the lap time for {} (in seconds) for lap {}: ".format(driver_name, y+1)))
    total = lap_time
    total_times.append(total)

#Table Results
print("\nRace Results:") #\n for new line
print("No.\tName\t\tTotal Time") #\t for indentation
for z in range(driver):
    print("{}\t{}\t\t{:.2f} seconds".format(z + 1, drivers[z], total_times[z]))