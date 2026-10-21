hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))

minutes = minutes + 15

if minutes >= 60:
    minutes = minutes - 60
    hours = hours + 1

if hours == 24:
    hours = 0

print(hours,":",f"{minutes:02d}")