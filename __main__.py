from multiprocessing import Lock
from flask import Flask, request, jsonify
from constants import HOST, PORT
from Database.database import Database
from handler.frontendHandler import frontend_handler
from handler.iotHandler import iot_handler


# Create the flask application
app = Flask(__name__)
db_name = 'test.db'
db_lock = Lock()


# Create a basic route for debugging
@app.route('/')
def index():
    """The homepage for the api
        This is for debugging purposes
    """
    return '<h1>Hello world</h1>'


# REST for frontend
@app.route('/frontend/<query>', methods=['GET'])
def front_end_get(query):
    """Get data"""
    # Get the body and the request type
    if not query.isdigit():
        return 404
    req_body = {'type': int(query)}
    req_type = request.method
    req_body.update(request.args)
    db_lock.acquire(True)
    db = Database(db_name)
    result = frontend_handler(req_body, req_type, db)
    del db
    db_lock.release()
    return jsonify(result)
    

@app.route('/frontend', methods=['POST', 'PUT', 'DELETE'])
def frontend():
    """The endpoint for the frontend application to interact with"""
    # Get the body and the request type
    req_body = request.get_json()
    req_type = request.method
    db_lock.acquire(True)
    db = Database(db_name)
    result = frontend_handler(req_body, req_type, db)
    del db
    db_lock.release()
    return jsonify(result)


@app.route('/device/<query>', methods = ['GET'])
def iot_get(query):
    req_body = {'type': query}
    req_type = request.method.lower()
    result = iot_handler(req_body, req_type)
    return jsonify(result)

# REST for IoT
@app.route('/device', methods=['POST'])
def iot():
    """The endpoint for the frontend application to interact with"""

    # Get the body and the request type
    req_body = request.get_json()
    req_type = request.method.lower()
    result = iot_handler(req_body, req_type)
    return jsonify(result)


if __name__ == "__main__":
    app.run(HOST, PORT)
