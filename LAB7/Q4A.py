s = input("Enter a sentence: ")

alphabet = "abcdefghijklmnopqrstuvwxyz"
pangram = True

for ch in alphabet:
    found = False

    for c in s:
        if c == ch or c == chr(ord(ch) - 32):
            found = True
            break

    if not found:
        pangram = False
        break

if pangram:
    print("The string is a pangram")
else:
    print("The string is not a pangram")