import server
import db
#Persona
#Car
if __name__=="__main__":
    db.Base.metadata.create_all(db.engine)
    server.app.run(host='0.0.0.0', port='8040', debug=True)

