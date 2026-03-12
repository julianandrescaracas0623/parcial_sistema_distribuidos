from fastapi import FastAPI, HTTPException
import mysql.connector
import requests

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
    return {"mensaje": "Servicio Crear Citas activo", "puerto": 8003}

@app.post("/citas")
def crear_cita(paciente_id: int, fecha: str):
    try:
        # Verificar que el paciente existe
        r = requests.get(f"http://127.0.0.1:8001/pacientes/{paciente_id}")
        if r.status_code != 200:
            raise HTTPException(status_code=404, detail="Paciente no existe")
        
        conexion = get_db()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO citas(paciente_id, fecha, estado) VALUES(%s, %s, 'activa')",
            (paciente_id, fecha)
        )
        conexion.commit()
        return {"mensaje": "Cita creada", "paciente_id": paciente_id, "fecha": fecha}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
