#Robert Keys
#10/10/2024
#P2HW2
#Grade Caclulator

def calculate_grades():
    # Print introduction
    print("This program calculates and displays grades for CTI110")
    print()
    
    #Gets user info for modules grades
    Module_1 = float(input("Enter grade for Module 1: "))
    Module_2 = float(input("Enter grade for Module 2: "))
    Module_3 = float(input("Enter grade for Module 3: "))
    Module_4 = float(input("Enter grade for Module 4: "))
    Module_5 = float(input("Enter grade for Module 5: "))
    Module_6 = float(input("Enter grade for Module 6: "))

    #Calculates the grades for output
    Grades = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]
    Sum_of_Grades = sum(Grades)
    Average = Sum_of_Grades / 6
    Lowest_Grade = min(Grades)
    Highest_Grade = max(Grades)

    #Displays the results of user input
    print(f"------------Results------------")
    print(f"Lowest Grade:\t{Lowest_Grade:.1f}")
    print(f"Highest Grade:\t{Highest_Grade:.1f}")
    print(f"Sum of Grades:\t{Sum_of_Grades:.1f}")
    print(f"Average:\t{Average:.2f}")
    print("------------------------------")

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    calculate_grades()
