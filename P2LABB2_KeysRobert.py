vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicles.keys()

print("Available vehicles:", keys)

vehicle = input("Enter one of the vehicles from the list: ")

if vehicle in vehicles:
    mpg = vehicles[vehicle]
    print(f"The MPG for {vehicle} is {mpg}")
else:
    print("Vehicle not found in the list.")
    exit()

miles = float(input("Enter the number of miles you will drive: "))

gallons = miles / mpg

print(f"Gallons of gas needed: {gallons:.2f}")
