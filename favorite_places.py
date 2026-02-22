# 6-9. Favorite Places
# This program stores favorite places for each person.

favorite_places = {
    "Alice": ["Paris", "New York", "Tokyo"],
    "Bob": ["Grand Canyon", "Yellowstone"],
    "Charlie": ["London", "Sydney", "Rome"]
}

# Loop through the dictionary and print each person and their favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f" - {place}")
    print()