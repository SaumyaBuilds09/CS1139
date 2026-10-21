seconds = int(input("Enter the number of seconds 1-86400 "))
if seconds < 1 or seconds > 86400:
    print("Invalid Input")
else:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    print(f"{hours}:{minutes}:{secs}")