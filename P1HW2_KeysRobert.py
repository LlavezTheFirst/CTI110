# Robert Keys
# 09/20/2024
# P1HW2
# Roadtrip expense sheet

# Pseudocode:
# 1. Define a function to calculate travel expenses
# 2. Print introduction message
# 3. Get user input for budget, destination, and expenses
# 4. Calculate total expenses and remaining balance
# 5. Display all the information in a formatted output

def calculate_expenses():
    # Print introduction
    print("This program calculates and displays travel expenses")
    
    # Get user input
    budget = float(input("Enter Budget: "))
    destination = input("Enter your travel destination: ")
    gas = float(input("How much do you think you will spend on gas? "))
    accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
    food = float(input("Last, how much do you need for food? "))
    
    # Calculate total expenses and remaining balance
    total_expenses = gas + accommodation + food
    remaining_balance = budget - total_expenses
    
    # Display formatted output
    print("\n" + "-" * 10 + "Travel Expenses" + "-" * 10)
    print(f"Location: {destination}")
    print(f"Initial Budget: {budget:.2f}")
    print()
    print(f"Fuel: {gas:.2f}")
    print(f"Accommodation: {accommodation:.2f}")
    print(f"Food: {food:.2f}")
    print()
    print(f"Remaining Balance: {remaining_balance:.2f}")

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    calculate_expenses()
