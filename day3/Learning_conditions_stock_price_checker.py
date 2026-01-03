# This is the example of If,Elif and Else for decision making to check if we should but a share or not.

print("\n*********START*********")

#making function to determine if the share should be bought or not.

""" def determine( if currentprice <= supportprice;
                    print(f"{stockname}" is a good to buy)
                elif   ) """

print("\n***********************************\n")
print("Welcome to stock price decision maker")
print("\n***********************************\n")

print("Please provide the below details.")

# Taking the reguired details

STName = (input("Please enter the stock Name: "))
CMP = float(input("Please enter the current Market price: "))
SupPrice = float(input("Please enter the Support price: "))
ResPrice = float(input("Please enter the resistance price: "))

print("Please select the one of the below option")

choice = input("Please press B to check range for new share or H to check the range for already holding shares: ").strip().lower()

print("\n***********************************\n")

## To check if we should buy the shares or not
if choice == "b":
    if CMP >= ResPrice:
        print(f"The price of {STName} is above {ResPrice} please dont buy the shares")
    elif CMP <= SupPrice:
        print(f"Please buy the shares of {STName} at {CMP}")
    else:
        print(f"Wait!!! Please buy the shares of {STName} near the support zone of {SupPrice}")

## To check if the share is good to hold or sell
elif choice == "h":

    YAP = float(input("Please enter your avg price: "))

    if CMP >= ResPrice:
        print(f"Please sell the share of {STName}")
    elif CMP > YAP and CMP < SupPrice:
        print(f"Please hold the share of {STName} till we reach the level of {ResPrice}")
    elif  CMP < YAP and CMP < SupPrice:
        print(f"please buy more share of {STName} to bring down the avg from {YAP}")
    else:
        print(f"Hold cautiously. {STName} is weak near support.")
    
else:
    print("Invalid selection.")


print("\n**********END************\n")

