# Ask for the user's weight
weight = float(input("Enter your weight: "))

# Ask for the unit system (case-sensitive)
unit = input("Enter unit system (M for Metric, I for Imperial): ")

# Validate the unit system (must be exactly M or I)
if unit != "M" and unit != "I":
    print("Invalid Unit")
else:
    # Ask for height only if unit is valid
    height = float(input("Enter your height: "))

    if unit == "M":
        print(f"Weight: {weight} kg")
        print(f"Height: {height} meters")

    elif unit == "I":
        print(f"Weight: {weight} lbs")
        print(f"Height: {height} inches")
