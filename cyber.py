# List of common weak passwords
weak_passwords = [
    "123456", "password", "12345678", "qwerty", "abc123", 
    "letmein", "123123", "admin", "welcome", "iloveyou"
]

def check_password(password):
    # Check if the given password is in the list of weak passwords
    if password in weak_passwords:
        print("Your password is too weak. Please choose a stronger one!")
    else:
        print("Your password seems strong enough.")

# Main function to run the password checker
def main():
    print("Welcome to the Password Checker!")
    user_password = input("Please enter a password to check: ")
    check_password(user_password)

# Run the program
if __name__ == "__main__":
    main()
