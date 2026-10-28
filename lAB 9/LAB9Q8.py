text = input()

digits = []
total = 0

for ch in text:
    if ch >= '0' and ch <= '9':
        digits.append(int(ch))
        total += int(ch)

print(digits)
print("Sum:", total)