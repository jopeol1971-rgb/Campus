# Campus - Proyecto de Formación

## Descripción

**Campus** es un proyecto educativo desarrollado como ejercicio de formación en desarrollo web. Se trata de una aplicación web de autenticación de usuarios con un sistema de registro e inicio de sesión, donde los usuarios pueden crear una cuenta y acceder a su perfil personalizado.

Este proyecto combina múltiples tecnologías modernas para crear una aplicación funcional y segura, siendo ideal para aprender cómo integrar el frontend y backend en una aplicación real.

## Tecnologías Utilizadas

- **Frontend:**
  - HTML5 - Estructura de las páginas web
  - CSS3 - Estilos y diseño responsivo
  - JavaScript - Interactividad en el cliente

- **Backend:**
  - Python 3.x - Lenguaje de programación servidor
  - Flask 3.0.0 - Framework web minimalista
  - Werkzeug - Seguridad (hashing de contraseñas)

- **Base de Datos:**
  - PostgreSQL - Sistema gestor de base de datos relacional
  - psycopg2 - Adaptador Python para PostgreSQL

- **Herramientas:**
  - python-dotenv - Gestión segura de variables de entorno
  - Git - Control de versiones

## Características

✅ Sistema de registro de usuarios  
✅ Autenticación segura con hash de contraseñas  
✅ Sesiones de usuario  
✅ Página de perfil protegida  
✅ Cierre de sesión (logout)  

---

## Guía de Instalación y Configuración

### Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
- [Python 3.8+](https://www.python.org/downloads/)
- [PostgreSQL 12+](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/download/)

### Paso 1: Clonar el Repositorio

Abre tu terminal (PowerShell, CMD o Git Bash) y ejecuta:

```bash
git clone <URL-del-repositorio>
cd Campus
```

### Paso 2: Crear un Entorno Virtual

Crea un entorno virtual para aislar las dependencias del proyecto:

```bash
# En Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1

# O en Windows (CMD)
python -m venv venv
venv\Scripts\activate.bat

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

Una vez activado el entorno virtual, instala todas las dependencias:

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar la Base de Datos PostgreSQL

#### 4.1 Crear la Base de Datos

Abre PostgreSQL (pgAdmin o psql) y ejecuta:

```sql
CREATE DATABASE campus_db;
```

#### 4.2 Crear la Tabla de Usuarios

Conéctate a la base de datos recién creada y ejecuta:

```sql
\c campus_db;

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    usuario_email VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Explicación de la tabla:**
- `id` - Identificador único autoincrementable
- `usuario` - Nombre de usuario único
- `password` - Contraseña hasheada (nunca se almacena en texto plano)
- `usuario_email` - Email único del usuario
- `fecha_registro` - Timestamp de cuándo se registró el usuario

### Paso 5: Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con tus credenciales:

```ini
SECRET_KEY=tu-clave-secreta-super-segura-aqui

# Configuración de PostgreSQL
DB_HOST=localhost
DB_PORT=5432
DB_NAME=campus_db
DB_USER=postgres
DB_PASSWORD=tu-contraseña-postgres
```

**⚠️ Importante:** Nunca subas el archivo `.env` a Git. Ya está en el `.gitignore`.

### Paso 6: Ejecutar la Aplicación

Con el entorno virtual activado, inicia el servidor Flask:

```bash
flask --app hola run
```

La aplicación estará disponible en: **http://localhost:5000**

---

## Uso de la Aplicación

1. **Registro:** Accede a `http://localhost:5000/registro` para crear una nueva cuenta
2. **Login:** En la página principal (`http://localhost:5000/`), inicia sesión con tus credenciales
3. **Perfil:** Después de logged-in, verás tu página de perfil protegida (`/perfil`)
4. **Logout:** Haz clic en logout para cerrar tu sesión

---

## Estructura del Proyecto

```
Campus/
├── hola.py                 # Archivo principal con la aplicación Flask
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
├── License.md             # Licencia del proyecto
├── .env                   # Variables de entorno (no subir a Git)
├── .gitignore             # Archivos ignorados por Git
├── templates/             # Plantillas HTML
│   ├── base.html         # Template base
│   ├── login.html        # Página de login
│   ├── registro.html     # Página de registro
│   └── user.html         # Página de perfil
└── static/               # Archivos estáticos (CSS, JS, imágenes)
```

---

## Solución de Problemas

**Problema: "ModuleNotFoundError: No module named 'flask'"**
- Solución: Asegúrate de haber activado el entorno virtual y ejecutado `pip install -r requirements.txt`

**Problema: "psycopg2 connection error"**
- Solución: Verifica que PostgreSQL está corriendo y que las credenciales en `.env` son correctas

**Problema: "Secret key not set"**
- Solución: Asegúrate de crear el archivo `.env` con `SECRET_KEY` configurado

---

## Próximos Pasos para Mejorar

- 📱 Hacer la aplicación responsive (mobile-friendly)
- 🔐 Implementar recuperación de contraseña
- 📧 Enviar email de confirmación en registro
- 🎨 Mejorar el diseño de las páginas
- 📝 Añadir validaciones más robustas
- 🧪 Implementar tests unitarios

---

## Autor

Joaquín - Proyecto de Formación

## Licencia

Ver [License.md](License.md) para más detalles.
