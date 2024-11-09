#Robert Keys
#11/05/2024
#P4HW2
#Work Pay
# Pseudocode:
# 1. Define function to calculate employee pay
#    Input: none - will get user input inside function
#    Output: displays formatted pay information
#
# 2. Get employee information
#    - Prompt for and store employee name
#    - Prompt for and store hours worked (convert to float)
#    - Prompt for and store hourly pay rate (convert to float)
#
# 3. Calculate overtime hours and pay
#    If hours > 40 then
#        overtime_hours = hours - 40
#        regular_hours = 40
#    Else
#        overtime_hours = 0
#        regular_hours = hours worked
#    overtime_pay = overtime_hours * (rate * 1.5)
#
# 4. Calculate regular and gross pay
#    regular_pay = regular_hours * rate
#    gross_pay = regular_pay + overtime_pay
#
# 5. Display results in formatted table
#    - Print employee name
#    - Print column headers
#    - Print calculated values aligned in columns
def main():
    # Initialize accumulator variables
    total_employees = 0
    total_overtime = 0
    total_regular = 0
    total_gross = 0
    
    while True:
        # Get employee name and check for sentinel
        name = input("Enter employee's name or \"Done\" to terminate: ")
        if name.lower() == "done":
            break
            
        # Get hours and pay rate
        hours = float(input(f"How many hours did {name} work? "))
        rate = float(input(f"What is {name}'s pay rate? "))
        
        # Calculate overtime and regular hours
        if hours > 40:
            overtime_hours = hours - 40
            regular_hours = 40
        else:
            overtime_hours = 0
            regular_hours = hours
            
        # Calculate pay
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = regular_hours * rate
        gross_pay = regular_pay + overtime_pay
        
        # Update running totals
        total_employees += 1
        total_overtime += overtime_pay
        total_regular += regular_pay
        total_gross += gross_pay
        
        # Display individual employee results
        print()
        print(f"Employee name:\t{name}")
        print()
        print("Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
        print("-" * 90)
        print(f"{hours:<12.1f}{rate:<12.2f}{overtime_hours:<12.1f}${overtime_pay:<11.2f}\t${regular_pay:<11.2f}\t${gross_pay:<11.2f}")
        print()
    
    # Display final totals only if at least one employee was entered
    if total_employees > 0:
        print()
        print(f"Total number of employees entered: {total_employees}")
        print(f"Total amount paid for overtime: ${total_overtime:.2f}")
        print(f"Total amount paid for regular hours: ${total_regular:.2f}")
        print(f"Total amount paid in gross: ${total_gross:.2f}")

if __name__ == "__main__":
    main()
