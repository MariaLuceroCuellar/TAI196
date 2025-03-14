from pydantic import BaseModel, Field

class modelEnvio(BaseModel):
    CP: str = Field(..., min_length = 5, description="Código Postal debe ser una palabra de 5 letras")
    Destino: str = Field(..., min_length=6, description="solo letras y espacios min 6 letras")    
    Peso: int = Field(..., gt=0, lt=500, description="Peso del paquete en kilogramos")
