list = [1, 2, 3, 4, 5, 5, 6, 6, 6, 6, 7]


def remove_duplicates(mylist):
    updated_list = []
    for i in mylist:
        if i not in updated_list:
            updated_list.append(i)
    return len(updated_list)

updated_list = remove_duplicates(list)
print(updated_list)


