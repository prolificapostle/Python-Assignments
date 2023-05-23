quest = int((input("Enter a Number: ")))

def fizzbuzz(quest):
    if quest % 3 == 0 and quest % 5 == 0:
        return "fizzbuzz"
    if quest % 5 == 0:
        return "buzz"
    if quest % 3 == 0:
        return "fizz"

print(fizzbuzz(quest))

list2 = [1, 2, 3, 4, 5, 6]


def square(y):
   return y ** 2



