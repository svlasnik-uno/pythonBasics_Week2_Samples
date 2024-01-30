# python3
# Sample Python program to calculate and display the future value of an investment
# This sample program uses conditional and repetition statements and a Python function
        
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    print ("Entering calculate_future_value() function")
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value and display current value for each iteration of the loop (round to 2 digits)
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
        print("Month =", i+1, "future value = $", str(round(future_value, 2)))
    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = float(input("Enter monthly investment:\t"))
        yearly_interest_rate = float(input("Enter yearly interest rate (i.e. 5% -> enter 5.0):\t"))
        years = int(input("Enter number of years:\t\t"))
        if monthly_investment <= 0 or yearly_interest_rate <= 0 or years <= 0:
            print("All values must be positive - try again")

        else:
            # get and display future value
            future_value = calculate_future_value(
                monthly_investment, yearly_interest_rate, years)

            print("Final Future value:\t\t\t$ " + str(round(future_value, 2)))
            print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
