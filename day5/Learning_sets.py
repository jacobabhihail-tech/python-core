# learning Sets 

print("\n**************\n")

numbers = {1, 2, 3, 3, 4}
print(numbers)

print("\n**************\n")

#Real Example: Remove Duplicate Data

raw_ids = [101, 102, 103, 101, 102]
clean_ids = set(raw_ids)

print(clean_ids)

print("\n**************\n")


#Add to a Set

skills = {"python", "ML"}
print(skills)


skills.add("AI")

print(skills)

print("\n**************\n")

#Remove from a Set

skills = {"python", "ML", "AI"}
print(skills)
skills.remove("ML")
print(skills)

#To check if a particular value exists

skills = {"python", "ML", "AI"}

for python in skills:
    print("Python exists")


#AI-Style Example: Filter Unique Words

print("\n**************\n")

words = ["ai", "ml", "ai", "python", "ml"]
unique_words = set(words) # to remove all the dupilcates and make a new set of only unqiue words

print(unique_words)

print("\n**************\n")


#Mini Task

data = [1, 2, 2, 3, 4, 4, 5]
clean_date = set(data)

print(clean_date)
print("\n**************\n")

# before ending today's session a quick recap

#[] = list
#() = tuples
#{} = sets

#Mini Wrap-Up Project

print("\n**************\n")

raw_scores = [50, 60, 60, 80, 90, 90]

uni_scores = set(raw_scores)

final_scores = []

for scores in uni_scores:
    final_scores.append(scores/100)

print(final_scores)

print("\n**************\n")