#program that prompts the user for a number and handles the case where the input is not a valid number.
def get_number_from_user():
    while True:
        user_input = input("Please enter a number: ")
        try:
            number = float(user_input)  # You can use int(user_input) if you want only integers
            print(f"You entered the number: {number}")
            break
        except ValueError:
            print("Oops! That wasn't a valid number. Please try again.")

# Run the function
get_number_from_user()
