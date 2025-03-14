from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from modelsPydantic import modelEnvio

app = FastAPI(
    title="Examen de un de Envios API-196",
    description="María Lucero Cuellar Araujo",
    version="1.0.1"
)


envios = [
    {"CP": "Queretaro", "Destino": "CIUDAD DE MEXICO", "Peso": 10},
    {"CP": "WDRGT", "Destino": "QUERETARO", "Peso": 20},
    {"CP": "FRWSS", "Destino": "PEDRO ESCOBEDO", "Peso": 30},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Luceroooo"}

@app.get("/envios", response_model = List[modelEnvio], tags=["Operaciones CRUD"])
def get_envios():
    return envios




@app.get("/envios/{CP}", response_model = modelEnvio, tags=["Operaciones CRUD"])
def get_envio(CP: str):
    for envio in envios:
        if envio["CP"] == CP:
            return envio
    raise HTTPException(status_code=404, detail="Envio no encontrado")

@app.put("/envios/{CP}", response_model = modelEnvio, tags=["Operaciones CRUD"])
def update_envio(CP: str, envio_actualizado: modelEnvio):
    for index, envio in enumerate(envios):
        if envio["CP"] == CP:
            envios[index] = envio_actualizado.model_dump()
            return envios[index]
    raise HTTPException(status_code=404, detail="Envio no encontrado")

