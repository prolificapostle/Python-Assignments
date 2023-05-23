def cohort16_register():

    cohort16_database =  {"esther": 23, "rotimi": 45, "lateef": 34, "mariam": 20}
    name_input = input("Enter your name please: \n")
    name_input_lower = name_input.lower()
    if name_input in cohort16_database:
        age = cohort16_database[name_input]
        print(f"Hello {name_input_lower.capitalize()}, you are {age} years old")
    else:
        print(f"Hello {name_input_lower.capitalize()}, your name is not in the database...")
        ans = int(input("Do you want your records in our data base? Press 1 for Yes and 2 for No"))
        if ans == 1:
            age = int(input("Please Enter your age: "))
            cohort16_database[name_input] = age
            print(f"{name_input_lower.capitalize()}, you are {age} years old")
        else:
            print("Thank you for using our software")



cohort16_register()




