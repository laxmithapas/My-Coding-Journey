num = int(input("Enter the number :"))


factorial = 1

current = num

while current > 0 :
    factorial *= num
    current -= 1

print(f"The factorial of {num} is {factorial}")