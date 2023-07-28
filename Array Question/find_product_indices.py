def ind_product_indices(prices, target):
    z = list(prices)
    for i in prices[::-1]:
        for j in prices:
            if i != j:
                if i + j == target:
                    return [list(prices).index(i), list(prices).index(j)]

    return []


price_list = [10, 20, 30, 40, 50]
print(ind_product_indices(price_list, 60))
