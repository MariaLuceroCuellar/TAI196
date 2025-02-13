from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Mi primera API-196",
    description="María Lucero Cuellar Araujo",
    version="1.0.1"
)

# Modelo de datos con Pydantic
class Usuario(BaseModel):
    id: int
    nombre: str
    edad: int

usuarios = [
    {"id": 1, "nombre": "Lucero", "edad": 21},
    {"id": 2, "nombre": "Estrella", "edad": 22},
    {"id": 3, "nombre": "Lalin", "edad": 23},
    {"id": 4, "nombre": "Ligorin", "edad": 24},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Lucero"}

@app.get("/usuarios", tags=["Operaciones CRUD"])
def ConsultarTodos():
    return {"Todos los usuarios registrados": usuarios}

@app.post("/usuarios/", tags=["Operaciones CRUD"])
def AgregarUsuario(usuarionuevo: Usuario):  # Usa el modelo Usuario en lugar de dict
    for usr in usuarios:
        if usr["id"] == usuarionuevo.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    usuarios.append(usuarionuevo.dict())  # Convierte el modelo a diccionario antes de agregarlo
    return {"Usuario Agregado": "Exitosamente"}
