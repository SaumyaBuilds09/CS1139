plate = input("Enter number plate: ")

valid = True

if len(plate) != 10:
    valid = False
else:
    if plate[0:2] != "RJ":
        valid = False

    if not plate[0].isupper() or not plate[1].isupper():
        valid = False

    if not plate[2:4].isdigit():
        valid = False

    if not plate[4:6].isupper():
        valid = False

    if not plate[6:10].isdigit():
        valid = False

    for ch in plate[0:2] + plate[4:6]:
        if not ch.isalpha():
            valid = False

print(valid)