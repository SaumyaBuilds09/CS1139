count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
total = 0

while True:
    n = int(input("Enter a number (1-10), or -1 to stop: "))

    if n == -1:
        break

    if n < 1 or n > 10:
        print("Enter a number between 1 and 10")
        continue

    total += 1

    if n <= 2:
        count1 += 1
    elif n <= 4:
        count2 += 1
    elif n <= 6:
        count3 += 1
    elif n <= 8:
        count4 += 1
    else:
        count5 += 1

if total > 0:
    print("1 - 2:", "# " * count1,
          format(count1 * 100 / total, ".2f"), "%")
    print("3 - 4:", "# " * count2,
          format(count2 * 100 / total, ".2f"), "%")
    print("5 - 6:", "# " * count3,
          format(count3 * 100 / total, ".2f"), "%")
    print("7 - 8:", "# " * count4,
          format(count4 * 100 / total, ".2f"), "%")
    print("9 - 10:", "# " * count5,
          format(count5 * 100 / total, ".2f"), "%")
else:
    print("No numbers entered")