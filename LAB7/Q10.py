s = input("Enter hyphen-separated words: ")
words = s.split("-")

n = len(words)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if words[j] > words[j + 1]:
            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp

result = ""

for i in range(n):
    if i > 0:
        result += "-"
    result += words[i]

print(result)