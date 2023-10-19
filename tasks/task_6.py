def func(list1, list2):
    list = []
    for value in range(len(list1)):
        list.append(list1[value])
        list.append(list2[value])
    return list


print(func([1, 2, 3], [10, 20, 30]))
