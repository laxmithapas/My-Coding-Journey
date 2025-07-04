num = int(input("Enter the number: "))

if num < 0:
    print("Inavlid!")
else:
    reverse = 0

    while num != 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    print("Reveresed number:", reverse)