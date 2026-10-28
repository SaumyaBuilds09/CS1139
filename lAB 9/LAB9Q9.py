n = int(input())

count = {}

for i in range(n):
    first, last = input().lower().split()

    name = first + "." + last

    if name in count:
        count[name] += 1
        email = first + "." + last + str(count[name])
    else:
        count[name] = 1
        email = name

    email += "@jklu.edu.in"

    print(email)