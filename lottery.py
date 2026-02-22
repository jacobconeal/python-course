# 9-14. Lottery
# This program generates a random lottery number and checks if the user wins

import random

# Create a list of 10 numbers and 5 letters
numbers_and_letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E"]

# Randomly select 4 numbers and 1 letter
lottery_numbers = random.sample(range(10), 4)  # 4 unique numbers from 0-9
lottery_letter = random.choice(["A", "B", "C", "D", "E"])  # 1 letter

lottery_ticket = "".join(map(str, lottery_numbers)) + lottery_letter

# Get user input
user_ticket = input("Enter your lottery ticket (4 numbers followed by 1 letter, e.g., 1234A): ")

# Compare and print result
if user_ticket == lottery_ticket:
    print(f"Congratulations! You won! The winning ticket was {lottery_ticket}.")
else:
    print(f"Sorry, you did not win. The winning ticket was {lottery_ticket}.")