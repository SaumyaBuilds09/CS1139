V = float(input("Enter initial quantity of water: "))
N = int(input("Enter number of days: "))

if V < 0:
    print("Invalid input: Initial quantity cannot be negative")

elif N < 0:
    print("Invalid input: Number of days cannot be negative")

else:
    water = V * (0.95**N) + 200 * (1 - (0.95 ** N))
    print(f"Quantity of water after {N} days = {water:.2f} litres") 