from pydantic import BaseModel, Field, EmailStr
#Modelo para validaciones del usuario
class modelUsuario(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Nombre del usuario")
    age: int = Field(..., gt=1, it=130, description="debe de ser mayor a 1 y menor a 2 Edad del usuario")
    email: str = Field(..., pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", example="usuario@example.com", description="Correo del usuario")

class modelAuth(BaseModel):
    correo:EmailStr
    passw: str = Field(..., min_length=8, strip_whiteespace=True, description="Contraseña minimo de 8 caracteres ")