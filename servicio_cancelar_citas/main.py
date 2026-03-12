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
    return {"mensaje": "Servicio Cancelar Citas activo", "puerto": 8005}

@app.delete("/citas/{id}")
def cancelar_cita(id: int):
    try:
        conexion = get_db()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE citas SET estado='cancelada' WHERE id=%s",
            (id,)
        )
        conexion.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Cita no encontrada")
        return {"mensaje": "Cita cancelada", "id": id}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

