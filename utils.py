# utils.py

import joblib
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


def load_data():
    loaded_te = joblib.load('transaction_encoder.joblib')
    data = pd.read_csv("Data/dummyData.csv")
    return loaded_te, data


def perform_market_basket_analysis(data, loaded_te):
    frequent_item = apriori(data, min_support=0.01, use_colnames=True)
    rules = association_rules(frequent_item, metric="confidence", min_threshold=0.5)
    return rules


def recommend_items(unseen_data, rules, loaded_te):
    te_unseen_ary = loaded_te.transform([unseen_data])
    df_unseen = pd.DataFrame(te_unseen_ary, columns=loaded_te.columns_)

    filtered_rules = rules[rules['antecedents'].apply(lambda x: set(unseen_data).issubset(set(x)))]

    output_dict = {'response': {}}

    for _, rule in filtered_rules.iterrows():
        antecedent = ', '.join(rule['antecedents'])
        consequent = ', '.join(rule['consequents'])
        score = rule['confidence']
        output_dict['response'][f"{antecedent} -> {consequent}"] = score

    return output_dict
