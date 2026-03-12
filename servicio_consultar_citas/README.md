# Servicio de Consultar Citas

## Endpoints implementados

### GET /citas/{paciente_id}
Consulta todas las citas de un paciente.

**Parámetros**
| Parámetro   | Tipo | Descripción             |
|-------------|------|-------------------------|
| paciente_id | int  | ID del paciente         |

**Ejemplo Request**
GET http://192.168.0.82:8004/citas/1

**Ejemplo Response**
[
  {
    "id": 1,
    "paciente_id": 1,
    "fecha": "2026-03-20T10:00:00",
    "estado": "activa"
  }
]

**Ejemplo Response (sin citas)**
[]

## IP y Puerto
- IP: 192.168.0.82
- Puerto: 8004
- Swagger: http://192.168.0.82:8004/docs
