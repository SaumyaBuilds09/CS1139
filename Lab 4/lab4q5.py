n = float(input("Enter distance in km: "))
time = input("Enter day or night: ")
if time == "day":
    taxi = 33.58 + 37.89 * n
else:
    taxi = 33.58 + 43.17 * n
cheapest = taxi
if n >= 20:
    bus = 4.32 * n
    if bus < cheapest:
        cost = bus
if n >= 100:
    train = 2.88 * n
    if train < cost:
        cheapest = train

print("Minimum cost =", cost) 