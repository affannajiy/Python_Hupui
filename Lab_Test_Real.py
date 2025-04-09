#Lab Test SAP 22.03.2024

print("MMCineplex SI Movie Recorder System")
print("==================================")
q = 'a'
num_movies = int(input("\nEnter the number of movie(s) on show: "))
movie_list = []
sales = []
total_sales = []
total = 0

while q != "Quit":
    for x in range(num_movies):
        name = input("\nEnter the name of movie {}: ".format(x+1))
        movie_list.append(name)
        qty_tickets = int(input("Enter the number of tickets sold for {}: ".format(name)))
        ticket_price = int(input("Enter the price of a ticket for {}: RM ".format(name)))
        sale = qty_tickets * ticket_price
        sales.append(sale)
        total += qty_tickets * ticket_price
        total_sales.append(total)
        
    print("\nTodays's Sales Summary:")
    print("No.\tMovie\t\tTotal Sales")
    for z in range(num_movies):
        print("{}\t{}\t\tRM{:.2f}".format(z+1, movie_list[z], sales[z]))
    print("Grand Total Sales: RM{:.2f}".format(total_sales[z]))
    q = input("\nEnter the next number of movies on show or 'Quit' to end program: ")