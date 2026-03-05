# Ask for the user's weight
weight = float(input("Enter your weight: "))

# Ask for the unit system (case-insensitive)
unit = input("Enter unit system (M for metric, I for imperial): ")

# Validate unit system
if unit.upper() != "M" and unit.upper() != "I":
    print("Invalid unit system.")
else:
    # Ask for height only if unit is valid
    height = float(input("Enter your height: "))

    # Metric BMI calculation
    if unit.upper() == "M":
        bmi = weight / (height ** 2)

    # Imperial BMI calculation
    else:  # unit == "I"
        bmi = (weight * 703) / (height ** 2)

    # Format BMI
    bmi_value = float(f"{bmi:.1f}")
    print(f"BMI: {bmi_value}")

    # Determine category
    if bmi_value < 18.5:
        category = "Underweight"
    elif bmi_value < 25.0:
        category = "Normal weight"
    elif bmi_value < 30.0:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Category: {category}")
password = input("Enter a password: ")

# Handle empty password
if password == "":
    print("No password entered")
else:
    # Counters
    upper = 0
    lower = 0
    digit = 0
    special = 0

    # Count character types
    for ch in password:
        if ch.isupper():
            upper
            # Initial data
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"]
quantities = [12, 45, 30, 8, 22]

# 1. Print original inventory as a formatted table
print("=== ORIGINAL INVENTORY ===")
for i in range(len(products)):
    print(f"{i+1}. {products[i]:10} - {quantities[i]}")
print()

# 2. Find highest and lowest
vehicle = input("Enter vehicle type (car, motorcycle, truck): ").lower()
hours = float(input("Enter number of hours parked: "))
has_pass = input("Monthly pass? (yes/no): ").lower()

# Monthly pass = free parking
if has_pass == "yes":
    fee = 0.00

else:
    # Determine fee based on vehicle type and hours
    if vehicle == "motorcycle":
        if hours <= 2:
            fee = 1.00
        else:
            fee = 1.00 + 0.50 * (hours - 2)

    elif vehicle == "car":
        if hours <= 2:
            fee = 3.00
        else:
            fee = 3.00 + 1.50 * (hours - 2)

    elif vehicle == "truck":
        if hours <= 2:
            fee = 5.00
        else:
            fee = 5.00 + 2.50 * (hours - 2)

    else:
        print("Invalid vehicle type.")
        fee = None

# Only print receipt if fee was calculated
if fee is not None:
    print("\n--- Parking Receipt ---")
    print(f"Vehicle: {vehicle.capitalize()}")
    print(f"Duration: {hours} hours")
    print(f"Pass holder: {'Yes' if has_pass == 'yes' else 'No'}")
    print(f"Fee: ${fee:.2f}")
    print("-----------------------")
sentence = input("Enter a sentence: ")

# 1. Convert to lowercase and split into words
sentence = sentence.lower()
words = sentence.split()

# 2. Print total number of words
print("Total words:", len(words))

# 3. Build a list of unique words (no duplicates)
unique_words = []
for w in words:
    if w not in unique_words:
        unique_words.append(w)

print("Unique words:", unique_words)

# 4 & 5. Count frequency of each unique word manually
print("\nWord Frequencies:")
most_freq_word = unique_words[0]
most_freq_count = 0

for uw in unique_words:
    count = 0
    for w in words:
        if w == uw:
            count += 1

    print(f"{uw}: {count}")

    # Track most frequent word
    if count > most_freq_count:
        most_freq_count = count
        most_freq_word = uw

# 6. Print the most frequently used word
print("\nMost frequent word:", most_freq_word)
