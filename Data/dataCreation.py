import random
import joblib
import pandas as pd

from mlxtend.preprocessing import TransactionEncoder

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
