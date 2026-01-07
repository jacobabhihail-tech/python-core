#learning tuples

coords = (10, 20)
print(coords)

print("\n************\n")
# Try to change (SEE THE ERROR)

coords = (10, 20)

# some examples of the use of tuples in AI / Backend REAL Examples

IMAGE_SIZE = (224, 224) #You don’t want this changing accidentally.
prediction = ("cat", 0.92) #Label + confidence → should stay together and unchanged.
user = ("Ashu", 80000, 8) #Read-only record fetched from DB.

#accessing tuples

print(coords[0])
print(coords[1])

#Important Rule to Remember
    #If data should not change → use tuple
    #If data will change → use list

print("\n*************\n")

point = (3, 5)
print(point[0])
print(point[1])