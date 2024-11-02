#Robert Keys
#11/01/2024
#P4LAB2
#Multiplication chart

def get_number():
    return int(input("Please enter a positive integer: "))

def print_multiplication_table(number):
    print(f"\nMultiplication table for {number}:")
    print("-" * 20)
    
    # Using a for loop for the multiplications 1-12
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    # Using a while loop for program repetition
    while True:
        try:
            number = get_number()
            
            if number < 0:
                print("Sorry, I cannot accept negative values.")
            else:
                print_multiplication_table(number)
            
            # Ask if user wants to continue
            choice = input("\nWould you like to run the program again? (yes/no): ").lower()
            if choice != "yes":
                print("Exiting program...")
                break
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
