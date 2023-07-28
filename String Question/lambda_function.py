names = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Brown", "William Lee"]

# updated_list = list(map(lambda x: [x.split()[-1], x], names))
#
# sorted_list = list(map(lambda x: x[0], updated_list))
#
# print(sorted_list.sort())
# sorted(names, )
names.sort(key=lambda x:x.split()[-1])
print(names)

names = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Brown", "William Lee"]

sorted_names = sorted(names, key=lambda name: name.split()[-1])

print(sorted_names)