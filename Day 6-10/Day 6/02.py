list1 = [1, 2, ['a', 'b', 'c'], 5.0, 6]

#print(type(list[1]))

#print(type(list1))

for elements in list1:
    print(type(elements))
    if isinstance(elements, list):
        for list2 in (elements):
            print(list2)
    else:
        pass
