#Robert Keys
#09/19/2024
#P1HW1
#Project is for basic calculations.
print("-----Calculating Exponents-----")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result} !!")

print("\n-----Addition and Subtraction-----")

start = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter an integer to subtract: "))

final_result = start + add - subtract
print(f"{start} + {add} - {subtract} is equal to {final_result}")
