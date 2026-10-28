numbers = list(map(int, input().split()))

result = []
zeros = 0

for n in numbers:
    if n == 0:
        zeros += 1
    else:
        result.append(n)

for i in range(zeros):
    result.append(0)

print(result)