# On this day, I learned:
# 1. Primitive Data Types - Strings, Integers, Floats, Booleans.
# 2. Type Conversion - int(), float(), str().
# 3. Mathematical Operations - we should use the PEMDAS rule.
# 4. Number Manipulation - Flooring, Rounding a number, Assignment Operators (e.g. +=), f-String.
# 5. Summary: I've created a project - Tip Calculator!

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people will be splitting the bill? "))

calculation = round((bill / people + ((bill * (tip/100)) / people)), 2)
print(f"Your Final Bill per person is: {calculation:.2f}")
