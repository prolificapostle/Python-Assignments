class Human:
    number_of_eyes = 2

    def __init__ (self, name):
        self.name = name

    def greet(self):
        print("Good morning")

    def walk(self):
        print(f"{self.name}, is Walking ")

    def get_name(self):
        print(self.name)

    def __str__(self):
        return f"{self.name}"

human1 = Human("Esther")
human2 = Human("Torin")

print(human2)





human1.get_name()
human2.get_name()
human2.greet()
print(human1.number_of_eyes)
print(Human.number_of_eyes)

name = "semicolon"
upper_name = name.upper()
x = name[0] # prints out the letter in the first index = s
x = upper_name[-2]
print(x)

email = input("Enter Your Email Address: \n")
wel = email.split("@")
print(wel[0])
