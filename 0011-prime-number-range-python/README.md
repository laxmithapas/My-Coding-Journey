# 0011. Find All Prime Numbers in a Given Range

## 📝 Problem Statement

Write a program that takes two numbers as input from the user: start and end, and prints all prime numbers within that range.

---

## 📥 Example

**Input:**  
Start: 10  
End: 30  

**Output:**  
Prime numbers between 10 and 30 are:
11  
13  
17  
19  
23  
29  

---

## 📋 Constraints

- Both numbers should be positive integers.
- start should be less than or equal to end.
- If no primes are found, display a suitable message.

---

## 🧠 Solution Approach

1. **Take input** from the user for start and end.
2. Validate that start and end are positive, and start <= end.
3. Use a loop from start to end.
4. For each number, check if it’s greater than 1.
5. Check divisibility from 2 to num-1.
6. If no divisors found, it’s prime.
7. Print all prime numbers found in the range.

---

## 💻 Code (Python)

```python
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

if start > end or start < 0 or end < 0:
    print("Invalid range. Please enter positive numbers where start <= end.")
else:
    print("Prime numbers between", start, "and", end, "are:")

    for num in range(start, end + 1):
        if num > 1:
            is_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(num)
