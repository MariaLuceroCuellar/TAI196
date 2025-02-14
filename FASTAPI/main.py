from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI(
    title="Mi primera API-196",
    description="María Lucero Cuellar Araujo",
    version="1.0.1"
)

usuarios = [
    {"id": 1, "nombre": "Lucero", "edad": 21},
    {"id": 2, "nombre": "Estrella", "edad": 22},
    {"id": 3, "nombre": "Lalin", "edad": 23},
    {"id": 4, "nombre": "Ligorin", "edad": 24},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Lucero"}
#endpoint para consultar todos los usuarios
@app.get("/usuarios", tags=["Operaciones CRUD"])
def ConsultarTodos():
    return {"Todos los usuarios registrados": usuarios}

#endpoint para consultar un usuario por su id
@app.post("/usuarios/", tags=["Operaciones CRUD"])
def AgregarUsuario(usuario: dict):  # Usa el modelo Usuario en lugar de dict
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    usuarios.append(usuario)  
    return usuario

#endpoint para actualizar un usuario por su id
@app.put("/usuarios/{id}", tags=["Operacion de actualización"])
def ActualizarUsuario(id: int,  usuario:dict):
    for usr in usuarios:
        if usr["id"] == id:
            usr.update(usuario)
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

