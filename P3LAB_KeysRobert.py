#Robert Keys
#P3LAB
#10/19/2024
#Money Converter

# Function to convert money amount to its components
def convert_money(amount):
    # PSEUDOCODE:
    # 1. Convert the input amount to cents
    # 2. If the amount is zero, return "No change"
    # 3. Otherwise, calculate the number of each coin type:
    #    - Divide by 100 for dollars
    #    - Divide remainder by 25 for quarters
    #    - Divide remainder by 10 for dimes
    #    - Divide remainder by 5 for nickels
    #    - Remainder is pennies
    # 4. Create output strings for each non-zero coin count
    # 5. Return the list of output strings

    # Convert the amount to cents
    cents = int(amount * 100)
    
    # Check if the amount is zero
    if cents == 0:
        return ["No change"]
    
    # Initialize variables for each coin type
    dollars = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    pennies = cents % 5
    
    # Create the output list
    output = []
    if dollars > 0:
        output.append(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        output.append(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        output.append(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        output.append(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        output.append(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
    
    return output

# PSEUDOCODE for main program:
# 1. Prompt user for input amount
# 2. Call convert_money function with input amount
# 3. Print the original input amount
# 4. Print each component of the converted amount on a new line

# Get user input
user_input = float(input("Enter the amount of money as a float: $"))

# Convert and display the result
result = convert_money(user_input)
for item in result:
    print(item)
