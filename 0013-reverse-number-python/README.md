# Reverse a Number

This program takes a positive integer from the user and prints its reverse.

## Example

Input:
7890

Output:
0987

## Note

- If the user enters a number less than 0, the program will display:
  Invalid input. Please enter a positive number.

## Logic Used

- Use the modulus operator `%` to get the last digit of the number.
- Multiply the reverse number by 10 and add the last digit.
- Use integer division `//` to remove the last digit from the original number.
- Repeat until the number becomes 0.
