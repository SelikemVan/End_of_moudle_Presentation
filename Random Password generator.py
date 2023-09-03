print("Welcome to Vankem's Global Movement App")


def registration(users):
    print("Welcome to the Registration page")

    name = input("Enter your name: ")
    postal_address = input("Enter your postal address: ")
    email_address = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")

    if not name or not postal_address or not email_address or not phone_number or not password:
        print("Registration failed. Please fill in all fields.")
        return False

    # Create a dictionary to store the user data.
    user_data = {
        'name': name,
        'postal_address': postal_address,
        'email_address': email_address,
        'phone_number': phone_number,
        'password': password
    }

    # Add the user data to the list of users.
    users.append(user_data)

    # Send a confirmation email and SMS message to the user.
    print("Registration successful! A confirmation email has been sent to {}.".format(email_address))

    return user_data


def login(users):
    print("Welcome to the login page")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user_data in users:
        if email == user_data.get("email_address") and password == user_data.get("password"):
            print("Login successful!")
            return
    print("Invalid email or password.")


# Main program
users = []

print("Welcome to the main Application")

while True:
    choice = input("Choose an option:\n1. Register\n2. Login\n3. Exit\n")

    if choice == "1":
        registration(users)

    elif choice == "2":
        login(users)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")