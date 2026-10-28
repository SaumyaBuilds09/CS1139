s = input("Enter a sentence: ")

result = ""

for ch in s:
    found = False

    for c in result:
        if ch == c:
            found = True
            break

    if not found:
        result += ch

print("String after removing duplicates:", result)