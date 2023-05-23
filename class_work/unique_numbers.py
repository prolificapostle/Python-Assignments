

def unique_numbers(numbers):
    unique_list = []
    sum_of_unique_list = 0
    sum_of_given_list = 0
    difference = sum_of_given_list - sum_of_unique_list
    for i in numbers:
        sum_of_given_list += i
        if i not in unique_list:
            unique_list.append(i)
            sum_of_unique_list += i

    print(f"Given List: ", numbers)
    print(f"Sum of Given Numbers is: ", sum_of_given_list)
    print(f"Unique List: ", unique_list)
    print(f"Sum of Unique Numbers is: ", sum_of_unique_list)
    if difference % 2 == 0:
        print(numbers)
    else:
        print(unique_list)
    return unique_list


numbers = [2, 4, 6, 1, 4, 7, 4, 8, 2, 6, 8]
result = unique_numbers(numbers)
