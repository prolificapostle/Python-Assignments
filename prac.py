for x in range(2):
    print("hello C16")

count = 0
while count < 2:
    print("hello while is looping")
    count += 1

multi_count = 1
while multi_count < 13:
    print("2 x", multi_count, " = ", 2 * multi_count)
    multi_count += 1

for y in range(1, 13):
    print("2 x", y, "= ", y * 2)

even_num = (i for i in range(1, 21) if i % 2 == 0)
a = even_num
print(a)

