#PROJECT 3 – DATA PREPROCESSING PIPELINE

#1️⃣: Clean Name + Clean Salary (we already discussed)

def clean_name(name):
    return name.strip().title() #strip space and capitalize rporperly

def clean_salary(salary_str):
    salary_str = salary_str.replace("$", "").replace(",","").strip()
    return int(salary_str)

def normalize(value, max_value):
    if max_value == 0:
        return None
    return value/max_value

print(clean_name(" ashu "))
print(clean_salary(" $ 80,000 "))

#Normalize TWO values together (salary + experience)

salary = 80000
experience = 8

max_salary = 100000
max_experience = 10

sal_norma = normalize(salary, max_salary)
exp_norma = normalize(experience, max_experience)

print(f"Salary normalized: {sal_norma:.2f}")
print(f"Experirence normalized: {exp_norma:.2f}")

#ONE user dictionary (SLOW & CLEAN)

user = {
    "name": " Ashu ",
    "salary": "$80,000",
    "experience": 8
}

user["name"] = clean_name(user["name"])
user["salary"] = clean_salary(user["salary"])

max_salary = 100000
max_experience = 10

user["sal_norma"] = normalize(user["salary"], max_salary)
user["exp_norma"] = normalize(user["experience"], max_experience)

print(user)

print("\n*****************\n)")  

#Multiple users

users = [
    {"name": " Ashu ", "salary": "$80,000", "experience": 8},
    {"name": " Ravi ", "salary": "$45,000", "experience": 5},
    {"name": " Neha ", "salary": "$100,000", "experience": 10}
]


max_salary = 100000
max_experience = 10

for user in users:
    # cleaning process
    user["name"] = clean_name(user["name"])
    user["salary"] = clean_salary(user["salary"])
    #normalizing process
    user["sal_norma"] = normalize(user["salary"], max_salary)
    user["exp_norma"] = normalize(user["experience"], max_experience)

print("Final processed data: ")

for user in users:
        print(user)



