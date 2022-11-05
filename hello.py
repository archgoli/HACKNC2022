from flask import Flask  # Import the Flask object from the flask package

# Use Flask object to create Flask application instance with the name app
app = Flask(__name__)  # Variable __name__ holds the name of the current python module; tells the instance where it's located


# app instance used to handle incoming web requests and send responses to the user
@app.route('/')  # decorator; turns regular Python function into a Flask view function
# Flask view function: converts the function's return value into an HTTP response to be displayed by an HTTP client (i.e. web browser)
# '/' signifies that function responds to web requests for the URL /

def hello () -> str:
    return 'Hello, World!'
