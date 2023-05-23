
def calculator():
    ar_fun = int(input("""
    "Select an Arithmetic Function from the Options below."
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division
    """))
    num1 = float(input("Enter the first Number"))
    num2 = float(input("Enter the second Number"))
    if ar_fun == 1:
        print(num1 + num2)
    if ar_fun == 2:
        print(num1 - num2)
    if ar_fun == 3:
        print(num1 * num2)
    if ar_fun == 4:
        print(num1 / num2)




calculator()

