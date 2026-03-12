# API Gateway

## Endpoints implementados

### POST /reservar-cita
Reserva una cita médica. Consume el servicio de pacientes
y el servicio de crear citas.

**Parámetros**
| Parámetro   | Tipo   | Descripción                    |
|-------------|--------|--------------------------------|
| paciente_id | int    | ID del paciente                |
| fecha       | string | Fecha y hora de la cita        |

**Ejemplo Request**
POST http://192.168.0.82:9000/reservar-cita?paciente_id=1&fecha=2026-03-20 10:00:00

**Ejemplo Response**
{
  "mensaje": "Cita reservada exitosamente",
  "paciente": {
    "id": 1,
    "nombre": "Juan",
    "email": "juan@test.com"
  },
  "cita": {
    "mensaje": "Cita creada",
    "paciente_id": 1,
    "fecha": "2026-03-20 10:00:00"
  }
}

## Servicios que consume
- Servicio de pacientes: http://192.168.0.82:8001
- Servicio de citas: http://192.168.0.82:8003

## IP y Puerto
- IP: 192.168.0.82
- Puerto: 9000
- Swagger: http://192.168.0.82:9000/docs
