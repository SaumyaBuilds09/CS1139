s = input("Enter a sentence: ")
word = input("Enter the word to search: ")

n = len(s)
m = len(word)
count = 0
i = 0

while i <= n - m:
    j = 0

    while j < m and s[i + j] == word[j]:
        j += 1

    if j == m:
        count += 1
        i += m
    else:
        i += 1

if count > 0:
    print("Word is present")
else:
    print("Word is not present")

print("Occurrences:", count)