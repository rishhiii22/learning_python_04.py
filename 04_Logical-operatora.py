# Logical Operators in Python

# Logical operators are used to combine conditional statements in Python. The main logical operators are `and`, `or`, and `not`.
a = int(input("Enter your age: "))
b = int(input("Enter your friend's age: "))
# Using 'and' operator

if a >= 18 and b >= 18:
    print("Both you and your friend are eligible to vote.")

# Using 'or' operator

if a >= 18 or b >= 18:
    print("At least one of you is eligible to vote.")

# Using 'not' operator

if not (a < 18): 
    print("You are not underage.") 
else:
    print("You are underage.")
# This code checks the ages of two individuals and prints messages based on their eligibility to vote.