#Esta libreria nos permite crear la base de datos
from DB.conexion import Base 
#Esta libreria nos permite crear las columnas de la base de datos
from sqlalchemy import Column, Integer, String 

#Se crea la clase User que hereda de la Base
class User(Base):
    __tablename__ = 'tb_users'
    id = Column(Integer, primary_key=True, autoincrement= "auto")
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
   