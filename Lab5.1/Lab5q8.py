s = input("Enter a sentence: ")
i = 0
capital = 0
small = 0
digits = 0
special = 0
while i < len(s):
    ch = s[i]
    if ch >= 'A' and ch <= 'Z':
        capital = capital + 1
    elif ch >= 'a' and ch <= 'z':
        small = small + 1
    elif ch >= '0' and ch <= '9':
        digits = digits + 1
    else:
        special = special + 1
    i = i + 1
print("Capital letters =", capital)
print("Small letters =", small)
print("Digits =", digits)
print("Special characters =", special)
