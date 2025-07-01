start = int(input('Enter the starting number'))
end = int(input('Enter the ending number'))

if start > end or start < 0 or end < 0:
    print("Invalid! not a prime number")
else:
    print("The prime number between", start and end , "are")

    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break
    if is_prime:
        print(num)



        