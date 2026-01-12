
"""
try:
    # risky code
except:
    # runs ONLY if error happens
else:
    # runs ONLY if no error
finally:
    # ALWAYS runs (error or no error)
"""

try:
    salary = int("80000")
except ValueError:
    print("Invalid salary")
else:
    print("Salary converted:", salary)
finally:
    print("conversion attempt finished")


print("\n****************\n")

file = None

try: 
    file = open("abc.txt") 
    data = file.read()
except FileNotFoundError:
    print("The file not found")
else:
    print("file read successfully")
finally:
    if file:
        file.close()