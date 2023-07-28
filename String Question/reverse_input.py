def reverse_in_place(some_stirng):
    if isinstance(some_stirng, float) or isinstance(some_stirng, list):
        raise TypeError("Input must be a string or an integer")
    x = type(some_stirng)
    return x(str(some_stirng)[::-1])


print(type(reverse_in_place(12345)))
