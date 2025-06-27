# 0008. Find the Smallest Number in a List

## 📝 Problem Statement

Write a program that takes a list of numbers from the user and finds the smallest number in that list.

---

## 📥 Example

**Input:**  
12 5 9 21 4

**Output:**  
The smallest number is: 4

---

## 📋 Constraints

- The list should have at least one number.
- Numbers can be positive, negative, or zero.

---

## 🧠 Solution Approach

1. **Take numbers as input** in a single line, separated by spaces.
2. Use `split()` to separate the numbers, then `map()` and `list()` to convert them into integers.
3. Assume the first number is the smallest.
4. Use a `for` loop to check if any number is smaller.
5. Update the smallest number if a smaller one is found.
6. Display the smallest number.

---

## 💻 Code (Python)

```python
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
smallest_number = numbers[0]

for number in numbers:
    if number < smallest_number:
        smallest_number = number

print("The smallest number is:", smallest_number)
