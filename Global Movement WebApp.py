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


def payment_options():
    print("Select your payment method:")
    print("1. Credit card")
    print("2. Debit card")
    print("3. PayPal")
    payment_method = input("Enter your choice: ")
    print("You have selected {} as your payment method.".format(payment_method))
    return payment_method


def transport_services():
    print("Global Movement App")
    print("Transport services")
    print("1. Luxurious bus services \n2. Airplane services\n3. Train services\n4. Taxi/Metro Services\n5. Hotel "
          "services")
    trs = input("Enter your choice: ")
    print("You have selected {} transport service.".format(trs))

    if trs == "1":
        print("Enter your desired luxury bus location from:\nAccra\nKumasi\nTakoradi\nTamale\nHo\nCape-Coast\n: ")
        origin = input()
        print("Enter your desired luxury bus location to: ")
        destination = input()
        print("You have selected to travel from {} to {}".format(origin, destination))

        adults = int(input("Enter the number of adults: "))
        children = int(input("Enter the number of children: "))
        basic_fare = 1000 * adults + 500 * children
        discount = 0.2 * basic_fare if adults > 3 else 0
        fare = basic_fare - discount
        print("The fare for the luxurious bus is {}.".format(fare))

        if trs == "2":
            print("Enter your desired airplane location from:\nAccra\nKumasi\nTakoradi\nTamale\nHo\nCape-Coast\n: ")
            origin = input()
            print("Enter your desired airplane location to: ")
            destination = input()
            print("You have selected to travel from {} to {}".format(origin, destination))

            adults = int(input("Enter the number of adults: "))
            children = int(input("Enter the number of children: "))
            basic_fare = 1000 * adults + 500 * children
            discount = 0.5 * basic_fare if adults > 3 else 0
            fare = basic_fare - discount
            print("The fare for the airplane is {}.".format(fare))

        if trs == "3":
            print("Enter your desired Train location from:Kumasi\nAccra\nSanyani\nTechiman\nCape-Coast\nGoaso"
                  "\nKoforidua\nTamale\nDamango\nNalerigu\nBolgatanga: ")
            origin = input()
            print("Enter your desired Train location to: ")
            destination = input()
            print("You have selected to travel from {} to {}".format(origin, destination))

        if trs == "4":
            print("Enter your desired Taxi/Metro location from:\nAccra\nKumasi\nTakoradi\nTamale\nHo\nCape-Coast\n: ")
            origin = input()
            print("Enter your desired Taxi/Metro location to: ")
            destination = input()
            print("You have selected to travel from {} to {}".format(origin, destination))

        if trs == "5":
            print("Do you want to book a hotel? (yes/no)")
            hotel_choice = input()

            if hotel_choice == "yes":
                print("Enter the hotel name: ")
                hotel_name = input()
                print("You have selected to book a hotel in {}".format(hotel_name))

            if hotel_choice == "no":
                return

                # Main program


users = []

print("Welcome to the main Application")

while True:
    choice = input("Choose an option:\n1. Register\n2. Login\n3. Exit\n4. Payment\n")

    if choice == "1":
        registration(users)

    elif choice == "2":
        login(users)

    elif choice == "3":
        print("Goodbye!")
        break

    if choice == "4":
        payment_method1 = payment_options()
        transport_services()

    else:
        print("Invalid choice!")
