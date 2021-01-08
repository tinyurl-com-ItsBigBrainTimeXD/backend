from flask import Flask, request, jsonify
from constants import HOST, PORT
from Database.database import Database
from handler.frontendHandler import frontend_handler
from handler.iotHandler import iot_handler


# Create the flask application
app = Flask(__name__)

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
    req_body = request.get_json()
    req_type = request.method
    db = Database('test.db')
    if req_body == None:
        return jsonify({"status_code": 404})
    result = frontend_handler(req_body, req_type, db)
    del db
    return jsonify(result)


# REST for IoT
@app.route('/device', methods=['POST', 'GET', 'PUT', 'DELETE'])
def iot():
    """The endpoint for the frontend application to interact with"""

    # Get the body and the request type
    req_body = json.loads(request.get_json())
    req_type = request.method.lower()

    db = Database('test.db')
    result = iot_handler(req_body, req_type, db)
    del db
    return result
    

if __name__ == "__main__":
    app.run(HOST, PORT)
