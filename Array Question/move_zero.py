arr = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]

def move_zeros(arr):
    for i in range(arr.count(0)):
        arr.remove(0)
        arr.append(0)
    return arr


print(move_zeros(arr))

