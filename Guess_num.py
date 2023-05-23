


def rand():
    lucky_num = 5
    num_entered = int(input("Guess the Lucky Number From 1 to 10 \n"))
    while num_entered != lucky_num:
        print("Wrong Number Try again")
    else:
         print("Congratulations! ")


rand()
