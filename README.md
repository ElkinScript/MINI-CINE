# Mi Proyecto Django

Una aplicación web desarrollada con Django que utiliza Bootstrap para el diseño responsivo. Este proyecto no requiere base de datos ya que no almacena registros permanentes.

## 🛠️ Tecnologías Utilizadas

- **Django** - Framework web de Python
- **Bootstrap** - Framework CSS para diseño responsivo
- **HTML5** - Estructura del contenido
- **CSS3** - Estilos personalizados
- **JavaScript** - Interactividad del frontend
- **Python** - Lenguaje de programación del backend
- **jQuery** - Biblioteca de JavaScript para manipulación del DOM
- **Font Awesome** - Iconos vectoriales
- **AJAX** - Para solicitudes asíncronas
- **Django REST Framework** - Para crear APIs RESTful

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

## Configurar variables de entorno
Asegúrate de configurar las variables de entorno necesarias para tu proyecto. Puedes crear un archivo `.env` en la raíz del proyecto y definir las variables que necesites, como `SECRET_KEY`, `DEBUG`, etc.

```plaintext
cp .env.example .env
```
## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/ElkinScript/nombre-del-repositorio.git
cd nombre-del-repositorio

### 2. Crear un entorno virtual
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate  # En Windows

### 3. Instalar las dependencias
pip install -r requirements.txt

### 4. Ejecutar el servidor de desarrollo
python manage.py runserver
```

