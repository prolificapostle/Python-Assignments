# file = open("student_records.txt", mode="w")
# file.write("001 mariam 75\n")
# file.write("002 david 75\n")
# file.write("003 nati 75\n")
# file.write("004 torin 75\n")
# file.close()

# with open("record2.txt", mode="w") as file:
#    file.write("006 Hyelnati 75\n")
#    file.write("006 Sammie 75\n")
#    file.write("007 Esther 75\n")

#with open("products.txt", mode="w") as file:
#     file.write("LIST OF PRODUCTS \n")
#     file.write("ID:001  Wireless Mouse      NGN7,000 \n")
#     file.write("ID:002  USB Mouse           NGN2,000 \n")
#     file.write("ID:003  Bluetooth Speakers  NGN17,000 \n")
#     file.write("ID:004  USB Keyboard        NGN2,000 \n")
#     file.write("ID:005  Laptop Charger      NGN4,000 \n")
#     file.write("ID:006  External HDD        NGN32,000 \n")
#     file.write("ID:007  32GB FlashDrive     NGN9,000 \n")
#     file.write("ID:008  WebCam              NGN12,500 \n")


# with open("record2.txt", mode="r") as records:
#    for record in records:
#        num, name, score = record.split()
#        print(f"{num:<10} {name:<10} {score: >10}")

#with open("products.txt", mode="r") as products:
#    for product in products:
#        nos, prod, price = product.split()
#        print(f"{nos:<10} {prod:<10} {price:>10}")

# HOW TO APPEND TO EXISTING FILE
with open("record2.txt", mode="a") as file:
    file.write("007 Masterr 75\n")
