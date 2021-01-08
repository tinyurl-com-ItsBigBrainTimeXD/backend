import json
from flask import Flask, request
from constants import HOST, PORT
from Database.database import Database
from handler.frontendHandler import frontend_handler
from handler.iotHandler import iot_handler


# Create the flask application
app = Flask(__name__)

# Create the database
db = Database('test.db')


# Create a basic route for debugging
@app.route('/')
def index():
    """The homepage for the api
        This is for debugging purposes
    """
    return '<h1>Hello world</h1>'


# REST for frontend
@app.route('/frontend', methods=['POST', 'GET', 'PUT', 'DELETE'])
def frontend():
    """The endpoint for the frontend application to interact with"""

    # Get the body and the request type
    req_body = json.loads(request.get_json()) # Get as dict
    req_type = request.method

    return frontend_handler(req_body, req_type, db)


    # Get the body and the request type
    req_body = request.get_json()
    req_type = request.method

    return frontend_handler(req_body, req_type)
    


if __name__ == "__main__":
    app.run(HOST, PORT)
