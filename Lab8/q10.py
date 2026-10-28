s = input("Enter a string: ")

if len(s) == 0:
    print("String is empty")
else:
    max_char = s[0]
    max_count = 1

    current_char = s[0]
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            current_count += 1
        else:
            current_char = s[i]
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            max_char = current_char

    print(max_char, max_count)