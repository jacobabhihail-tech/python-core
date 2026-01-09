#Project 3 – Data Preprocessing Pipeline 

def clean_name(name):
    return name.strip().title()

def clean_salary(salary):
    salary = salary.replace("$", "").replace(",", "").replace("₹", "").strip()
    return int(salary)

def normalize(value, max_value):
    if max_value == 0:
        return None
    return value / max_value

def process_user(user, max_salary, max_experience):
    user["name"] = clean_name(user["name"])
    user["salary"] = clean_salary(user["salary"])
    user["sal_norma"] = normalize(user["salary"], max_salary)
    user["exp_norma"] = normalize(user["experience"], max_experience)
    return user

users = [
    {"name": " Ashu ", "salary": "₹80,000", "experience": 8},
    {"name": " Ravi ", "salary": "$45,000", "experience": 5},
    {"name": " Neha ", "salary": "$100,000", "experience": 10},
]

MAX_SALARY = 100000
MAX_EXPERIENCE = 10

for user in users:
    cleaned_user = process_user(user, MAX_SALARY, MAX_EXPERIENCE)
    print(cleaned_user)