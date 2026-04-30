# Create the rgb_color tuple
rgb_color = (255, 128, 0)

# Print each value individually using indexing
print("Red:  ", rgb_color[0])
print("Green:", rgb_color[1])
print("Blue: ", rgb_color[2])

# Create a palette list and add the tuple to it
palette = []
palette.append(rgb_color)

# Show the palette list
print("Palette:", palette)
# Create a tuple of student records
student1 = ("Alice", 90, 20)
student2 = ("Brian", 85, 19)
student3 = ("Chloe", 92, 21)

# Store them in a list called classroom
classroom = [student1, student2, student3]

# Print the name of the second student using double subscripting
print("Second student's name:", classroom[1][0])

# Unpack the first student's information
name, grade, age = classroom[0]

# Print a formatted message
print(f"First student: {name} is {age} years old and has a grade of {grade}.")
# Create the original tuple with mutable + immutable data
student_record = ("Alex", [88, 92, 79], 0)   # final_grade starts as 0

print("Original tuple:", student_record)

# Add a fourth exam score to the list inside the tuple
student_record[1].append(85)

# Calculate the new average
exams = student_record[1]
average = sum(exams) / len(exams)

# Create a NEW updated tuple (because tuples are immutable)
updated_record = (student_record[0], exams, average)

print("Updated tuple:", updated_record)
