s = input("Enter a string: ")
shift = int(input("Enter shift value: "))

result = ""

for ch in s:
    if 'a' <= ch <= 'z':
        result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':
        result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

print("Encrypted string:", result)