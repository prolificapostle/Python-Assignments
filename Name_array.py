name_list = []
for i in range(3):
    name_entered = input("Enter a Name not longer than 10 character: ")
    while len(name_entered) > 10:
        print("Name Entered is longer than 10")
        name_entered = input("Enter a Name not longer than 10 character: ")
    name_list.append(name_entered)

print(name_list)

