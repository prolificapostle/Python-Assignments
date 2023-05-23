name = "Semicolon"
rever = name[:]
print(rever)


def gen_user_name():
    email = input("Enter your Email Address: ")
    username = email.split("@")[0]
    print("Welcome,", username.capitalize())

gen_user_name()
