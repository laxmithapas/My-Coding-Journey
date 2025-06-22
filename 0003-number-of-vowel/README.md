# 0003. Count the Number of Vowels in a String

## 📝 Problem Statement

Write a program that takes a string input from the user and counts how many vowels (a, e, i, o, u) are in the string.

---

## 📥 Example

**Input:**  
OpenAI is awesome

**Output:**  
Number of vowels: 7

---

## 📋 Constraints

- The string can have spaces, uppercase, and lowercase letters.
- Count both uppercase and lowercase vowels.

---

## 🧠 Solution Approach

1. **Take input** from the user.
2. Define a string of vowels: `aeiouAEIOU`.
3. Initialize a counter to 0.
4. Go through each character in the input string.
5. If the character is in the vowels string, increment the counter.
6. Display the total number of vowels.

---

## 💻 Code (Python)

```python
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)
