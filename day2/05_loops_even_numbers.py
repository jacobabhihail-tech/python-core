print("\n******Start******\n")

#using for loops to print even and odd number from 1 to 20

#Setting a Range 

numA = int(input("Please enter the first number:"))
numB = int(input("Please enter the last number:"))

#giving option to select between ODD and EVEN

OE = input("Please select Odd or Even: ").lower()

"""
if OE.lower == "Even":
   for i in range (numA, numB + 1):
       if i % 2 == 0:
           print(i)
    
elif OE.lower == "Odd":
   for j in range (numA, numB + 1):
        if j % 2 != 0:
           print(j)
else:
    print("Invalid Input. Please enter Odd or Even")

"""
    
if OE in ["even","odd"]:
    for i in range(numA, numB + 1):
        if(OE == "even" and i % 2==0) or (OE == "odd" and i % 2 !=0):
            print(i)
      
else:
    print("Invalid Input. Please enter Odd or Even") 


print("\n**********END********\n")