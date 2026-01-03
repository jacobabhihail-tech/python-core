print("\n*******START*****\n")

#learning while loop

#Count from 1 to 5

count = 1

while count <= 5:
    print(count)
    count += 1

print("\n******************\n")

#Stock price watch (target based)

price = 170

while price <= 180:
    print(price)
    price += 2

print("\n******************\n")

#Password validation

Password = ""

while Password != "Ashu@123":
    Password = input("Please enter Password: ")
    if Password != "Ashu@123":
        print("Password incorrect please enter again")
print("Access granted")

print("\n******************\n")
#Recruiter example – calls until filled - reverse counter

position = 3 

while position > 0:
    print("Calling candidates....", position)
    position -= 1
print("Position filled") 


print("\n*******END********\n")

