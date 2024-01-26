# Market Basket Analysis:
- Market Basket Analysis is one of the key techniques used to uncover associations between items. It works by looking for combinations of items that occur together frequently in transactions

Sure, here's a small description that you can use for your GitHub repository:

---

## Flask Market Basket Analysis API

This repository contains a simple Flask API for performing Market Basket Analysis using the mlxtend library. The application loads a pre-trained transaction encoder and dummy transactional data to generate association rules. It provides a real-time recommendation endpoint where you can input a list of items, and the API will return relevant association rules and their confidence scores.

### Files:

- `app.py`: Flask application file containing the API endpoints for performing market basket analysis in real-time.
- `utils.py`: Utility functions for loading data, performing market basket analysis, and generating recommendations.
- `transaction_encoder.joblib`: Pre-trained transaction encoder used for transforming input data.

### Usage:

1. Install required libraries: `pip install Flask pandas mlxtend joblib`.
2. Run the Flask app: `python app.py`.
3. Send a POST request to `http://127.0.0.1:5000/recommend` with JSON data containing the 'data' key.

Example Input JSON data:
```json
{
  "data": ["Milk", "Bread"]
}
```

The API will respond with relevant association rules and their confidence scores based on the input data.

Example Output JSON Data:
```json
{
    "response": {
        "Cheese, Bread, Eggs, Milk, Butter -> Yogurt": 0.8570621758997792,
        "Cheese, Bread, Milk, Butter, Yogurt -> Eggs": 0.8566663245406958,
        "Milk, Butter, Yogurt -> Bread": 0.8048990263873121,
        "Milk, Butter, Yogurt -> Bread, Cheese": 0.6703822203873809,
        "Milk, Butter, Yogurt -> Bread, Eggs, Cheese": 0.5742938727766883,
        "Milk, Butter, Yogurt -> Cheese": 0.8006330202635291,
        "Milk, Butter, Yogurt -> Eggs": 0.8022155709223519,
        "Milk, Butter, Yogurt -> Eggs, Bread": 0.6717583513950528,
        "Milk, Butter, Yogurt -> Eggs, Cheese": 0.6679051845735715
    }
}
```
