N = int(input("Enter a positive integer N: "))
if N <= 0:
    print("N must be a positive integer.")
else:
    divisible_count = 0
    not_divisible_count = 0  
    while True:
        num = int(input("Enter a number (-999 to stop): "))       
        if num == -999:
            break     
        if num % N == 0:
            divisible_count += 1
        else:
            not_divisible_count += 1
    print("Divisible numbers count =", divisible_count)
    print("Not divisible numbers count =", not_divisible_count)