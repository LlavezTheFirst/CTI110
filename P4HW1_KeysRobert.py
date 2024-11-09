# Robert Keys
# 11/03/2024
# P4HW1
# Grade Calculator

def calculate_grades():
    """
    PSEUDOCODE:
    1. START program
    2. Display introduction message
    3. PROMPT user for number of scores to enter
    4. VALIDATE number of scores is positive
    5. CREATE empty list for storing scores
    6. FOR each score needed:
        a. PROMPT user for score
        b. WHILE score is invalid:
            - CHECK if score is between 0-100
            - IF invalid, display error and ask again
        c. ADD valid score to list
    7. CALCULATE results:
        - Find lowest score
        - Remove lowest score
        - Calculate average of remaining scores
        - Determine letter grade
    8. DISPLAY all results
    9. END program
    """
    
    # Print introduction
    print("This program calculates and displays grades")
    print()
    
    # Get number of scores from user and validate
    while True:
        try:
            num_scores = int(input("How many scores do you want to enter? "))
            if num_scores > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Initialize empty list for scores
    student_scores = []
    
    # Collect and validate scores
    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score #{i+1}: "))
                # Validate score is between 0 and 100
                if 0 <= score <= 100:
                    student_scores.append(score)
                    break
                else:
                    print("\nINVALID Score entered!!!!")
                    print("Score should be between 0 and 100")
                    input(f"Enter score #{i+1} again: ")
            except ValueError:
                print("\nINVALID Score entered!!!!")
                print("Score should be between 0 and 100")
                input(f"Enter score #{i+1} again: ")
    
    # Process scores and calculate results
    if student_scores:
        # Find lowest score
        lowest_score = min(student_scores)
        
        # Remove lowest score
        modified_scores = student_scores.copy()
        modified_scores.remove(lowest_score)
        
        # Calculate average of modified list
        average = sum(modified_scores) / len(modified_scores)
        
        # Determine letter grade based on average
        if average >= 90:
            letter_grade = 'A'
        elif average >= 80:
            letter_grade = 'B'
        elif average >= 70:
            letter_grade = 'C'
        elif average >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        
        # Display final results
        print("\n------------Results------------")
        print(f"Lowest Score: {lowest_score:.1f}")
        print(f"Scores after dropping lowest: {[round(score, 1) for score in modified_scores]}")
        print(f"Average: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print("------------------------------")

# Entry point of program
if __name__ == "__main__":
    calculate_grades()
