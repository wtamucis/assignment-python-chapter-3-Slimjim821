# James (Jim) Johnson
# Chapter 3.1 Introduction, no code
# Chapter 3.2 Conditional Statements
print("Chapter 3.2 Conditional Statements")
temperature = 15
if temperature > 30:
    print("It's Warm")
    print("Drink Water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")
print("*" * 30)

# Chapter 3.3 Ternary Operator
print("Chapter 3.3 Ternary Operator")
age = 12
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

cost = 300
status = "expensive" if cost > 100 else "cheap"
print(status)
print("*" * 30)


# Chapter 3.4 Logical Operators
print("Chapter 3.4 Logical Operators")
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
print("*" * 30)


# Chapter 3.5 Short-circuit Evaluation
print("Chapter 3.5 Short-circuit Evaluation")
high_income = False
good_credit = True
student = False

if high_income or good_credit or not student:
    print("Eligible")

# Chapter 3.6 Chaining Comparison Operators
print("Chapter 3.6 Chaining Comparison Operators")
age = 22
if 18 < + age < 65:
    print("Eligible")
print("*" * 30)
