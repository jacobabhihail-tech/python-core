# Testing sessions:

print("\n*****START*****\n")

#Challenge 1: Conditions + Loop
    #Print numbers from 1 to 10:
        #Print "BUY" if number is even
        #Print "SELL" if number is odd

"""
for i in range(1, 11):
    if i % 2 ==0:
        print(i,"->Buy")
    
    else:
        print(i,"->sell")

print("\n******END****\n")

"""

#Challenge 2: Pattern + Condition
        #   *
        #   * *
        #   * * *
        #   * * * *

"""

for rows in range (0, 5):
    for col in range(rows):
        print("#", end= " ")
    print("")    

print("\n*****END*****\n") ""

"""


#Challenge 3: While Loop Logic
    #Keep asking the user:
    #Enter number greater than 10:
    #Stop only when the user enters a number > 10


Gtrnum = 0

while Gtrnum <= 10:
    Gtrnum = int(input("Enter Number greater than 10: "))
    if Gtrnum < 10:
        print("Please enter Number greater than 10: ")
    elif Gtrnum == 10:
        print("The number is Equal to 10")    
print("the number is greater")


print("\n********END******\n")