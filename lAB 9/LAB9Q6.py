menu = input().split()
prices = list(map(int, input().split()))
orders = input().split()

total = 0

for i in range(len(menu)):
    quantity = 0

    for item in orders:
        if item == menu[i]:
            quantity += 1

    if quantity > 0:
        cost = quantity * prices[i]
        print(menu[i], "x", quantity, "=", cost)
        total += cost

print("Total:", total)