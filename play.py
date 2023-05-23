lst = [3, 6, 1, 80, 43, 77, 22]
# def my_func(list=[]):
#    for i in range(len(lst)):
#       for j in range(i + 1, len(lst)):
#           if lst[i] > lst[j]:
#               lst[i], lst[j] = lst[j], lst[i]
#               return lst

# DICTIONARIES
double = {}
for a in range(1, 11):
    double[a] = a ** 2
print(double)

doubles = {a: a ** 2 for a in range(1, 11)}
print(doubles)

tuples1 = {a ** 2 for a in range(1, 11)}
print(tuples1)


my_dic = [{"name": "sam", "Cohort": "C 14"}, {"name": "Tolu", "Cohort": "C 15"}]
print(my_dic[0]["name"])

