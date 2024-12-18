word = input("Write a word:")
if word.lower() == word.lower()[::-1]:
    print(f"Yes, this {word} is a Palindrome ")
else:
    print(f"No, this {word} is not a Palindrome ")
