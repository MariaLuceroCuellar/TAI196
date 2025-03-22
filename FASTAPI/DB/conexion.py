import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Nombre de la base de datos
dbname= 'usuarios.sqlite'
#Ruta de la base de datos
base_dir = os.path.dirname(os.path.realpath(__file__))
#URL de la base de datos
dbUrl = f"sqlite:///{os.path.join(base_dir, dbname)}"

#Creación de la conexión a la base de datos
engine = create_engine(dbUrl, echo=True)
#se crea la sesión de la base de datos para poder hacer las consultas
Session = sessionmaker(bind=engine)
#se declara la base de datos para poder crear las tablas
Base = declarative_base()

