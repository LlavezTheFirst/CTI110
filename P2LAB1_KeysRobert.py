#Robert Keys
#09/28/2024
#PLAB2
#Program designed to use mathematical expressions to find values of a circle given the radius.

import math

def calculate_circle_properties(radius):
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    
    return diameter, circumference, area

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        
        diameter, circumference, area = calculate_circle_properties(radius)
        
        print(f"\nFor a circle with radius {radius}:")
        print(f"Diameter: {diameter:.2f}")
        print(f"Circumference: {circumference:.2f}")
        print(f"Area: {area:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
        print("Please enter a valid non-negative number for the radius.")

if __name__ == "__main__":
    main()
