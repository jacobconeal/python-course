# Original guest list
guest_list = ["Albert Einstein", "Oprah Winfrey", "Leonardo da Vinci"]

# Print original invitations
print("Original invitations:\n")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to dinner!")
new code
# Found a bigger dinner table
print("\nGood news! We found a bigger dinner table!\n")

# Add new guests
guest_list.insert(0, "Dave Grohl")                # Add to the beginning
guest_list.insert(len(guest_list)//2, "Chris Cornell")  # Add to the middle
guest_list.append("Layne Staley")                # Add to the end

# Sort the list alphabetically
guest_list.sort()

# Print updated sorted invitations
print("Updated invitations (sorted):\n")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to dinner!")
