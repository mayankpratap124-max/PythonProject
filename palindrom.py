text = input("Enter any word:")

original = text
reverse = text[::-1]
print(reverse)
if original == reverse:
    print("This is the palidrom word.")
else:
    print("This is not palindrom word")

#OR

if text == text[::-1]:
    print("This is a palindrom")
else:
    print("This is not a plindrom word")