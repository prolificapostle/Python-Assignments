def palindron(input):
    input_lower = input.lower()
    reversed_input = input_lower[::-1]
    return input_lower == reversed_input

print(palindron("111"))

total_num = 0
list_of_numbers = []
num_entered = int(input("Enter a number from 1 - 100, or 0 to quit: \n"))
while num_entered != 0:
    list_of_numbers.append(num_entered)
    num_entered = input("Enter a number from 1 - 100, or 0 to quit: \n")


print(list_of_numbers)
print(total_num)


