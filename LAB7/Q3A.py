s = input("Enter a sentence: ")
word = input("Enter the word to search: ")

count = s.count(word)

if word in s:
    print("Word is present")
else:
    print("Word is not present")

print("Occurrences:", count)