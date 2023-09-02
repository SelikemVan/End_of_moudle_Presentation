print("Welcome to Vankem's Global Movement App")


def send_confirmation_email():
    pass


def send_confirmation_sms():
    pass


def registration(name, postal_address, email_address, phone_number, password, users):
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

    if not name or not postal_address or not email_address or not phone_number:
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
    send_confirmation_email()
    send_confirmation_sms()

    return True


def login(email_address, password, users):
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

    # Check if the user exists in the list of users.
    for user in users:
        if user['email_address'] == email_address and user['password'] == hash(password):
            return user['session_id']

    return False
