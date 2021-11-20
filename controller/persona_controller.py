from flask import request, jsonfy
import server, db
from  entity.persona_entity import Persona

#create
def persona_create():
    json = request.json
    persona = Persona(**json)
    db.session.add(persona)
    db.session.commit()
    return jsonify(
        status = "success",
        data = json
    )

#read
def persona_read(id):
    persona = db.session.query(Persona).get(id)
    return jsonify(
        status = "success",
        data = persona.to_dict()
    )
    
#read
def persona_read():
    persona = db.session.query(Persona).all()
    return jsonify(
        status = "success",
        data =[persona.to_dict() for persona in personas]
    )

#update
def persona_update(id):
    json = request.json
    persona = db.session.query(Persona).get(id)
    for key, value in json.items():
        if hasattr(persona, key):
            setattr(persona, key, value)
    db.session.commit()
    return jsonify( 
        status = "success",
        data = persona.to_dict()
    )


#DELETE
def persona_delete(id):
    persona = db.session.query(Persona).get(id)
    db.session.delete(persona)
    db.session.commit()
    return jsonify( 
        status = "success",
        data = persona.to_dict()
    )

