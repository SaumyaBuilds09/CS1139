message = input("Enter message: ")
k = int(input("Enter K: "))

result = ""

for ch in message:
    if ch == " ":
        result += " "
    else:
        new_char = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        result += new_char

print(result)