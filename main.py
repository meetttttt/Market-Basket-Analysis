"""
This file is used to perform the market basket analysis using mlxtend library.
We will use the dummy data we created.
We will also create a function to test it on unseen data.
"""

# Imports are written here
import joblib
import pandas as pd

from mlxtend.frequent_patterns import apriori, association_rules

try:

    # Loading the TransactionalEncoder
    loaded_te = joblib.load('transaction_encoder.joblib')

    # Loading the dummydata
    data = pd.read_csv("Data/dummyData.csv")

    # Find frequent items using Apriori
    frequent_item = apriori(data, min_support=0.01, use_colnames=True)

    # Generate association rules
    rules = association_rules(frequent_item, metric="confidence", min_threshold=0.5)

    # Displaying the Frequent Item
    print("Frequent Item:")
    print(frequent_item)

    # Displaying the Association Rules
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

except Exception as e:
    print(f"Error occurred: {e}")
