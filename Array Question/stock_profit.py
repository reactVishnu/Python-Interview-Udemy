# "You have been given a list of stock prices of a particular stock. You want to maximize your profit by buying and
# selling the stock at the right time. On each day, you can either buy the stock, sell the stock, or do nothing. You
# can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the
# same day. Write a function that takes in a list of stock prices and returns the maximum profit you can achieve. If no
# profit can be made, return 0. Python function signature: ```python def max_profit(prices: List[float]) -> float: ```
# Example 1: ```python prices = [7, 1, 5, 3, 6, 4] assert max_profit(prices) == 5.0 ``` Example 2: ```python prices = [
#     7, 6, 4, 3, 1] assert max_profit(prices) == 0.0 ``` The function should take in a list of stock prices as input
# and return the maximum profit that can be achieved by buying and selling the stock at the right time. If no profit
# can be made, the function should return 0."


my_stock_list = [9, 7, 5, 3, 1]


def max_profit(list_stock):
    first_value = []
    price_store = []
    last_value = []
    for index, price in enumerate(list_stock):
        if index != len(list_stock)-1:
            print(f'Performing subtraction for {price} - {list_stock[index+1]}')
            profit = list_stock[index + 1] - price
            if profit > 0:
                print('profit')
                first_value.append((profit, price, list_stock[index+1]))
                price_store.append(price)
                last_value.append(list_stock[index+1])
    print(first_value)
    if len(first_value) == 1:
        return first_value[0][0]
    if len(first_value) > 1:
        index_fv = price_store.index(min(price_store))
        index_lv = last_value.index(max(last_value))
        if index_fv > index_lv:
            return max(last_value) - min(price_store)
        return first_value[len(first_value)-1][2] - first_value[0][1]

    return 0



result = max_profit(my_stock_list)

print(result)
