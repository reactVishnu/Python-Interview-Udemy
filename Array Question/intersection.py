def common_customers(cust_1, cust_2):
    int_list = []
    for i in cust_1:
        if i in cust_2:
            if i not in int_list:
                int_list.append(i)

    return int_list


cust_1 = [1,2,4, 4, 5,5]
cust_2 = [1,3,45,6,4,4]

z = common_customers(cust_2, cust_1)
print(z)
