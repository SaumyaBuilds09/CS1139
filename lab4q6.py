holidays = int(input("enter the number of holidays "))

workdays = 365 - holidays

play_time = workdays * 63 + holidays * 127

difference = 30000 - play_time

if play_time <= 30000:
    print("Tom sleeps well")
    print(difference)
else:
    print("Tom will not sleep well")
    print(difference)