from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
#from typing import List, Optional
#from pydantic import BaseModel
from modelsPydantic import modelUsuario
#from tokenGen import createToken
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter


routerUsuario = APIRouter()



#endpoint para consultar todos los usuarios
# @app.get("/usuarios", dependencies=[Depends(BearerJWT())] ,response_model = List[modelUsuario], tags=["Operaciones CRUD"])
@routerUsuario.get("/usuarios", tags=["Operaciones CRUD"])
def ConsultarTodos():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content = jsonable_encoder(consulta))
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje": "No fue posible consultar", "error": str(x)})

        
    finally:
        db.close()

@routerUsuario.get("/usuarios/{id}", tags=["Consultar un usuario por ID"])
def ConsultarUno(id:int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        return JSONResponse(content = jsonable_encoder(consulta))
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje": "No fue posible consultar", "error": str(x)})

    finally:
        db.close()


#endpoint para agregar un usuario por su id
@routerUsuario.post("/usuarios/", response_model = modelUsuario, tags=["Operaciones CRUD"])
def AgregarUsuario(usuarionuevo: modelUsuario):  # Usa el modelo Usuario en lugar de dict
    db = Session()
    try:
        db.add(User(**usuarionuevo.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"mensaje": "Usuario creado", "usuario": usuarionuevo.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "Error al crear el usuario", "error": str(e)})
    finally:
        db.close()
        
#endpoint para actualizar un usuario por su id
@routerUsuario.put("/usuarios/{id}", response_model=modelUsuario, tags=["Operacion de actualización"])
def ActualizarUsuario(id: int,  usuario_actualizado:modelUsuario):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        
        for key, value in usuario_actualizado.model_dump().items():
            setattr(consulta, key, value)
        
        db.commit()
        return JSONResponse(status_code=200, content={"mensaje": "Usuario actualizado", "usuario": usuario_actualizado.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "Error al actualizar el usuario", "error": str(e)})
    finally:
        db.close()
        
#endpoint para eliminar un usuario por su id
@routerUsuario.delete("/usuarios/{id}", tags=["Operacion de eliminación"])
def EliminarUsuario(id: int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()

        if not consulta:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        
        usuario_eliminado = jsonable_encoder(consulta)
        db.delete(consulta)
        db.commit()
        return JSONResponse(status_code=200, content={"mensaje": "Usuario eliminado", "usuario": usuario_eliminado})

    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "Error al eliminar el usuario", "error": str(e)})
    finally:
        db.close()