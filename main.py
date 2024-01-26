import joblib
import pandas as pd

from mlxtend.frequent_patterns import apriori, association_rules

loaded_te = joblib.load('transaction_encoder.joblib')

data = pd.read_csv("Data/dummyData.csv")
print(data)

# Find frequent items using Apriori
frequent_itemsets = apriori(data, min_support=0.01, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules)

# Convert the unseen data to the format required by mlxtend
unseen_data = ['Milk', 'Bread']
te_unseen_ary = loaded_te.transform([unseen_data])
df_unseen = pd.DataFrame(te_unseen_ary, columns=loaded_te.columns_)

# Identify relevant rules for the new data
filtered_rules = rules[rules['antecedents'].apply(lambda x: set(unseen_data).issubset(set(x)))]

# Create a dictionary in the specified format
output_dict = {'response': {}}

# Populate the dictionary with suggested items and scores
for _, rule in filtered_rules.iterrows():
    antecedent = ', '.join(rule['antecedents'])
    consequent = ', '.join(rule['consequents'])
    score = rule['confidence']
    output_dict['response'][f"{antecedent} -> {consequent}"] = score

# Display the output dictionary
print(output_dict)
