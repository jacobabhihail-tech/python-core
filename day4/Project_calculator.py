# to make calculator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b   

def divide(a,b):
    if b==0:
        print("Error: Cannot be Divided by 0")   
    else:
        return a / b

def calculator():    
    print("\n********************************\n")
    print("Welcome to Python calculator")
    print("\n********************************\n")
    print("Please press a for Addition")
    print("Please press s for Subtraction")
    print("Please press m for Multiplication")
    print("Please press d for Division")

    choice = input("Please Enter the option: ").strip().lower()

    while choice not in ("a", "s", "m", "d"):
        print("The selected option is invalid")
        choice = input("Please Enter the correct option again: ").strip().lower()

    print("\n********************************\n")

    valA = float(input("Please enter First number: "))
    valB = float(input("Please enter Second number: "))
    valC = None

    print("\n********************************\n")

    if choice == "a":
        valC = add(valA, valB)
        print(f"The answer is : ", valC)

    elif choice == "s":
        valC = sub(valA, valB)
        print(f"The answer is : ", valC)

    elif choice == "m":
        valC = multiply(valA, valB)
        print(f"The answer is : ", valC)

    elif choice == "d":
        valC = divide(valA, valB)
        print(f"The answer is :{valC} ")

    print("\n********************************\n")
    print("Thank you for using calculator")
    print("\n********************************\n")

#loop until user exits
while True:
    calculator()
    again = input("If you want to use the calculator again please press Y or N to exit: ").strip().lower()
    if again != "y":
        print("\n********************************\n")
        print("Thank you for using Python Calculator")
        print("\n********************************\n")
        break
