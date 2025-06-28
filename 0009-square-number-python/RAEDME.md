# 0009. Find the Square of a Number

## 📝 Problem Statement

Write a program that takes a number as input from the user and prints its square.

---

## 📥 Example

**Input:**  
8

**Output:**  
Square of 8 is: 64

---

## 📋 Constraints

- Number can be positive, negative, or zero.

---

## 🧠 Solution Approach

1. **Take input** from the user.
2. Multiply the number by itself to get the square.
3. Display the result.

---

## 💻 Code (Python)

```python
num = int(input("Enter a number: "))
square = num * num
print("Square of", num, "is:", square)
