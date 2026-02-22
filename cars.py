# 8-14. Cars
# This program defines a function that stores car information in a dictionary

def make_car(manufacturer, model, **options):
    """Return a dictionary representing a car with arbitrary info."""
    car_info = {
        "manufacturer": manufacturer,
        "model": model
    }
    # Add any additional key-value pairs
    for key, value in options.items():
        car_info[key] = value
    return car_info

# Call the function with required info and extra options
car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
car2 = make_car('tesla', 'model 3', color='red', autopilot=True)
car3 = make_car('ford', 'mustang', color='black', convertible=True)

# Print the dictionaries to check
print(car1)
print(car2)
print(car3)