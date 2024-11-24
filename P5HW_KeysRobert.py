#Robert Keys
#11/21/2024
#P5HW
#MathQuiz

import random

def generate_numbers():
    """Generate two random numbers between 0 and 999"""
    return random.randint(0, 999), random.randint(0, 999)

def play_addition_game():
    """Function to handle addition game logic"""
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    guesses = 0
    
    print(f"{num1:3d}")
    print(f"+{num2:3d}")
    
    while True:
        try:
            guess = int(input("Enter answer: "))
            guesses += 1
            
            if guess == correct_answer:
                print("Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
                break
            elif guess < correct_answer:
                print("Sorry, guess is too low.")
                print("\nTry again: ", end="")
            else:
                print("Sorry, guess is too high.")
                print("\nTry again: ", end="")
        except ValueError:
            print("Please enter a valid number.")
            
def play_subtraction_game():
    """Function to handle subtraction game logic"""
    num1, num2 = generate_numbers()
    # Ensure first number is larger to avoid negative results
    if num2 > num1:
        num1, num2 = num2, num1
    correct_answer = num1 - num2
    guesses = 0
    
    print(f"{num1:3d}")
    print(f"-{num2:3d}")
    
    while True:
        try:
            guess = int(input("Enter answer: "))
            guesses += 1
            
            if guess == correct_answer:
                print("Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
                break
            elif guess < correct_answer:
                print("Sorry, guess is too low.")
                print("\nTry again: ", end="")
            else:
                print("Sorry, guess is too high.")
                print("\nTry again: ", end="")
        except ValueError:
            print("Please enter a valid number.")

def display_menu():
    """Display the main menu"""
    print("\nWelcome to Math Quiz")
    print("\nMAIN MENU")
    print("-----------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print("\nPlease choose one of the menu options: ", end="")

def main():
    while True:
        display_menu()
        try:
            choice = input()
            
            if choice == "1":
                play_addition_game()
            elif choice == "2":
                play_subtraction_game()
            elif choice == "3":
                print("Thank you for playing...")
                print("Bye!!")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
