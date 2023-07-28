image = [[1, 2], [3, 4]]


# k = image[::-1]
# l=[]
# for index, i in enumerate(k):
#     if (len(k)+1)%2!=0:
#         l.append(i[::-1])
#     else:
#         if index != len(k)+1/2 - 1:
#             l.append(i[::-1])
# print(l)
def rotate_image(image):
    k = image[::-1]
    l = []
    for index, i in enumerate(k):
        if (len(k) + 1) % 2 != 0:
            l.append(i[::-1])
        else:
            if index != len(k) + 1 / 2 - 1:
                l.append(i[::-1])
    return l


j = rotate_image(image)
print(j)
