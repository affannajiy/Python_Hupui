msg = "Mahen Borgirs Bill Calculator"
print(msg)
print("*" * len(msg))

table = int(input("Number of tables: "))
name = []
count = []
quantity = []
price = []
total_bills = [] #Initialize an empty list to store total bills per table

for x in range(table):
    item_count = int(input("How many item(s) purchased for Table {}: ".format(x + 1)))
    count.append(item_count) # parking lot
    table_total = 0 #Initialize a variable to store total bill for current table

    for y in range(item_count):
        item_name = input("What is the name of the item {}: ".format(y + 1))
        name.append(item_name)
        item_quantity = int(input("How many {} purchased: ".format(item_name)))
        quantity.append(item_quantity)
        item_price = float(input("How much is the price {}: ".format(item_name)))
        price.append(item_price)
        total = item_quantity * item_price
        table_total += total  # Add current item total to table total

    total_bills.append(table_total) # Append the calculated table total to the total_bills list

# Summary
print("\nSummary:")
print("Table No.\tItem\t\t\tTotal Bill") # \t for indentation
q = 0
for z in range(table):
    name2 = []
    for u in range(count[z]):
        name2.append(name[q])
        q += 1
    print("{}\t\t{}\t\tRM{:.2f}".format(z + 1, name2, total_bills[z])) # total_bills for individual table total