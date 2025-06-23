# 0004. Reverse a String

## 📝 Problem Statement

Write a program that takes a string input from the user and prints the reversed version of that string.

---

## 📥 Example

**Input:**  
hello

**Output:**  
olleh

---

## 📋 Constraints

- The string can have spaces, numbers, and symbols.
- Maintain uppercase and lowercase letters as they are.

---

## 🧠 Solution Approach

1. **Take input** from the user.
2. Use Python string slicing to reverse the string.
   - `string[::-1]` reads the string backward.
3. Display the reversed string.

---

## 💻 Code (Python)

```python
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
