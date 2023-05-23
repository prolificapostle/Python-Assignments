with open("test.txt", mode="w") as file:
    file.write("001  Samuel  Anambra\n")
    file.write("002  Michael  Calabar\n")
    file.write("003  Johnson  Ondo\n")

with open("test.txt", mode="a") as file:
    file.write("004  Muntula  Makurdi\n")

with open("test.txt", mode="a") as file:
    file.write("005  Torin  Akure")

with open("test.txt", mode="r") as file2:
    for data in file2:
        Num, Name, State = data.split()
        print(f"{Num:<8} {Name:<10} {State:<10}")




