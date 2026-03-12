# Servicio de Cancelar Citas

## Endpoints implementados

### DELETE /citas/{id}
Cancela una cita médica por su ID.

**Parámetros**
| Parámetro | Tipo | Descripción        |
|-----------|------|--------------------|
| id        | int  | ID de la cita      |

**Ejemplo Request**
DELETE http://192.168.0.82:8005/citas/1

**Ejemplo Response**
{"mensaje": "Cita cancelada", "id": 1}

**Ejemplo Response (cita no encontrada)**
{"detail": "Cita no encontrada"}

## IP y Puerto
- IP: 192.168.0.82
- Puerto: 8005
- Swagger: http://192.168.0.82:8005/docs
