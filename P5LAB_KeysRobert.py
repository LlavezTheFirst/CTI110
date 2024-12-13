#Robert Keys
#P5LAB
#11/15/2024
#Change give-back calculator

import random

def disperse_change(amount):
    # Convert the amount to cents
    cents = int(amount * 100)
    
    # Check if the amount is zero
    if cents == 0:
        print("No change")
        return
    
    # Calculate each denomination
    dollars = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    pennies = cents % 5
    
    # Print each non-zero denomination matching the example format
    if dollars > 0:
        print(f"{dollars} Dollars" if dollars > 1 else f"{dollars} Dollar")
    if quarters > 0:
        print(f"{quarters} Quarters" if quarters > 1 else f"{quarters} Quarter")
    if dimes > 0:
        print(f"{dimes} Dimes" if dimes > 1 else f"{dimes} Dime")
    if nickels > 0:
        print(f"{nickels} Nickels" if nickels > 1 else f"{nickels} Nickel")
    if pennies > 0:
        print(f"{pennies} Pennies" if pennies > 1 else f"{pennies} Penny")

def main():
    # Generate random purchase amount
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")
    
    # Get payment amount from user
    print("How much cash will you put in the self-checkout?", end=" ")
    payment = float(input())
    
    # Calculate change
    change = payment - amount_owed
    
    # Handle insufficient payment
    if change < 0:
        print(f"Insufficient payment. You still owe ${abs(change):.2f}")
        return
    
    # Display change amount
    print(f"Change is: ${change:.2f}")
    print()  # Add blank line before denominations
    disperse_change(change)

# Call the main function to start the program
if __name__ == "__main__":
    main()
