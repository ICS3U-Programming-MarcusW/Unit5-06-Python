#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Dec 8 2022
# This program asks the user to enter a decimal
# it then sends it to a function that rounds it


# Function to round decimal
def round_decimal(num_array, dec_places):
    # Calculations for rounding the number
    num_array[0] = num_array[0] * (10**dec_places)
    num_array[0] += 0.5
    num_array[0] = int(num_array[0])
    num_array[0] = num_array[0] / (10**dec_places)


# Function to get the users number
def main():

    # Explain what the program is about
    print("This program rounds decimals to the number of" " decimal places entered.")
    print("")

    # Declare an empty list in order to change the value by reference
    user_num = []

    # Get the users decimal number
    dec_num_string = input("Enter a decimal number: ")

    try:
        # Convert their number to a float
        dec_num_float = float(dec_num_string)

        # Add the users number to the list
        user_num.append(dec_num_float)

        # Get number of decimal places
        dec_places_string = input("Enter the number of decimal places: ")

        try:
            # Convert the number of decimal numbers to an integer
            dec_places_int = int(dec_places_string)

            # Check if the number is negative
            if dec_places_int < 0:
                # Tell them if it isn't
                print("{} is not a positive integer.".format(dec_places_int))
            else:

                # Call the function that rounds the number
                round_decimal(user_num, dec_places_int)
                # Display the rounded number
                print(
                    "{} rounded to {} decimals is {}".format(
                        dec_num_float, dec_places_int, user_num[0]
                    )
                )

        # Message fro invalid input on second conversion
        except Exception:
            print("Invalid input!")

    # Message fro invalid input on first conversion
    except Exception:
        print("{} is not a decimal number".format(dec_num_string))


if __name__ == "__main__":
    main()
