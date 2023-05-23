file1 = open("record2.txt", mode="r")

file2 = open("record.txt", mode="w")

with file1, file2:
    for record in file1:
        S, s, s = record.split()
        if S == "008":
            file2.write("001 mariam 75\n002 david 75\n003 nati 75\n004 torin 75\n005 Hyelnati 75\n006 Sammie 75\n007 Esther 75\n008 Masterr 75\n")
        else:
            new_record = " ".join([S, "oluwaseyifunmi", s])
            file2.write(new_record + "\n")


with open("record.txt", mode="a") as file:
    file.write("009 PastorJames 090\n")

with open("record.txt", mode="a") as file:
    file.write("010 Chibuzor 100\n")
