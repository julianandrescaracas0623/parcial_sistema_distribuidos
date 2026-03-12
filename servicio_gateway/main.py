from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API Gateway activo", "puerto": 8000}

@app.post("/reservar-cita")
def reservar_cita(paciente_id: int, fecha: str):
    try:
        # 1. Verificar que el paciente existe
        r_paciente = requests.get(f"http://127.0.0.1:8001/pacientes/{paciente_id}")
        if r_paciente.status_code != 200:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")

        # 2. Crear la cita
        r_cita = requests.post(
            "http://127.0.0.1:8003/citas",
            params={"paciente_id": paciente_id, "fecha": fecha}
        )
        if r_cita.status_code != 200:
            raise HTTPException(status_code=500, detail="Error al crear la cita")

        return {
            "mensaje": "Cita reservada exitosamente",
            "paciente": r_paciente.json(),
            "cita": r_cita.json()
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
