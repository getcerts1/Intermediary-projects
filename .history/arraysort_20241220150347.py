def sorting(array):
    i = 0
    list_a = []
    while i in array:
        if i not in list_a:
            list_a.append(i)
            array.remove(i)
        i += 1
    return list_a

newarray = [7, 4, 6, 7, 5, 3, 2, 1, 0]
print(sorting(newarray))
