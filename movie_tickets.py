# 7-5. Movie Tickets
# This program calculates the total cost of movie tickets based on age.

total_cost = 0

# Ask how many tickets
num_tickets = int(input("How many tickets do you want to buy? "))

# Loop through each ticket holder
for i in range(num_tickets):
    age = int(input(f"Enter the age of ticket holder #{i+1}: "))
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    total_cost += ticket_price

print(f"\nThe total cost of the tickets is: ${total_cost}")