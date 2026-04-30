# FizzBuzz program: prints numbers 1 through 30 with substitutions
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# Multiplication table program for n = 6
n = 6

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # Print each product right-aligned in a 4-character-wide field
        print(f"{i * j:4d}", end=" ")
    print()  # Move to the next row
def unique_preserve_order(lst):
    seen = []          # list to track items already added
    result = []        # list to store unique items in original order

    for item in lst:
        if item not in seen:   # only add if not already seen
            seen.append(item)
            result.append(item)
    return result
def fibonacci(n):
    # Handle base cases first
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Start with the first two numbers
    fib_seq = [0, 1]
    
    # Generate remaining numbers using a loop
    for i in range(2, n):
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)
    
    return fib_seq


# Test cases
print(fibonacci(0))  # []
print(fibonacci(1))  # [0]
print(fibonacci(2))  # [0, 1]
print(fibonacci(6))  # [0, 1, 1, 2, 3, 5]
# Interactive Banking Program
# Manages a single account with a starting balance of $1000.00

balance = 1000.0
history = []

while True:
    print("\n--- Banking Menu ---")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show transaction history")
    print("5. Quit")

    choice = input("Select an option (1-5): ")

    # Handle invalid menu input gracefully
    if not choice.isdigit():
        print("Invalid choice, please select 1-5.")
        continue

    choice = int(choice)

    if choice == 1:
        print(f"Current balance: ${balance:,.2f}")

    elif choice == 2:
        try:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                history.append(("Deposit", amount))
                print(f"Deposited ${amount:,.2f}. New balance: ${balance:,.2f}")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

    elif choice == 3:
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Amount must be positive.")
            elif amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                history.append(("Withdraw", amount))
                print(f"Withdrew ${amount:,.2f}. New balance: ${balance:,.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

    elif choice == 4:
        if not history:
            print("No transactions yet.")
        else:
            print("\nTransaction History:")
            for i, (action, amt) in enumerate(history, start=1):
                print(f"{i}. {action}: ${amt:,.2f}")

    elif choice == 5:
        print(f"Final balance")