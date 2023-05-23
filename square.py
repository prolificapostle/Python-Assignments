list1 = range(1, 20)
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(n):
    return n ** 2

ans = list(map(square, list2))
print(ans)

ans1 = list(map(square, list2))
print(ans1)

ans2 = list(map(lambda n: n % 2 == 1, list2))
print(ans2)



