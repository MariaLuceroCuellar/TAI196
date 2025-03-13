from pydantic import BaseModel, Field
#Modelo para validaciones del usuario
class modelUsuario(BaseModel):
    id: int = Field(..., gt=0, description="ID unico del usuario y solo son numeros positivos")
    nombre: str = Field(..., min_length=3, max_length=50, description="Nombre del usuario")
    edad: int = Field(..., gt=1, it=130, description="debe de ser mayor a 1 y menor a 2 Edad del usuario")
    correo: str = Field(..., pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", example="usuario@example.com", description="Correo del usuario")