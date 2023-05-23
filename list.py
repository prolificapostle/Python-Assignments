class List:

    def __init__(self, a, b):
        self.a = 1
        self.b = 2

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = range(1, 21)


def even_num(lists):
    ans = []
    for i in lists:
        if i % 2 == 0:
            ans.append(i)
    return ans


print(even_num(list1))
print(even_num(list2))


list3 = range(1, 11)


def check_for_odd(n):
    if n % 2 != 0:
        return n


print(list(filter(check_for_odd, list3)))




p1 = List(1, 2)
p2 = List(1, 2)
print(p1 < p2)