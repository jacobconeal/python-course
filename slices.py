# 4-10. Slices

guests = ["Chris Cornell", "Dave Grohl", "Layne Staley",
          "Kurt Cobain", "Eddie Vedder", "Scott Weiland"]

guests.sort()

print("Sorted guest list:")
for guest in guests:
    print(guest)

print("\n--- SLICES ---")

print("\nThe first three items in the list are:")
print(guests[:3])

print("\nThree items from the middle of the list are:")
print(guests[2:5])

print("\nThe last three items in the list are:")
print(guests[-3:])
