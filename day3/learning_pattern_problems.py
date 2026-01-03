print("\n*****Start*****\n")

#learning pattern loops.

#Pattern 1: Square Pattern

for row in range(5):
    for col in range(10):
        print("*", end= " ")
    print()


print("\n*****END*****\n")

#Pattern 2: Right Angle Triangle

for row in range(1, 6):
    for col in range(row):
        print("*", end= "")
    print()

print("\n*****END*****\n")

#Pattern 2: inverted Right Angle Triangle

for row in range(5, 0, -1):
    for col in range(row):
        print("*", end="")
    print()

print("\n*****END*****\n")

#Pattern 4: Number Triangle

for row in range (1, 5):
    for col in range(1, row + 1):
        print(col, end= " ")
    print()

print("\n*****END*****\n")

#Pattern 4: Same Number Triangle

for row in range(1,5):
    for col in range(row):
        print(row, end= " ")
    print()

print("\n*****END*****\n")

#Pattern 6: Reverse Number Pattern

for row in range(4, 0, -1):
    for col in range(row):
        print(row, end=" ")
    print()