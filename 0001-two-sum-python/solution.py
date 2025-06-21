user_input = input("Enter two numbers separated by a space: ")

numbers = list(map(int, user_input.split()))

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print(f"The largest number is: {largest_number}")