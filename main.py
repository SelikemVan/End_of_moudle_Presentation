# Global variables
user_logged_in = False
current_user = None


# Registration function
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
    print("Registration successful! A confirmation email has been sent to {}".format(email_address))

    return user_data


# Login function
def login(users):
    global user_logged_in, current_user
    print("Welcome to the login page")

    name = input("Enter your name: ")
    password = input("Enter your password: ")

    authenticated_user = None

    for user_data in users:
        if name == user_data.get("name") and password == user_data.get("password"):
            print("Login successful!")
            user_logged_in = True
            authenticated_user = user_data  # Store the authenticated user's data

    # Check if the user is an admin
    if (name == "seli" or name == "kofi") and (password == "seli123" or password == "kofi123"):
        print("Admin login successful!")
        while user_logged_in:  # Stay in the admin menu until the user logs out
            choice1 = input("Choose an option:\n1. Payment\n2. Transportation Options\n3. Entertainment\n4. Logout\n")

            if choice1 == "1":
                payment_method, currency = payment_options()
                # Handle admin-specific payment processing here
                # Example: admin_payment_processing(payment_method, currency)

            elif choice1 == "2":
                transport_services()  # Allow admin to access transportation options
                # Handle admin-specific transportation processing here
                # Example: admin_transport_processing()

            elif choice1 == "3":
                entertainment()  # Allow admin to access entertainment options
                # Handle admin-specific entertainment processing here

            elif choice1 == "4":
                print("Goodbye, admin!")
                user_logged_in = False  # Log out the admin

    elif authenticated_user is None:
        print("Invalid name or password.")


def entertainment():
    while True:
        print("\nEntertainment Options\n")
        print("1. Play Tic Tac Toe")
        print("2. Rock, Paper, Scissors")
        print("3. Back to Main Menu")
        print("4. Music")
        print("5. movies")

        option = input("Choose an option: ")

        if option == "1":
            tic_tac_toe_game()
        if option == "2":
            while True:
                print("Let's play Rock Paper Scissors!")
                user_choice = input("What is your choice? (rock/paper/scissors): ")
                computer_choice = "rock" or "paper" or "scissors"

                if user_choice == computer_choice:
                    print("It's a tie!")
                elif user_choice == "rock" and computer_choice == "scissors":
                    print("You win!")
                elif user_choice == "paper" and computer_choice == "rock":
                    print("You win!")
                elif user_choice == "scissors" and computer_choice == "paper":
                    print("You win!")
                else:
                    print("You lose!")
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again == "no":
                    return

                if play_again == "yes":
                    return

        if option == "3":
            break

        if option == "4":
            print("\n Loading music...")

            music = input(
                "\n Music list_ \n1. As it was:By Harry Styles\n2.Pretty little lair:By JVKE\n3. Sunflower:By "
                "Post Malone\n4.Cradles:By Suburban\n5. Enemy:By Imagine dragons\n")

            if music == "1":
                print("Playing 'As it was' by Harry Styles...")

            if music == "2":
                print("Playing 'Pretty Little liar' by JVKE...")

            if music == "3":
                print("Playing 'Sunflower' by Post Malone...")

            if music == "4":
                print("Playing 'Cradles' by Suburban...")

            if music == "5":
                print("Playing 'Enemy' by Imagine Dragons...")

        if option == "5":
            print("Playing Movies...")


# Payment options function
def payment_options():
    print("Select your payment method:")
    print("1. Credit card")
    print("2. Debit card")
    print("3. PayPal")
    payment_method = input("Enter your choice: ")
    print("You have selected {} as your payment method.".format(payment_method))
    currency = input("Select your currency:\ncedis\ndollars\neuros\npound\nYen\nAUD\nCAD\n")
    if currency == "cedis":
        print("You have selected {} as your currency.".format(currency))
    if currency == "dollars":
        print("You have selected {} as your currency.".format(currency))
    if currency == "euros":
        print("You have selected {} as your currency.".format(currency))
    if currency == "pound":
        print("You have selected {} as your currency.".format(currency))
    if currency == "Yen".lower():
        print("You have selected {} as your currency.".format(currency))
    if currency == "AUD".lower():
        print("You have selected {} as your currency.".format(currency))
    if currency == "CAD".lower():
        print("You have selected {} as your currency.".format(currency))
    return payment_method, currency


# Transportation services function
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

        print("Do you want to add in-app entertainment? (yes/no)")
        in_app_entertainment_choice = input()

        if in_app_entertainment_choice == "yes":
            print("The in-app entertainment options include movies, TV shows, music, and games.")
            print("Do you want to play a game? (yes/no)")
            game_choice = input()

            if game_choice == "yes":
                print("The available games are:")
                print("1. Rock Paper Scissors")
                print("2. tic tac toe")
                game_choice = input("Enter the number of the game you want to play: ")

                if game_choice == "1":
                    print("Let's play Rock Paper Scissors!")
                    while True:
                        user_choice = input("What is your choice? (rock/paper/scissors): ")
                        computer_choice = "rock" or "paper" or "scissors"

                        if user_choice == computer_choice:
                            print("It's a tie!")

                        elif user_choice == "rock" and computer_choice == "scissors":
                            print("You win!")

                        elif user_choice == "paper" and computer_choice == "rock":
                            print("You win!")

                        elif user_choice == "scissors" and computer_choice == "paper":
                            print("You win!")

                        else:
                            print("You lose!")

                        play_again = input("Do you want to play again? (yes/no): ")

                        if play_again == "no":
                            return

                        if play_again == "yes":
                            return

                if game_choice == "2":
                    tic_tac_toe_game()


def tic_tac_toe_game():
    # Define the Tic Tac Toe game logic here
    board = [" " for _ in range(9)]
    current_player = "X"
    game_over = False

    def print_board():
        # 'range(0, 9, 3) '
        # generates a sequence of numbers starting from 0, incrementing by 3, and stopping just before reaching 9.
        for i in range(0, 9, 3):
            print(" | ".join(board[i:i + 3]))
            if i < 6:
                print("-" * 9)

    def check_winner(player):
        # Check rows, columns, and diagonals for a win
        return (
                (board[0] == board[1] == board[2] == player) or
                (board[3] == board[4] == board[5] == player) or
                (board[6] == board[7] == board[8] == player) or
                (board[0] == board[3] == board[6] == player) or
                (board[1] == board[4] == board[7] == player) or
                (board[2] == board[5] == board[8] == player) or
                (board[0] == board[4] == board[8] == player) or
                (board[2] == board[4] == board[6] == player)
        )

    while not game_over:
        print("\nTic Tac Toe Game\n")
        print_board()
        position = input(f"Player {current_player}, choose a position (1-9): ")

        if position.isdigit() and 1 <= int(position) <= 9 and board[int(position) - 1] == " ":
            board[int(position) - 1] = current_player

            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                game_over = True
            elif " " not in board:
                print_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid input. Please choose a valid empty position.")
            return


# Define the tic_tac_toe_game() and entertainment() functions as before

# Main program

users = []

print("Welcome to Vankem's Global Movement App\nTRANSPORTATION MADE EASIER!\n")
print("Register and login to use the app")

while True:
    choice = input("Choose an option:\n1. Register\n2. Login\n3. Exit\n")

    if choice == "1":
        registration(users)

    if choice == "2":
        user_data = login(users)
        if user_data:
            current_user = user_data  # Store the current user data
            user_logged_in = True
            # Show payment and entertainment options after successful login
            while user_logged_in:
                choice2 = input("Choose an option:\n1. Payment\n2. Transportation Options\n3. Entertainment\n4. "
                                "Logout\n")
                if choice2 == "1":
                    payment_options()
                elif choice2 == "2":
                    transport_services()
                elif choice2 == "3":
                    entertainment()
                elif choice2 == "4":
                    user_logged_in = False  # Logout the user
                    current_user = None  # Clear current user data
                    print("Logged out successfully!")

    elif choice == "3":
        print("Goodbye!")
        break
