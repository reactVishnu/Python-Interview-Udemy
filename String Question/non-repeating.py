
def first_non_repeating_char_index(s):
    for index, i in enumerate(s):
        if str(s).count(i) == 1:
            return index
    return -1


sm = 'lovely you'
print(first_non_repeating_char_index(sm))