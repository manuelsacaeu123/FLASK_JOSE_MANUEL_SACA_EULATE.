from flask import request, jsonify
import server
from controller import persona_controller
#create
@server.app.route('/personas', methods=['POST'])
def persona_create():
    return "persona_controller.persona_create()"

#read
@server.app.route('/personas/<id>', methods=['GET'])
def persona_read(id):
    return "persona_controller.persona_read(id)"

#read
@server.app.route('/personas', methods=['GET'])
def persona_read():
    return "persona_controller.persona_read()"
    """ return "API GET PERSONAS"
 """
#update
@server.app.route('/personas/<id>', methods=['PUT','PATCH'])
def persona_update(id):
    return "persona_controller.persona_update(id)"
    
#delete
@server.app.route('/personas/<id>', methods=['DELETE'])
def persona_read(id):
    return "persona_controller.persona_delete(id)"
