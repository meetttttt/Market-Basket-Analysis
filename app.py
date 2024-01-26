"""
This is actual flask api file, where multiple routes are been written.
Make sure to install the requirements
"""

# Imports are written here
import logging
from flask import Flask, jsonify, Response, request
from utils import load_data, perform_market_basket_analysis, recommend_items

# Setting up Logging
logging.basicConfig(filename="log.log",
                    format="%(asctime)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    level=logging.INFO)


# Initialize the Flask app
app = Flask(__name__)


# Testing Route
@app.route('/home')
def hello() -> Response:
    logging.info(f"Home Endpoint Here")
    return jsonify({"status": "Working....!"})


# Recommend route
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json.get('data')  # Assuming JSON data with 'data' key
        loaded_te, original_data = load_data()

        rules = perform_market_basket_analysis(original_data, loaded_te)

        output_dict = recommend_items(data, rules, loaded_te)

        return jsonify(output_dict)

    except Exception as e:
        return jsonify({'error': f"Error occurred: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=False,
            host="0.0.0.0",
            port=5000)
