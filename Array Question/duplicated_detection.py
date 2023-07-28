prod = [1, 2, 3, 4, 5, 6, 7, 6, 7, 6]
print(prod.count(6))


def detect_duplicate_products(products):
    for i in products:
        if list(products).count(i) > 1:
            return True
    return False


z = detect_duplicate_products(prod)
print(z)