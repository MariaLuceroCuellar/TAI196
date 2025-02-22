from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel


app = FastAPI(
    title="Mi primera API-196",
    description="María Lucero Cuellar Araujo",
    version="1.0.1"
)

#Modelo para validaciones del usuario
class modelUsuario(BaseModel):
    id: int
    nombre: str
    edad: int
    correo: str

usuarios = [
    {"id": 1, "nombre": "Lucero", "edad": 21, "correo": "lucero@example"},
    {"id": 2, "nombre": "Estrella", "edad": 22,"correo": "estrella@example"},
    {"id": 3, "nombre": "Lalin", "edad": 23, "correo": "lalin@example"},
    {"id": 4, "nombre": "Ligorin", "edad": 24, "correo": "ligorin@example"},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Lucero"}
#endpoint para consultar todos los usuarios
@app.get("/usuarios", response_model = List[modelUsuario], tags=["Operaciones CRUD"])
def ConsultarTodos():
    return usuarios

#endpoint para agregar un usuario por su id
@app.post("/usuarios/", response_model = modelUsuario, tags=["Operaciones CRUD"])
def AgregarUsuario(usuarionuevo: modelUsuario):  # Usa el modelo Usuario en lugar de dict
    for usr in usuarios:
        if usr["id"] == usuarionuevo.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    usuarios.append(usuarionuevo)  
    return usuarionuevo

#endpoint para actualizar un usuario por su id
@app.put("/usuarios/{id}", response_model=modelUsuario, tags=["Operacion de actualización"])
def ActualizarUsuario(id: int,  usuario_actualizado:modelUsuario):
    for usr in usuarios:
        if usr["id"] == id:
            usr.update(usuario_actualizado)
            return {"Usuario actualizado": usr}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

        
#endpoint para eliminar un usuario por su id    
@app.delete("/usuarios/{id}", tags=["Operacion de eliminación"])
def EliminarUsuario(id: int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"Usuario eliminado": usr}
    raise HTTPException(status_code=400, detail="El usuario no existe")

