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

## Base de datos
- Motor: MariaDB/MySQL
- Base de datos: citas_medicas
- Usuario: clase
- Contraseña: 1234
- Puerto: 3306

## Conexión a la base de datos

### Opción 1 - Desde la misma máquina
Si todos los servicios corren en el mismo equipo usar:
```python
host="127.0.0.1"
```

### Opción 2 - Desde otro equipo en la red
MariaDB corre dentro de WSL, por lo que se necesita
redirigir el puerto de Windows hacia WSL.

Ejecutar en PowerShell como administrador:
```powershell
netsh interface portproxy add v4tov4 listenport=3306 listenaddress=0.0.0.0 connectport=3306 connectaddress=172.19.64.246
```

Luego los otros equipos se conectan con:
```python
host="192.168.0.82"  # IP del equipo en la red del aula
```

## Flujo completo
1. Registrar paciente → `POST http://192.168.0.82:8001/pacientes`
2. Reservar cita → `POST http://192.168.0.82:9000/reservar-cita`
3. Consultar citas → `GET http://192.168.0.82:8004/citas/{paciente_id}`
4. Cancelar cita → `DELETE http://192.168.0.82:8005/citas/{id}`

## Tecnologías
- Python 3.12
- FastAPI
- Uvicorn
- MariaDB
- mysql-connector-python

## Cómo ejecutar cada servicio
```bash
cd servicio_pacientes && uvicorn main:app --host 0.0.0.0 --port 8001 --reload
cd servicio_citas && uvicorn main:app --host 0.0.0.0 --port 8003 --reload
cd servicio_consultar_citas && uvicorn main:app --host 0.0.0.0 --port 8004 --reload
cd servicio_cancelar_citas && uvicorn main:app --host 0.0.0.0 --port 8005 --reload
cd servicio_gateway && uvicorn main:app --host 0.0.0.0 --port 9000 --reload
```

