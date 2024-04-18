from flask import Flask, request

app = Flask(__name__)

# Defining the route for receiving messages
@app.route('/.', methods=['POST'])
def chat():
    # Getting the user's message from the request
    user_message = request.form['message']
    
    # Responding with a "Hello, World!" message
    response = 'Hello, World!'
    
    # Returning the response to the user
    return response

# Running the Flask application
if __name__ == '__main__':
    app.run()