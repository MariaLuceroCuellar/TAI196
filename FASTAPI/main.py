
from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

#Levanta las tablas defenidas en los modelos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mi primera API-196",
    description="María Lucero Cuellar Araujo",
    version="1.0.1"
)
app.include_router(routerUsuario)
app.include_router(routerAuth)

usuarios = [
    {"id": 1, "nombre": "Lucero", "edad": 21, "correo": "lucero@example.com"},
    {"id": 2, "nombre": "Estrella", "edad": 22,"correo": "estrella@example.com"},
    {"id": 3, "nombre": "Lalin", "edad": 23, "correo": "lalin@example.com"},
    {"id": 4, "nombre": "Ligorin", "edad": 24, "correo": "ligorin@example.com"},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Lucero"}





        
        
        
#endpoint para actualizar un usuario por su id
# @app.put("/usuarios/{id}", response_model=modelUsuario, tags=["Operacion de actualización"])
# def ActualizarUsuario(id: int,  usuario_actualizado:modelUsuario):
#     for index, usr in usuarios:
#         if usr["id"] == id:
#             usr[index] = usuario_actualizado.model_dump()
#             return [index]
#     raise HTTPException(status_code=404, detail="Usuario no encontrado")

        
# #endpoint para eliminar un usuario por su id    
# @app.delete("/usuarios/{id}", tags=["Operacion de eliminación"])
# def EliminarUsuario(id: int):
#     for usr in usuarios:
#         if usr["id"] == id:
#             usuarios.remove(usr)
#             return {"Usuario eliminado": usr}
#     raise HTTPException(status_code=400, detail="El usuario no existe")

