# 1️⃣: Lists (MOST IMPORTANT in AI & Backend)

numbers = [10, 20, 30, 40]


#🔹 Accessing List Items
print(numbers[0])
print(numbers[3])

print("\n**********\n")

# Looping Through a List (VERY IMPORTANT)

for n in numbers:
    print(n)

print("\n**********\n")

#Normalize scores using a list:

scores = [50, 60, 80, 100]
max_scores = max(scores)

for s in scores:
    normalized = s/max_scores
    print(round(normalized, 2))

print("\n**********\n")

#Modifying Lists
scores.append(90)
print(scores)

#MINI TASK

values = [5, 10, 15, 20]

for v in values:
    print(v * 2)

#Storing results using append()

values = [5, 10, 15, 20]
results = []

for v in values:
    results.append(v * 2)

print("\n**********\n")

print(values)
print(results)

print("\n**********\n")

#Filtering Lists

print("\n**********\n")

values = [5, 10, 15, 20]
filteredlist = []

for v in values:
    if v > 10:
        filteredlist.append(v)

print(values)
print(filteredlist)



print("\n**********\n")
