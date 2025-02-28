import jwt

def createToken(datos:dict):
    token:str = jwt.encode(payload = datos, key = 'holi', algorithm = 'HS256')
    return token