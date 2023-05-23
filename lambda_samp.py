list3 = range(1, 31)
print(list3)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def odd_num(list):
    ans = []
    for i in list:
        if i % 2 != 0:
            ans.append(i)
    return ans

def odd_num2(n):
    if n % 2 == 0:
        return n

print(odd_num(list3))

print(list(filter(odd_num2, list3)))

print(list(filter(lambda n: n % 2 != 0, list3)))

print(list(map(lambda n: n % 2 == 0, list3)))

