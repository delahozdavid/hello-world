from fastapi import FastAPI

app = FastAPI()

@app.get("/usuario")
async def read_user_info():
    user_info = {
        "nombre": "David Castro",
        "correo": "castrodavidd@hotmail.com"
    }
    return user_info


