def find_unique_customer_id(custId):
    unq_cust_id = []
    for i in custId:
        if list(custId).count(i) == 1:
            unq_cust_id.append(i)
    return unq_cust_id


customer_id = [1,2,3,4,5,1,2,3,4]
z = find_unique_customer_id(customer_id)
print(int(z))

