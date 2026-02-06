text = input("Enter a word: ")

cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
