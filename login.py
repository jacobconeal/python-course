# 9-5. Login Attempts
# This program adds login_attempts to a User class

class User:
    """A simple user class"""
    
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0  # new attribute for login attempts

    def describe_user(self):
        print(f"User: {self.username}, Name: {self.first_name} {self.last_name}, Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        """Increment login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0"""
        self.login_attempts = 0


# Make an instance of User
user1 = User("Jacob", "O'Neal", "joneal", "jacob@example.com")

# Call increment_login_attempts several times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print login_attempts
print(f"Login attempts after incrementing: {user1.login_attempts}")

# Reset login_attempts
user1.reset_login_attempts()

# Print login_attempts again
print(f"Login attempts after resetting: {user1.login_attempts}")