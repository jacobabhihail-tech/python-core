print("\n********START******\n")

#input marks
studentname = input("Please enter your name: ")
marks = float(input("Enter Marks: "))

#Check if Pass or Fail

if marks >=  33.33:
    print(f"{studentname} You have Passed the exam by {marks - 33.33} marks")
else:
    print(f"{studentname} Sorry you have failed the exam by {33.33 - marks} marks")

print("\n********END*******\n")