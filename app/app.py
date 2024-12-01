from flask import Flask, request, jsonify
from app.generate_recipe import generate_recipe

app = Flask(__name__)

@app.route('/generate-recipe', methods=['POST'])
def generate_recipe_endpoint():
    # Get user input from the request
    data = request.get_json()
    user_text = data.get("user_text", "").strip()
    
    # Call the recipe generation function
    response = generate_recipe(user_text)
    
    # Handle errors
    if "error" in response:
        return jsonify({"error": response["error"]}), 400
    
    # Return the generated recipe
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
