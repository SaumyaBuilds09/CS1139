password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    elif ch != " ":
        special = True

count = upper + lower + digit + special

if len(password) < 8:
    print("WEAK")
elif count == 4:
    print("STRONG")
elif count >= 2:
    print("MODERATE")
else:
    print("WEAK")