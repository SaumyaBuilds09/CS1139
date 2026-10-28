s = input("Enter a paragraph: ")

digits = 0
alphabets = 0
uppercase = 0
lowercase = 0
special = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alphabets += 1

        if ch.isupper():
            uppercase += 1
        elif ch.islower():
            lowercase += 1
    else:
        special += 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Uppercase alphabets:", uppercase)
print("Lowercase alphabets:", lowercase)
print("Special characters:", special)