from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title = ('Mi primera API-196'),
    description = ('María Lucero Cuellar Araujo'),
    version = ('1.0.1')
)

usuarios=[
    {'id':1, 'nombre':'Lucero', 'edad':21},
    {'id':2, 'nombre':'Estrella', 'edad':22},
    {'id':3, 'nombre':'Lalin', 'edad':23},
    {'id':4, 'nombre':'Ligorin', 'edad':24},
    ]

@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FastAPI': 'Lucero'}


@app.get('/promedio', tags=['Mi calificación TAI'])
def promedio():
    return {'Promedio': 9.55}


#endpoint parametro obligatorio
@app.get('/usuario/{id}', tags=['Parametro Obligatorio'])
def consultarUsuario(id: int):
    #conectamos a la base de datos
    #hacemos la consulta y retornamos el resultado
    return {'Usuario encontrado': id}

#endpoint parametro opcional
@app.get('/usuario2/', tags=['Parametro Opcional'])
def consultarUsuarioOpcional(id: Optional[int] = None):
    if id is not None:
        for usuario in usuarios:
            if usuario['id'] == id: 
                return {'Usuario encontrado': usuario}
        return {'Mensaje':f'No se encontrado el id: {id}'}
    else:
        return{'mensaje': 'No hay usuarios registrados'}
   
#endpoint con varios parametro opcionales
@app.get("/usuarios3/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}