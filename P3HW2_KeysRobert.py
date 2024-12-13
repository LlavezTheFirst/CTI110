#Robert Keys
#10/23/2024
#P3HW2
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

def calculate_employee_pay():
   # Get employee information
   name = input("Enter employee's name: ")
   hours = float(input("Enter number of hours worked: "))
   rate = float(input("Enter employee's pay rate: "))
   
   # Calculate overtime
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
   
   # Display results
   print("-" * 90)
   print(f'Employee name:\t{name}')
   print()
   print(f'Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay')
   print("-" * 90)
   print(f'{hours:<12.1f}{rate:<12.1f}{overtime_hours:<12.1f}${overtime_pay:<12.2f}${regular_pay:<12.2f}${gross_pay:<12.2f}')

# Call the function
calculate_employee_pay()
