from flask.globals import session
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

provider ='mysql+pymysql'
database = 'registrovehiculos'
serverDB = 'localhost'
port = '3306'
user ='root'
password = ''

engine = create_engine(provider+"://"+user+":"+password+"@"+serverDB+"/"+database+"?charset=utf8mb4")
Session =sessionmaker(bind=engine)
session = Session()

Base = declarative_base()