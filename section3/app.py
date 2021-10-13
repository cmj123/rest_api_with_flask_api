# Import required libraries, class
from flask import Flask

#Initialise a new flask application
app = Flask(__name__)

# Set the home request
@app.route('/')
def home():
    return "Hello, world!"

# Run the app
app.run(port=5000)
