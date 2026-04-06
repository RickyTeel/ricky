# Problem 1: Temperature Converter

temp = float(input("Enter temperature: "))
scale = input("Enter scale (C/F): ").strip().upper()

if scale == "C":
    # Celsius to Fahrenheit
    f = temp * 9 / 5 + 32
    print(f"{temp:.1f}°C = {f:.1f}ºF")
elif scale == "F":
    # Fahrenheit to Celsius
    c = (temp - 32) * 5 / 9
    print(f"{temp:.1f}ºF = {c:.1f}℃")
else:
    print("Invalid scale.")
# Problem 2: String Analyzer

sentence = input("Enter a sentence: ")

total_chars = len(sentence)
upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0

# Count character types
for ch in sentence:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
    elif ch.isdigit():
        digit_count += 1
    if ch == " ":
        space_count += 1

reversed_sentence = sentence[::-1]

print(f"Total characters: {total_chars}")
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
print(f"Reversed: {reversed_sentence}")
# Problem 3: List Operations Toolkit

numbers = [15, 8, 23, 42, 4, 16, 31, 7, 19, 11]

# 1. Original list
print("Original:", numbers)

# 2. First and last elements
print(f"First: {numbers[0]}, Last: {numbers[len(numbers) - 1]}")

# 3. Middle 4 elements (indices 3-6)
middle_slice = numbers[3:7]
print("Middle 4:", middle_slice)

# 4. Append 99
numbers.append(99)
print("After append 99:", numbers)

# 5. Insert 0 at beginning
numbers.insert(0, 0)
print("After insert 0 at start:", numbers)

# 6. Remove 42
numbers.remove(42)
print("After remove 42:", numbers)

# 7. Pop last element
popped = numbers.pop()
print("Popped last:", popped)
print("After pop:", numbers)

# 8. Check if 23 is in list
print(23 in numbers)

# 9. Index of 16
print("Index of 16:", numbers.index(16))

# 10. Final list and length
print("Final list:", numbers)
print("Length:", len(numbers))
# Problem 4: Course Eligibility Checker

gpa = float(input("Enter GPA (0.0-4.0): "))
credits = int(input("Enter credit hours completed: "))
prereq_input = input("Prerequisite completed? (yes/no): ").strip().lower()

prereq_completed = (prereq_input == "yes")

# Determine status using if-elif-else
if gpa >= 3.5 and credits >= 60 and prereq_completed:
    status = "Approved: You meet all requirements."
elif gpa >= 3.5 and credits >= 60 and not prereq_completed:
    status = "Conditionally approved: Complete the prerequisite first."
elif gpa >= 3.0 and credits >= 45:
    status = "Waitlisted: You may be admitted if space is available."
elif gpa >= 2.0:
    status = "Not eligible yet: Raise your GPA or earn more credits."
else:
    status = "Denied: GPA is below minimum threshold."

# Summary report
print("--- Registration Summary ---")
print(f"GPA: {gpa:.2f}")
print(f"Credits: {credits}")
print(f"Prerequisite: {'Yes' if prereq_completed else 'No'}")
print(f"Status: {status}")
# Problem 5: Student Roster Manager

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 72, 95, 64, 81]

# Task 1: Print formatted roster
print("=== CLASS ROSTER ===")
for i in range(len(names)):
    print(f"{i + 1}. {names[i]} - {scores[i]}")

# Task 2: Find highest and lowest scores (no max/min)
highest_index = 0
lowest_index = 0

for i in range(1, len(scores)):
    if scores[i] > scores[highest_index]:
        highest_index = i
    if scores[i] < scores[lowest_index]:
        lowest_index = i

print(f"Highest: {names[highest_index]} - {scores[highest_index]}")
print(f"Lowest: {names[lowest_index]} - {scores[lowest_index]}")

# Task 3: Class average
total = 0
for s in scores:
    total += s
average = total / len(scores)
print(f"Class average: {average:.2f}")

# Task 4: Letter grades
print("Grade Report -")
for i in range(len(names)):
    score = scores[i]
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score <= 89:
        grade = "B"
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "D"
    else:
        grade = "F"
    print(f"{names[i]}: {score} -> {grade}")

# Task 5: Add Frank, remove Diana
names.append("Frank")
scores.append(77)

# Find index of Diana and remove from both lists
diana_index = names.index("Diana")
names.pop(diana_index)
scores.pop(diana_index)

print("Updated roster length:", len(names))
