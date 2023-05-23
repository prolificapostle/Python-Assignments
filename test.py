

lst = [42, 34, 26, 68, 100]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i]. lst[j] = lst[j]. lst[i]
print(lst)
