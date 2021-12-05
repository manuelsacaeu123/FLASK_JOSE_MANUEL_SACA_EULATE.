from flask import request, jsonify
import server
from controller import car_controller
#create
@server.app.route('/cars', methods=['POST'])
def car_create():
    return "car_controller.car_create()"

#read
@server.app.route('/cars/<id>', methods=['GET'])
def car_read(id):
    return "car_controller.car_read(id)"

#read
@server.app.route('/cars', methods=['GET'])
def car_read():
    return "car_controller.car_read()"
    """ return "API GET CARS"
 """
#update
@server.app.route('/cars/<id>', methods=['PUT','PATCH'])
def car_update(id):
    return "car_controller.car_update(id)"
    
#delete
@server.app.route('/cars/<id>', methods=['DELETE'])
def car_read(id):
    return "car_controller.car_delete(id)"
