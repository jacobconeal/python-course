# 10-6 Addition

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 + num2
    print("The sum is:", result)

except ValueError:
    print("Sorry, you must enter numbers only.")