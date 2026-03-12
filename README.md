# Sistema Distribuido de Citas Médicas

Sistema de microservicios para gestión de citas médicas desarrollado con FastAPI y MariaDB.

## Arquitectura

| Servicio                    | Endpoint                  | Puerto |
|-----------------------------|---------------------------|--------|
| Registro/Consulta pacientes | POST/GET /pacientes       | 8001   |
| Crear citas                 | POST /citas               | 8003   |
| Consultar citas             | GET /citas/{paciente_id}  | 8004   |
| Cancelar citas              | DELETE /citas/{id}        | 8005   |
| API Gateway                 | POST /reservar-cita       | 9000   |

## Requisitos
- Python 3.12
- pip
- WSL (si usas Windows)

## Instalación y ejecución

Clona el repositorio:
```bash
git clone https://github.com/julianandrescaracas0623/parcial_sistema_distribuidos.git
cd parcial_sistema_distribuidos
```

Para cada servicio, abre una terminal y ejecuta:
```bash
cd servicio_pacientes
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

Repite el mismo proceso para cada servicio cambiando la carpeta y el puerto:
- `servicio_citas` → puerto 8003
- `servicio_consultar_citas` → puerto 8004
- `servicio_cancelar_citas` → puerto 8005
- `servicio_gateway` → puerto 9000

## Conexión a la base de datos

### Opción 1 - Desde la misma máquina
```python
host="127.0.0.1"
```

### Opción 2 - Desde otro equipo en la red
Ejecutar en PowerShell como administrador:
```powershell
netsh interface portproxy add v4tov4 listenport=3306 listenaddress=0.0.0.0 connectport=3306 connectaddress=172.19.64.246
```

Luego conectarse con:
```python
host="192.168.0.82"
```

## Flujo de pruebas
1. Registrar paciente → `POST http://192.168.0.82:8001/pacientes`
2. Reservar cita → `POST http://192.168.0.82:9000/reservar-cita`
3. Consultar citas → `GET http://192.168.0.82:8004/citas/{paciente_id}`
4. Cancelar cita → `DELETE http://192.168.0.82:8005/citas/{id}`

## Swagger UI de cada servicio
- http://192.168.0.82:8001/docs
- http://192.168.0.82:8003/docs
- http://192.168.0.82:8004/docs
- http://192.168.0.82:8005/docs
- http://192.168.0.82:9000/docs
