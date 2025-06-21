# 0001. Find the Largest Number in a List

## 📝 Problem Statement

Write a program that takes a list of numbers from the user and finds the largest number from that list.

---

## 📥 Example

**Input:**  
`5 12 9 21 4`

**Output:**  
`The largest number is: 21`

---

## 📋 Constraints

- The list can contain positive or negative numbers.
- The list will always have at least one number.
- A maximum of 100 numbers can be entered.

---

## 🧠 Solution Approach

1. **Take Input:**  
   Get numbers from the user in a single line, separated by spaces.

2. **Convert Input to List:**  
   Use `split()` to separate the numbers, then `map()` and `list()` to convert them into integers.

3. **Initialize Largest Number:**  
   Assume the first number in the list is the largest.

4. **Iterate Through List:**  
   Use a `for` loop to compare each number with the current largest number.

5. **Update if Bigger:**  
   If a number is greater than the current largest, update the largest number.

6. **Display Result:**  
   Print the largest number found.

---

## 💻 Code (Python)

```python
# Program to find the largest number in a list

# Step 1: Ask the user to enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert the input string into a list of integers
numbers = list(map(int, user_input.split()))

# Step 3: Assume the first number is the largest for now
largest_number = numbers[0]

# Step 4: Go through each number in the list
for number in numbers:
    if number > largest_number:
        largest_number = number

# Step 5: Show the largest number to the user
print("The largest number is:", largest_number)
