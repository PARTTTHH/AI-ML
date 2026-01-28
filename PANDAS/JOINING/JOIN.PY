"""
SYNTAX:-
        df.concat([df1, df2], axis=0/1, ignore_index=True)
"""

import pandas as pd

Customer_list1 = pd.DataFrame({
    "CustomerID":[1,2,3,4],
    "CustomerName":['GOPAL', 'RAJU', "RAJ", "GANSHAM"]
})

Customer_list2 = pd.DataFrame({
    "CustomerID":[5,6,7,8],
    "CustomerName":['SHAYM', 'BABURAO', "RAHUL", "ADARSH"]
})

TOTAL_CUSTOMER_LIST = pd.concat([Customer_list1, Customer_list2], ignore_index=False)
print("AFTER CONCATINATE WITH axis=0:-")
print(TOTAL_CUSTOMER_LIST)

print()

TOTAL_CUSTOMER_LIST2 = pd.concat([Customer_list1, Customer_list2], axis=1, ignore_index=False)
print("AFTER CONCATINATE WITH axis=1:-")
print(TOTAL_CUSTOMER_LIST2)