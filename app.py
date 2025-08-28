from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load predefined responses from JSON file
with open('responses.json', 'r') as file:
    responses = json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message'].lower().strip()
    # Default response if no match is found
    bot_response = "Sorry, I don't understand that. Try asking something else!"
    
    # Check for matching keywords in responses
    for key, value in responses.items():
        if key in user_message:
            bot_response = value
            break
    
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
