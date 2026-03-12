# Servicio de Crear Citas

## Endpoints implementados

### POST /citas
Crea una nueva cita médica.

**Parámetros**
| Parámetro   | Tipo   | Descripción                    |
|-------------|--------|--------------------------------|
| paciente_id | int    | ID del paciente                |
| fecha       | string | Fecha y hora de la cita        |

**Ejemplo Request**
POST http://192.168.0.82:8003/citas?paciente_id=1&fecha=2026-03-20 10:00:00

**Ejemplo Response**
{"mensaje": "Cita creada", "paciente_id": 1, "fecha": "2026-03-20 10:00:00"}

**Nota**
Este servicio consulta el servicio de pacientes (puerto 8001)
antes de crear la cita para verificar que el paciente existe.

## IP y Puerto
- IP: 192.168.0.82
- Puerto: 8003
- Swagger: http://192.168.0.82:8003/docs
