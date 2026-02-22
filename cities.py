# 8-5. Cities
# This program defines a function to describe a city and its country

def describe_city(city, country="Iceland"):
    """Prints a simple sentence about a city and its country."""
    print(f"{city} is in {country}.")

# Call the function for three cities
describe_city("Reykjavik")         # Uses default country
describe_city("Akureyri")          # Uses default country
describe_city("Paris", "France")   # Overrides default country