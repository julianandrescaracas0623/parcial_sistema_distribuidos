from fastapi import FastAPI, HTTPException
import mysql.connector

app = FastAPI()

def get_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="clase",
        password="1234",
        database="citas_medicas"
    )

@app.get("/")
def inicio():
    return {"mensaje": "Servicio Registro de Pacientes activo", "puerto": 8001}

@app.post("/pacientes")
def crear_paciente(nombre: str, email: str):
    try:
        conexion = get_db()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO pacientes(nombre, email) VALUES(%s, %s)",
            (nombre, email)
        )
        conexion.commit()
        return {"mensaje": "Paciente registrado", "nombre": nombre, "email": email}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/pacientes/{id}")
def obtener_paciente(id: int):
    try:
        conexion = get_db()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pacientes WHERE id=%s", (id,))
        paciente = cursor.fetchone()
        if not paciente:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        return paciente
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
