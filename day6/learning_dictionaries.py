# Day 6 –  learning Dictionaries

user = {
    "name": "Ashu",
    "age": 32,
    "city": "Dubai"
}

user["salary"] = 100000

print(user["name"])
print(user["city"])
print(user)

print("\n*********\n")

#Looping Through Dictionary (IMPORTANT)

print("\n*********\n")

for key, value in user.items():
    print(key, ": ", value)

print("\n*********\n")

#REAL AI / BACKEND EXAMPLE

user = {
    "name": "Ashu",
    "salary": "$80,000",
    "experience": 8
}

user["salary"] = int(user["salary"].replace("$", "").replace(",", ""))

print(user)

for key, value in user.items():
    print(key, ":", value)

print("\n*********\n")


#MINI TASK

person = {
    "name": "Ravi",
    "phone": "99999",
    "city": "Delhi"
}

print(person["name"])
person["city"] = "bangalore"
person["email"] = "ravi@gmail.com"

print(person)

print("\n*********\n")

for key, value in person.items():
    print(key, " : ", value)

print("\n*********\n")


#Next Topic: Nested Dictionaries
#A dictionary inside another dictionary.

users = {
    "user1": {
        "name": "Ashu",
        "phone": "88888",
        "city": "Dubai"
    },
    "user2": {
        "name": "Ravi",
        "phone": "99999",
        "city": "Bangalore"
    }
}

print(users["user1"]["name"])
print(users["user2"]["city"])

#Update Nested Values
print("\n*********\n")
print(users)
print("\n*********\n")
users["user1"]["city"] = "abu dhabi"

print(users)

print("\n*********\n")

#Add New Data Inside Nested Dict
users["user2"]["Email"] = "ravi@email.com"

print(users)

print("\n*********\n")
#MINI TASK
contacts = {
    "c1": {
        "name": "Ashu",
        "phone": "88888"
    },
    "c2": {
        "name": "Neha",
        "phone": "77777"
    }
}

print(contacts["c1"]["phone"])
contacts["c2"]["city"] = "mumbai"

print(contacts)
print("\n*********\n")


for key, con in contacts.items():
    print(key, ":", con)

print("\n*********\n")