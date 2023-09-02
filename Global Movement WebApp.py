print("Welcome to Vankem's Global Movement App")


def registration(name, postal_address, email_address, phone_number, password, users):
    print("Welcome to the Registration page")
    """
  This function registers a new user on the Global Movement app.

  Args:
    name: The user's name.
    postal_address: The user's postal address.
    email_address: The user's email address.
    phone_number: The user's phone number.
    password: The user's password.

  Returns:
    A boolean value indicating whether the registration was successful.
    :param users:
    :param name:
    :param postal_address:
    :param email_address:
    :param phone_number:
    :param password:
    """

    if not name or not postal_address or not email_address or not phone_number or not password:
        return False

    # Get the user input.
    name = input("Enter your name: ")
    postal_address = input("Enter your postal address: ")
    email_address = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")
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


def login(email_address, password, users):
    print("Welcome to the login page")
    """
  This function logs in a user to the Global Movement app.

  Args:
    email_address: The user's email address.
    password: The user's password.

  Returns:
    A boolean value indicating whether the login was successful.
    :param email_address:
    :param password:
    :param users:
  """

    def check_password_and_email(email, password):
        # Implementation of password verification logic
        # Replace this with your own password verification mechanism
        # For demonstration purposes, this function simply checks if the password is "password123"
        if password == "password123":
            return True
        if email == "selikemvan@gmail.com":
            return True

        else:
            return False

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user_data in users:
        if email == user_data.get("email"):
            stored_password = user_data.get("password")
            if check_password_and_email(password, stored_password):
                print("Login successful!")
            else:
                print("Invalid password.")
            return
    print("Invalid email.")
    # Check if the user exists in the list of users.
    for user in users:
        if user['email_address'] == email_address and user['password'] == hash(password):
            return user['session_id']

    return False


# Main program
user_data = {}

print("Welcome to the main Application")

while True:
    choice = input("Choose an option:\n1. Register\n2. Login\n3. Exit\n")

    if choice == "1":
        user_data = registration(name, postal_address, email_address, phone_number, password, users)

    if choice == "2":
        login(email_address, password, users)

    if choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
