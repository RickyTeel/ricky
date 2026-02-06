first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
birth_year = int(input("Enter your birth year: "))
hobby = input("Enter your favorite hobby: ")

age = 2026 - birth_year

print("\n--- Profile Card ---")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Favorite Hobby: {hobby}")
print("---------------------")
print("=== TEXT ANALYZER ===")

# 1. Ask the user for a sentence
sentence = input("Enter a sentence: ")

print("\n--- Analysis Results ---")

# 2. Total characters (with spaces)
total_with_spaces = len(sentence)

# 3. Total characters (without spaces)
total_without_spaces = len(sentence.replace(" ", ""))

# 4. Number of words
words = sentence.split()
num_words = len(words)

# 5. Number of vowels (case-insensitive)
vowels = "aeiou"
vowel_count = sum(1 for char in sentence.lower() if char in vowels)

# 6. Uppercase version
upper_version = sentence.upper()

# 7. Lowercase version
lower_version = sentence.lower()

# 8. Reversed sentence
reversed_sentence = sentence[::-1]

# 9. Starts with capital?
starts_with_capital = sentence[0].isupper() if sentence else False

# 10. Ends with punctuation?
ends_with_punctuation = sentence.endswith((".", "!", "?"))

# Display results
print(f"Total characters (with spaces): {total_with_spaces}")
print(f"Total characters (without spaces): {total_without_spaces}")
print(f"Number of words: {num_words}")
print(f"Number of vowels: {vowel_count}")
print(f"Uppercase version: {upper_version}")
print(f"Lowercase version: {lower_version}")
print(f"Reversed: {reversed_sentence}")
print(f"Starts with capital: {'Yes' if starts_with_capital else 'No'}")
print(f"Ends with punctuation: {'Yes' if ends_with_punctuation else 'No'}")
