from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load responses from JSON file
with open('responses.json', 'r') as file:
    responses = json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['user_input'].lower()
    response = "I don't understand."

    # Check if any keyword is present in the user input
    for keyword in responses:
        if keyword in user_input:
            response = responses[keyword]
            break

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
