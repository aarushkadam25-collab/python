char = input("Enter a character: ")

if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print("The character", char, "is an alphabet.")
else:
    print("The character", char, "is not an alphabet.")