l = [1, 2, 3, 4]
a = 34

print(str(a)[0])


def increment_large_integer(some_list):
    stringular = ''
    upd_list = []
    for i in some_list:
        stringular += str(i)
    update = int(stringular) + 1
    for i in str(update):
        upd_list.append(int(i))
    return upd_list
increment_large_integer(l)
