# 1️⃣: Even or Odd Checker 

def is_even(num):
    return num % 2 == 0

print(is_even(7))
print(is_even(10))

"""
result = int(input("Please enter number to check: "))

if (is_even(result)):
    print("This number is Even")
else:
    print("This number is Odd")
"""

#2️⃣: Clean Salary / Number Input (REAL-WORLD GOLD)

def clean_salary(salary_str):
   try:
     salary_str = salary_str.replace(",", "").replace("$", "").replace("Rs.", "")
     salary_str = salary_str.strip()
     return float(salary_str)

   except ValueError:
    return "Invalid Salary format"

print(clean_salary("45,000 "))
print(clean_salary("$45,000 "))
print(clean_salary("Rs.45,000 "))
print(clean_salary("abc "))

"""
check_salary = (input("Please enter the salary: "))
print(clean_salary(check_salary))
"""


#3️⃣: Normalize Values (🔥 ML CORE CONCEPT 🔥)

def normalize(value, max_value):
    if max_value == 0:
        return None
    return value / max_value


valA = 80000
valB = 100000

val_normaliz = normalize(valA, valB)

print(val_normaliz)
"""
invalA = int(input("please enter the value a: "))
invalb = int(input("please enter the value b: "))

invalnorma = normalize(invalA, invalb)

if invalnorma is None:
   print("The value entered is not correct")
else:
    print(f"The Normalized value is : ", invalnorma) 

"""

#4️⃣ Normalizing a LIST (ML PREPROCESSING 🔥)

scores = [50, 60, 80, 90]
max_score = max(scores)

normalized_scores = []

for s in scores:
   normalized_scores.append(normalize(s, max_score))

for value in normalized_scores: #OPTION 1: Format EACH value
   print(f"{value : .2f}")

formatted_scores = [f"{v:.2f}" for v in normalized_scores] #OPTION 2: Create a new formatted list
print(formatted_scores) #Useful for UI, JSON responses, reports

rounded_scores = [round(v, 2) for v in normalized_scores] #Round values (NOT formatting)
print(rounded_scores)

#Normalize Salary Data

salaries = [30000, 45000, 82000, 100000]
max_salary = max(salaries)

for sal in salaries:
   print(f"{sal} -> {normalize(sal, max_salary):.2f}")

#Mini Task
    #Create a list: [10, 20, 30, 40]
    #Normalize it using a loop
    #Print results with 2 decimals

testlist = [10, 20, 30, 40]
max_in_test_list = max(testlist)

for tlist in testlist:
   print(f"{tlist} -> {normalize(tlist, max_in_test_list): .2f}")
