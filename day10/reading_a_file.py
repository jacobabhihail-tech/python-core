
#reading a file
"""
with open(r"D:\Python Journey\Python training\python-core\day10\data.txt", "r") as file:
    data = file.read()
    print(data)

"""
"""

What would “scan everywhere” look like? (DON’T DO THIS)
# This is slow, unsafe, and never used in production
for root, dirs, files in os.walk("C:\\"):
    if "data.txt" in files:
        print(os.path.join(root, "data.txt"))



"""    
# PROFESSIONAL WAY TO READ THE FILE

import os

#setup a file path
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "data.txt")

# read file and build users list
users = []

with open(file_path, "r") as file:

    for line in file:
        line = line.strip()

        if not line:
            continue #skips empty lines

        parts = line.split(",")

        if len(parts) != 3:
            continue # skips bad line       
        
        name, salary, experince = line.strip().split(",")

        user = {
            "name" : name,
            "salary" : int(salary),
            "experince" : int(experince)
        }

        users.append(user)


# for senior Employees
print("\n-----Senior Employees-----\n")

for u in users:
    if u["experince"] >= 7:
        print(f"{u['name']} is a senior employee")

#To find out the avg salary
total_salary = sum(u["salary"] for u in users)
average_salary = total_salary / len(users)
print(f"\nAverage Salary : {average_salary:.0f}\n")

#to check the highest paid employee
highest_paid = max(users, key=lambda u: u["salary"])
print(f"Highest Paid salary is to: {highest_paid['name']} - {highest_paid['salary']}")

#to check the highest paid employee
lowest_paid = min(users, key=lambda u: u["salary"])
print(f"Lowest Paid salary is to: {lowest_paid['name']} - {lowest_paid['salary']}")
    


   #for making structured data 
   # for line in file:
   #     clean_line = line.strip()
   #     parts = clean_line.split(",")
   #     print(parts)

    
   #for reading the file line by line
   #     for line in file:
   #        print(line.strip())
    
   # data1 = file.read()
   # print(data1)

