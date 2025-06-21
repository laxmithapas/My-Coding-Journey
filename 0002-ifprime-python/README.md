# 0002. Check if a Number is Prime

## 📝 Problem Statement

Write a program that takes a number from the user and checks whether it is a prime number.

---

## 📥 Example

**Input:**  
7

**Output:**  
7 is a prime number.

**Input:**  
10

**Output:**  
10 is not a prime number.

---

## 📋 Constraints

- Number should be a positive integer.
- If number is 1 or less, it is not a prime.

---

## 🧠 Solution Approach

1. **Take input** from the user.
2. If the number is less than or equal to 1, it’s not prime.
3. Check every number from 2 to num-1:
   - If the number divides evenly, it’s not a prime.
4. If no factors found, it’s prime.
5. Display the result.

---

## 💻 Code (Python)

```python
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number.")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
