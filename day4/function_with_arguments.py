# Functions with ARGUMENTS (Inputs)

def greet(Name):
    print("Hello", Name)

greet("Ann")

#using Multi Arguments

def Add(a, b):
    print(a + b)

Add(10, 5)   

# Task for understanding
#1️⃣ Function that prints your age
#2️⃣ Function that prints two numbers multiplied
#3️⃣ Function that prints "Welcome to UAE" with your name

#1️⃣ Function that prints your age
def age(a):
    print("Your age is", a)

age(32)    

#2️⃣ Function that prints two numbers multiplied

def multi(a, b):
    print(f"{a} multiply by {b} = ", a * b)

multi(5, 10)    

#3️⃣ Function that prints "Welcome to UAE" with your name

def greet(name):
    print(f"Hello {name}, Welcome to UAE")

greet("Ashu")

print("\n********PART 2******\n")

#usage of return

def add(a, b):
    return a + b

sum = add(10, 5)
print(f"The is sum of the numbers =", sum)

print("\n**************\n")
#task to understand the return

def multiply(a, b):
    return a * b

ans = multiply(10, 5)
print("Answer =", ans)

print("\n**************\n")
#Using multiple Returned Values

def add(a,b):
    return a+b

def multiply(a, b):
    return a * b

x = add(10, 5)
y = multiply(x, 5)

print("The value of y is: ", y )
print("\n**************\n")