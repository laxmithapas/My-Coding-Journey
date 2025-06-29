# 0010. Convert Celsius to Fahrenheit

## 📝 Problem Statement

Write a program that takes a temperature in Celsius from the user and converts it to Fahrenheit.

Use the formula:

Fahrenheit = (Celsius × 9/5) + 32

---

## 📥 Example

**Input:**  
25

**Output:**  
Temperature in Fahrenheit: 77.0°F

---

## 📋 Constraints

- Temperature can be positive, negative, or zero.
- Result should display one decimal place if needed.

---

## 🧠 Solution Approach

1. **Take input** from the user as a float (since temperatures can be decimal values).
2. Use the conversion formula to convert Celsius to Fahrenheit.
3. Display the result.

---

## 💻 Code (Python)

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit, "°F")
