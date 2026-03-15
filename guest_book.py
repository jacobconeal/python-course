# 10-4. Guest Book

print("Enter names for the guest book. Type 'quit' to stop.")

while True:
    name = input("Enter your name: ")

    if name.lower() == 'quit':
        break

    print(f"Hello {name}, thanks for visiting!")

    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")