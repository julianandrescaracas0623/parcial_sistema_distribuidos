# Servicio de Pacientes

## Endpoints implementados

### POST /pacientes
Registra un nuevo paciente.

**Parámetros**
| Parámetro | Tipo   | Descripción           |
|-----------|--------|-----------------------|
| nombre    | string | Nombre del paciente   |
| email     | string | Email del paciente    |

**Ejemplo Request**
POST http://192.168.0.82:8001/pacientes?nombre=Juan&email=juan@test.com

**Ejemplo Response**
{"mensaje": "Paciente registrado", "nombre": "Juan", "email": "juan@test.com"}

---

### GET /pacientes/{id}
Consulta un paciente por su ID.

**Parámetros**
| Parámetro | Tipo | Descripción          |
|-----------|------|----------------------|
| id        | int  | ID del paciente      |

**Ejemplo Request**
GET http://192.168.0.82:8001/pacientes/1

**Ejemplo Response**
{"id": 1, "nombre": "Juan", "email": "juan@test.com"}

## IP y Puerto
- IP: 192.168.0.82
- Puerto: 8001
- Swagger: http://192.168.0.82:8001/docs
