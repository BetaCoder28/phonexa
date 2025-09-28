# Phonexa API

API REST desarrollada con Django y Django REST Framework para la gestión de usuarios y flashcards.

## 📚 API Endpoints

### 🔐 Autenticación

#### Obtener Token de Acceso
```http
POST /api/token/
Content-Type: application/json

{
  "email": "usuario@ejemplo.com",
  "password": "contraseña123"
}
```

**Respuesta:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### Refrescar Token
```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 👥 Usuarios

#### Crear Usuario
```http
POST /api/users/create/
Content-Type: application/json

{
  "name": "Juan Pérez",
  "email": "juan@ejemplo.com",
  "password": "contraseña123",
  "password_confirm": "contraseña123",
  "isPremiumUser": false
}
```

**Respuesta:**
```json
{
  "message": "Usuario creado correctamente"
}
```

#### Listar Usuarios
```http
GET /api/users/
Authorization: Bearer <access_token>
```

**Respuesta:**
```json
[
  {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@ejemplo.com",
    "isPremiumUser": false,
    "date_joined": "2024-01-15T10:30:00Z",
    "is_active": true
  }
]
```

#### Obtener Usuario por ID
```http
GET /api/users/{id}/
Authorization: Bearer <access_token>
```

**Respuesta:**
```json
{
  "id": 1,
  "name": "Juan Pérez",
  "email": "juan@ejemplo.com",
  "isPremiumUser": false,
  "date_joined": "2024-01-15T10:30:00Z",
  "is_active": true
}
```

### 🔧 Administración

#### Panel de Administración
```http
GET /admin/
```

