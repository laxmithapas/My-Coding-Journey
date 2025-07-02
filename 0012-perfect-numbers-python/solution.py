N = int(input("Enter the upper limit"))

if N < 1 :
    Print("Invalid!")

else:
    print(f"The perefect number between 1 and {N}:")
for num in range(1, N + 1):

    sum_of_divisor = 0

    for i in range(1, num):
        if num % i == 0 :
            sum_of_divisor += i
    
    if sum_of_divisor == num :
        print(num)
        