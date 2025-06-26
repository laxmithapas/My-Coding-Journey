# 0007. Check if a Number is Even or Odd

## 📝 Problem Statement

Write a program that takes a number as input from the user and checks whether it is even or odd.

---

## 📥 Example

**Input:**  
6

**Output:**  
6 is an even number.

**Input:**  
9

**Output:**  
9 is an odd number.

---

## 📋 Constraints

- Number should be an integer (positive, negative, or zero).
- Zero is considered an even number.

---

## 🧠 Solution Approach

1. **Take input** from the user.
2. Use the modulus operator `%` to check if the number is divisible by 2.
   - If `num % 2 == 0`, it’s even.
   - Else, it’s odd.
3. Display the result.

---

## 💻 Code (Python)

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
