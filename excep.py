name = input("Enter Your Full Name: \n")

user_name = name.split(" ")[0]

print("Welcome",user_name.capitalize() +",")


def multiply(x: int, y: int) -> int:
    return x * y



def multiply2(x, y):
    try:
        return x * y
    except TypeError:
        return f"The input must be a number"


print(multiply2("4", "i"))
