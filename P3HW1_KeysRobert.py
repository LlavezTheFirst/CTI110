# Robert Keys
# 10/19/2024
# P3HW1
# Grade Calculator fix

def calculate_grades():
    # Display introduction
    # Print welcome message
    print("This program calculates and displays grades for CTI110")
    print()
    
    # Initialize empty list to store grades
    # Create an empty list called grades
    grades = []

    # Loop 6 times to get grades for 6 modules
    # For each module from 1 to 6:
    for i in range(1, 7):
        # Keep asking for input until a valid grade is entered
        # While we don't have a valid grade:
        while True:
            try:
                # Ask for grade input and convert to float
                # Prompt user for grade and store as float
                grade = float(input(f"Enter grade for Module {i}: "))
                # Add grade to list
                # Append grade to grades list
                grades.append(grade)
                # PSEUDOCODE: Exit loop if input is valid
                # Break out of while loop
                break
            except ValueError:
                #Handle invalid input
                # If input is not a valid number, print error message
                print("Please enter a valid number.")
    
    #Calculate grade statistics
    # Find lowest grade in the list
    lowest_grade = min(grades)
    # Find highest grade in the list
    highest_grade = max(grades)
    # Calculate sum of all grades
    sum_of_grades = sum(grades)
    # Calculate average grade
    average = sum_of_grades / len(grades)
    
    #Determine letter grade based on average
    # If average is 90 or above
    if average >= 90:
        letter_grade = 'A'
    else:
        # If average is 80 or above
        if average >= 80:
            letter_grade = 'B'
        else:
            # If average is 70 or above
            if average >= 70:
                letter_grade = 'C'
            else:
                # If average is 60 or above
                if average >= 60:
                    letter_grade = 'D'
                else:
                    # If average is below 60
                    letter_grade = 'F'
    
    # Display results
    # Print header for results
    print("\n------------Results------------")
    # Print lowest grade
    print(f"Lowest Grade:      {lowest_grade:.1f}")
    # Print highest grade
    print(f"Highest Grade:     {highest_grade:.1f}")
    # Print sum of grades
    print(f"Sum of Grades:     {sum_of_grades:.1f}")
    # Print average grade
    print(f"Average:           {average:.2f}")
    # Print separator line
    print("------------------------------")
    # Print final letter grade
    print(f"Your grade is:  {letter_grade}")

# Check if this script is being run directly (not imported)
# If this file is the main program being run:
if __name__ == "__main__":
    # Run the main function
    # Call the calculate_grades function
    calculate_grades()
