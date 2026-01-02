#Function to calculate simple interest

def simple_interest(principal, rate,time):
    return(principal * rate * time)/ 100

print("\n******START*******\n")

#input from the user

P = float(input("Please Enter the Principal Amount: "))
R = float(input("Please Enter the rate of interest: "))
T = float(input("Please enter the duration in years: "))

# call the function

SI = simple_interest(P,R,T)

print(f"Simple interest is: {SI}")

print("\n*******END******\n")