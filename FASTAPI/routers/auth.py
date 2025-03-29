from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
#from fastapi.encoders import jsonable_encoder
#from typing import List, Optional
#from pydantic import BaseModel
from modelsPydantic import modelAuth
from tokenGen import createToken
#from middlewares import BearerJWT
#from DB.conexion import Session
#from models.modelsDB import User
from fastapi import APIRouter


routerAuth = APIRouter()

@routerAuth.post('/auth', tags=["Autentificación"])
def login(autorizado: modelAuth):
    if autorizado.correo == "lucero@example.com" and autorizado.passw == "12345678":
        token: str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content={"token": token})
    else:
        return {"Error": "Usuario incorrecto "}