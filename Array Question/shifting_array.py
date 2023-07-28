from typing import List

array = [1, 2, 3, 4, 5]


def shift_array(arr: List[int], n: int) -> List[int]:
    if n == 0:
        return arr
    elif n > 0:
        n = n % len(arr)
        return arr[-n:] + arr[:-n]
    else:
        n = abs(n) % len(arr)
        return arr[n:] + arr[:n]


print(shift_array(array, 3))
