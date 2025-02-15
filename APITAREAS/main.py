#Api de Gestión de tareas
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI(
    title="API de Gestión de Tareas",
    description = "María Lucero Cuellar Araujo",
    version="1.0.1"
)

tareas = [
    {"id": 1, "nombre": "Tarea 1", "descripcion": "Realizar la tarea 1", "vencimiento": "14-02-2025","estado": "pendiente"},
    {"id": 2, "nombre": "Tarea 2", "descripcion": "Realizar la tarea 2", "vencimiento": "14-02-2025","estado": "pendiente"},
    {"id": 3, "nombre": "Tarea 3", "descripcion": "Realizar la tarea 3", "vencimiento": "14-02-2025","estado": "pendiente"},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Lucero"}

#Endponint para Obtener todas las tareas
@app.get("/tareas", tags=["Operaciones CRUD Obtener tareas"])
def obtener_tareas():
    return {"Todas las tareas": tareas}

#Endpoint para obtener una tarea por su id
@app.get("/tareas/{id}", tags=["Operaciones CRUD Obtener tareas por su ID"])
def obtener_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(status_code=400, detail="Tarea no encontrada")

#Endpoint para agregar una tarea
@app.post("/tareas", tags=["Operaciones CRUD Agregar tareas"])
def agregar_tarea(tarea: dict):
    tareas.append(tarea)
    return tarea



