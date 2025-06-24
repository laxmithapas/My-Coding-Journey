# 0005. Calculate the Factorial of a Number

## 📝 Problem Statement

Write a program that takes a number as input from the user and calculates its factorial.

---

## 📥 Example

**Input:**  
5

**Output:**  
Factorial of 5 is: 120

---

## 📋 Constraints

- Number should be a positive integer or zero.
- Factorial of 0 is 1.

---

## 🧠 Solution Approach

1. **Take input** from the user.
2. Initialize a result variable to 1.
3. If the number is 0, factorial is 1.
4. Else, use a loop from 1 to the number:
   - Multiply result by each number in the loop.
5. Display the factorial.

---

## 💻 Code (Python)

```python
num = int(input("Enter a number: "))

factorial = 1

if num == 0:
    factorial = 1
else:
    for i in range(1, num + 1):
        factorial *= i

print("Factorial of", num, "is:", factorial)
