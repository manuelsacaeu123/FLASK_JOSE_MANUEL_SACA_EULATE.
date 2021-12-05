import server
import db
#Persona
#Car 
import entity.persona_entity
import entity.car_entity

import route.persona_route
import route.car_route
import route.upload_route
import route.download_route

  
if __name__=="__main__":
    #conexion
    db.Base.metadata.create_all(db.engine)

    #iniciar db
    server.app.run(host='0.0.0.0', port='8040', debug=True)

 