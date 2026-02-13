# 6-5. Rivers
# This program uses a dictionary to store rivers
# and the countries they run through.

rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states"
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()

# Print the name of each river
print("Rivers:")
for river in rivers.keys():
    print(river.title())

print()

# Print the name of each country
print("Countries:")
for country in rivers.values():
    print(country.title())
