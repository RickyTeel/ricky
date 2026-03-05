# Problem 1: Boolean Expression Evaluator

# 1. Ask the user for three integer values
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

# 2. Evaluate the expressions
expr1 = a < b < c                     # Chained comparison
expr2 = not (a > b or b > c)          # De Morgan's candidate
expr3 = a <= b and b <= c             # Equivalent form

# 3. Print results
print(f"a < b < c            : {expr1}")
print(f"not (a > b or b > c) : {expr2}")
print(f"a <= b and b <= c    : {expr3}")

# 4. Confirm De Morgan's Law
if expr2 == expr3:
    print("De Morgan's confirmed: Expressions 2 and 3 match!")
else:
    print("De Morgan's NOT confirmed: Expressions 2 and 3 differ.")

# Weather Advisory System

# Ask for inputs
temp = int(input("Enter the current temperature (°F): "))
raining = input("Is it raining (yes/no)? ").strip().lower()
is_raining = (raining == "yes")

# Temperature-based if-elif-else chain
if temp > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")

elif temp > 85:
    # Nested rain logic
    if is_raining:
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")

elif 60 <= temp <= 85:
    # Nested rain logic
    if is_raining:
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")

elif 32 <= temp < 60:
    print("It's cold — bundle up!")

else:  # temp < 32
    print("FREEZE WARNING: Roads may be icy!")

# Student Grade Report Program

# 1. Ask for student name and exam scores
name = input("Enter student name: ")
exam1 = float(input("Enter Exam 1 score: "))
exam2 = float(input("Enter Exam 2 score: "))
exam3 = float(input("Enter Exam 3 score: "))

# 2. Calculate average
average = (exam1 + exam2 + exam3) / 3

# 3. Determine letter grade using CS 1300 syllabus scale
if average >= 90:
    grade = "A"
elif average >= 87:
    grade = "A-"
elif average >= 83:
    grade = "B+"
elif average >= 80:
    grade = "B"
elif average >= 77:
    grade = "B-"
elif average >= 73:
    grade = "C+"
elif average >= 70:
    grade = "C"
elif average >= 67:
    grade = "C-"
elif average >= 63:
    grade = "D+"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# 4. Determine academic standing
if average >= 90:
    status = "Dean's List"
elif average >= 70:
    status = "Good Standing"
elif average >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

# 5. Print formatted grade report
print("============================")
print("    STUDENT GRADE REPORT")
print("============================")
print(f"Student: {name}")
print(f"Exam 1:  {exam1}")
print(f"Exam 2:  {exam2}")
print(f"Exam 3:  {exam3}")
print("----------------------------")
print(f"Average: {average:.2f}")
print(f"Grade:   {grade}")
