def divide( a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

try:
    print(divide(10,0))
except ValueError as e:
    print("Error: ", e)

# real world example

def process_salary(salary):
    if salary < 0:
        raise ValueError("Salary cannot be negative")
    return salary *0.10 #tax example

try:
    tax = process_salary(-5000)
    print(tax)
except ValueError as e:
    print("Error: ", e)

#When you should use raise:
    # Input validation
    # Data cleaning
    # File processing
    # ML preprocessing
    # Backend APIs

#mini task

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted"

agecheck = None

try:
    inage = int(input("please enter age: "))
    agecheck = check_age(inage)
    print(agecheck)
except ValueError as e:
    print("Error: ", e )


