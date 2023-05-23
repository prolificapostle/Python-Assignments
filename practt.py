list1 = ["male", "female", "Female", "male", "Male", "male", "female"]
list2 = [x.lower() for x in list1]
print(list2)
male = []
female = []
for i in list2:
    if i == "male":
        male = i
        print(male, list2.count(male))

for y in list2:
    if y == "female":
        female = y
        print(female, list2.count(female))


numbers = range(1, 21)
for i in numbers:
    print()









