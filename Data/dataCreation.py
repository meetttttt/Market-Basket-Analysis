"""
- This file contains the code to create dummy data for the marketBasketAnalysis.
- We are simply using pandas and random to create dummy data.
- After we have created it dummy data we are storing it in a csv file for later use.
- We are also transforming the data using transactionEncoder it's super helpful to transform
    the dummy data into a transactional dataframe.
- After doing the Transactional Encoding we are storing the Encoder using joblib for later use
    while running on unseen data.
"""

# Imports are written here
import random
import joblib
import pandas as pd

from mlxtend.preprocessing import TransactionEncoder

try:

    # List of possible items
    items = ['Bread', 'Milk', 'Eggs', 'Cheese', 'Yogurt', 'Butter']

    # Number of transactions
    num_transactions = 100000

    # Generate dummy data
    data = []
    for transaction_id in range(1, num_transactions + 1):
        num_items_in_transaction = random.randint(1, len(items))
        items_purchased = random.sample(items, num_items_in_transaction)
        data.append({'Transaction ID': transaction_id, 'Items Purchased': ', '.join(items_purchased)})

    # Assuming 'data' is the list of dictionaries from the market basket analysis script
    transactions = [d['Items Purchased'].split(', ') for d in data]

    # Convert the data to the format required by mlxtend
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)

    # Save the encoder to a file
    joblib.dump(te, '../transaction_encoder.joblib')

    # Load data into the dataframe
    df = pd.DataFrame(te_ary, columns=te.columns_)

    # Save the data into csv file
    df.to_csv(path_or_buf="./dummyData.csv", index=False)

except Exception as e:
    print(f"Error in creating dummy data: {e}")
    print(f"Data not created..!")
