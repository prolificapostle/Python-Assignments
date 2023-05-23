def cohort16_register():
    names_age = {"esther": 23, "rotimi": 45, "lateef": 34, "mariam": 20}

    name = input("Enter your name: ").lower()

    if name in names_age:
        age = names_age[name]
        print(f"Hi, {name.capitalize()}, you are {age} years old.")
    else:
        age = int(input("Your name is not in the database. Please enter your age: "))
        names_age[name] = age
        print(f"Hi, {name.capitalize()}, you are {age} years old.")

