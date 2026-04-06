# Problem 1: Movie Ticket Pricing

age_input = input("Enter your age: ")

# Validate age is an integer and non-negative
try:
    age = int(age_input)
except ValueError:
    print("Error: Age must be an integer.")
    exit()

if age < 0:
    print("Error: Age cannot be negative.")
    exit()

matinee_input = input("Is this a matinee showing? (yes/no): ").strip().lower()
# Requirement: use conditional expression to convert to boolean
is_matinee = True if matinee_input == "yes" else False

# Determine age group and price using nested ifs
if age < 13:
    age_group = "Child"
    if is_matinee:
        price = 6.00
    else:
        price = 8.00
elif age <= 17:
    age_group = "Teen"
    if is_matinee:
        price = 7.00
    else:
        price = 10.00
elif age <= 64:
    age_group = "Adult"
    if is_matinee:
        price = 8.00
    else:
        price = 13.00
else:
    age_group = "Senior"
    if is_matinee:
        price = 6.00
    else:
        price = 7.00

print(f"\nAge group: {age_group}")
print(f"Ticket price: ${price:.2f}")
# Problem 2: Input Validator

errors = []

student_id = input("Enter student ID: ").strip()
name = input("Enter full name: ")
age_input = input("Enter age: ")
major_input = input("Enter major: ")

# --- Student ID validation ---
# Exactly 8 chars; first char letter; remaining 7 digits
if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")
if not student_id:
    errors.append("Student ID cannot be empty")
else:
    if not student_id[0].isalpha():
        errors.append("Student ID must start with a letter")
    if len(student_id) >= 2 and not student_id[1:].isdigit():
        errors.append("Student ID must have 7 digits after the first letter")

# --- Name validation ---
if name.strip() == "":
    errors.append("Name cannot be empty")
elif len(name.strip()) < 2:
    errors.append("Name must be at least 2 characters")

# --- Age validation with try/except ---
try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99")
except ValueError:
    errors.append("Age must be a valid integer")

# --- Major validation ---
major = major_input.strip().upper()
valid_majors = ["CS", "IT", "CE", "DS"]
if major not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major_input})")

# --- Final output ---
if not errors:
    print("\n✓ Profile created successfully!")
    print(f"Student ID: {student_id}")
    print(f"Name: {name.strip()}")
    print(f"Age: {age}")
    print(f"Major: {major}")
else:
    print("\n✗ Profile has errors:")
    for e in errors:
        print("-", e)
# Problem 3: Campus Café Menu

TAX_RATE = 0.07

print("CAMPUS CAFÉ ORDER SYSTEM")
print("1. Coffee  - $3.50")
print("2. Sandwich - $6.00")
print("3. Salad   - $5.50")
print("4. Combo   - $8.00")
print("5. Exit")

choice = input("Enter your choice (1-5): ").strip()

if choice == "5":
    print("Goodbye!")
    exit()

item_name = ""
unit_price = 0.0

# --- Coffee ---
if choice == "1":
    base_price = 3.50
    size = input("Size (S/M/L): ").strip().upper()
    if size == "M":
        unit_price = base_price + 1.00
        item_name = "Coffee (Medium)"
    elif size == "L":
        unit_price = base_price + 2.00
        item_name = "Coffee (Large)"
    elif size == "S":
        unit_price = base_price
        item_name = "Coffee (Small)"
    else:
        print("Invalid size, defaulting to Small.")
        unit_price = base_price
        item_name = "Coffee (Small)"

# --- Sandwich ---
elif choice == "2":
    base_price = 6.00
    cheese = input("Add cheese? (yes/no): ").strip().lower()
    if cheese == "yes":
        unit_price = base_price + 0.75
        item_name = "Sandwich + Cheese"
    else:
        unit_price = base_price
        item_name = "Sandwich"

# --- Salad ---
elif choice == "3":
    base_price = 5.50
    dressing = input("Dressing (ranch/italian/vinaigrette/none): ").strip().lower()
    valid_dressings = ["ranch", "italian", "vinaigrette", "none"]
    if dressing not in valid_dressings:
        print("Invalid dressing, defaulting to none.")
        dressing = "none"
    unit_price = base_price
    item_name = f"Salad ({dressing.capitalize()})" if dressing != "none" else "Salad (No dressing)"

# --- Combo ---
elif choice == "4":
    base_price = 8.00
    # Coffee size
    size = input("Coffee size (S/M/L): ").strip().upper()
    coffee_extra = 0.0
    if size == "M":
        coffee_extra = 1.00
    elif size == "L":
        coffee_extra = 2.00
    elif size != "S":
        print("Invalid size, defaulting coffee to Small.")
    # Cheese
    cheese = input("Add cheese to sandwich? (yes/no): ").strip().lower()
    cheese_extra = 0.75 if cheese == "yes" else 0.0

    unit_price = base_price + coffee_extra + cheese_extra
    coffee_label = "Coffee"
    if size == "M":
        coffee_label = "Coffee (Medium)"
    elif size == "L":
        coffee_label = "Coffee (Large)"
    item_name = f"Combo ({coffee_label} + Sandwich{' + Cheese' if cheese == 'yes' else ''})"

else:
    print("Invalid menu choice.")
    exit()

# --- Name and quantity ---
name = input("Enter your name: ").strip()
if name == "":
    print("Error: Name cannot be empty.")
    exit()

qty_input = input("How many? ").strip()
try:
    quantity = int(qty_input)
    if quantity <= 0:
        print("Error: Quantity must be a positive integer.")
        exit()
except ValueError:
    print("Error: Quantity must be a valid integer.")
    exit()

subtotal = unit_price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

print("\nORDER RECEIPT")
print(f"Customer: {name}")
print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("\nThank you for your order!")
