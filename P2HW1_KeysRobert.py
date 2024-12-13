# Robert Keys
# 10/10/2024
# P2HW1
# Roadtrip expense sheet

def calculate_expenses():
    # Print introduction
    print("This program calculates and displays travel expenses")
    print()

    # Get user input to create expense sheet
    budget = float(input("Enter Budget: "))
    destination = input("Enter your travel destination: ")
    gas = float(input("How much do you think you will spend on gas? "))
    accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
    food = float(input("Last, how much do you need for food? "))

    # Calculate total expenses and remaining balance
    total_expenses = gas + accommodation + food
    remaining_balance = budget - total_expenses

    # Display the results of user input
    print()
    print("-----------Travel Expenses-----------")
    print(f"Location:           {destination:>0}")
    print(f"Initial Budget:     {'$':>0}{budget:>0.2f}")
    print(f"Fuel:               {'$':>0}{gas:>0.2f}")
    print(f"Accommodation:      {'$':>0}{accommodation:>0.2f}")
    print(f"Food:               {'$':>0}{food:>0.2f}")
    print("---------------------------------------")
    print(f"Remaining Balance:  {'$':>0}{remaining_balance:>0.2f}")

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    calculate_expenses()
