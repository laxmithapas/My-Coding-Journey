user_input = input('Enter the numbers serparated by space: ')

numbers = list(map(int, user_input.split()))
smallest_number = numbers[0]
for number in numbers:
    if number < smallest_number:
        smallest_number = number
print('The smallest number is', smallest_number)
