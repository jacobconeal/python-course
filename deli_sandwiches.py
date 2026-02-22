# 7-8. Deli Sandwiches
# This program moves sandwiches from orders to finished list

# List of sandwich orders
sandwich_orders = ["tuna", "ham & cheese", "veggie", "turkey", "chicken salad"]

# Empty list for finished sandwiches
finished_sandwiches = []

# Process each sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # remove the first sandwich
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")