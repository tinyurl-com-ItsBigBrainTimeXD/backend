from flask import Flask
from constants import HOST, PORT


# Create the flask application
app = Flask(__name__)


# Create a basic route for debugging
@app.route('/')
def index():
    """The homepage for the api
        This is for debugging purposes
    """
    return '<h1>Hello world</h1>'


if __name__ == "__main__":
    app.run(HOST, PORT)
