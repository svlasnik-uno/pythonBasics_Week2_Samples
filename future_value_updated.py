# Sample Program: future_value_updated.py
# Calculates the future value of an investment using a monthly deposit amount, number of years invested, and
# the yearly interest rate entered as a value from 0 to 100.0 (larger values are allowed)
# Program demonstrates: conditional statements, repetition statements, mathematical calculations, python
# functions, and exception handling
# Based on a program file provided with the Python textbook - updated to include error handling

# Function: calculate_future_value
# Inputs: monthly investment, yearly_interest rate, years
# Converts yearly interest rate to monthly interest and converts to a number between 0.0 and 0.99
# Returns the calculated future_value of the investment
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

# Function: getPositiveFloat
# Inputs: prompt to display to the user
# Prompts the user to enter a floating point value. Validates the value is numeric and positive. Errors must be
# corrected before the value is returned.
# Returns a positive floating point number
def getPositiveFloat(prompt):
    value = 0.0
    while (value <= 0):
        try:
            value = float(input(prompt))
            if value <= 0.0:
                print("Value entered must be a positive number greater than 0 - Try again.")
            else:
                return value
        except ValueError:
            print("Value entered must be a positive number greater than 0 - Try again.")


# Function: getPositiveInteger
# Inputs: prompt to display to the user
# Prompts the user to enter an integer value. Validates the value is numeric and positive. Errors must be
# corrected before the value is returned.
# Returns a positive whole number
def getPositiveInteger(prompt):
    value = 0
    while (value <= 0):
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value entered must be a positive, whole number greater than 0 - Try again.")
            else:
                return value
        except ValueError:
            print("Value entered must be a positive, whole number greater than 0 - Try again.")


# Main function
def main():
    choice = "y"

    # user is allowed to calculate the future value of any number of investments
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = getPositiveFloat("Enter monthly investment (Decimal > 0.0):\t")
        yearly_interest_rate = \
            getPositiveFloat("Enter yearly interest rate (Decimal > 0.0 - Format: 5.0% - enter as 5.0):\t")
        years = getPositiveInteger("Enter number of years (Whole number > 0):\t\t")

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print("Future value of investment:\t\t\t$", round(future_value, 2))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()


# start execution at the 'main' function
if __name__ == "__main__":
    main()
