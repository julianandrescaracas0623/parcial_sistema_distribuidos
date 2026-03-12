from fastapi import FastAPI, HTTPException
import mysql.connector

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Grupo 4 - Consultar Citas activo", "puerto": 8004}

@app.get("/citas/{paciente_id}")
def listar_citas(paciente_id: int):
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1", # aca colcaremos la IP de la red donde se encuentra la base de datos
            user="clase",
            password="1234",
            database="citas_medicas"
        )
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM citas WHERE paciente_id=%s",
            (paciente_id,)
        )
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))