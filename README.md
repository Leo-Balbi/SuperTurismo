# 🏎️ SuperTurismo - Sistema de Gestión de Precintos y Piezas


SuperTurismo es una aplicación de escritorio/web construida con [Flet](https://flet.dev/), diseñada para el **equipo de ingenieros de competición**, con el objetivo de gestionar:

- 🔧 Control de piezas y precintos de cada motor.  
- 📂 Carga de información manual y mediante archivos **Excel**.  
- 👨‍👩‍👧‍👦 Asociación de pilotos con sus respectivos equipos (12 equipos, 24 pilotos).  
- 📝 Registro de motivos de reemplazo de piezas y situaciones en que ocurrieron (*Práctica, Clasificación, Carrera*).  
- 📊 Visualización interactiva de datos en un **Dashboard profesional** con tablas y gráficos.  
- 🕒 Gestión por **Temporadas y fechas** (ej: Temporada 1 - viernes práctica, sábado clasificación, domingo carrera).  

---

## ✨ Características Principales

✅ **Interfaz moderna y en modo oscuro** con colores personalizados (rojo/blanco).  
✅ **Ingreso de registros manuales** con formularios dinámicos.  
✅ **Carga de archivos Excel** para notificación de cambios de piezas.  
✅ **Dashboard con visualizaciones** para analizar reemplazos y estadísticas.  
✅ **Base de datos SQLite integrada**, simple y portable.  
✅ **Arquitectura modular** con carpetas separadas para vistas, componentes, base de datos y utilidades.  

---

## 📂 Estructura del Proyecto

```bash
SuperTurismo/
│── main.py                # Punto de entrada de la app
│
├── app/
│   ├── routes.py          # Sistema de rutas
│   ├── views/             # Vistas principales
│   ├── components/        # Navbar, formularios y gráficos
│   ├── db/                # Base de datos y queries
│   └── utils/             # Constantes y funciones auxiliares
│
├── data/                  # Archivos persistentes
│   ├── superturismo.db    # Base de datos SQLite
│   ├── example.xlsx       # Ejemplo de carga Excel
│
├── assets/                # Recursos gráficos (logo, imágenes)
│   └── logo.png
│
└── README.md

## 🚀 Instalación y Ejecución

    1️⃣ Clonar el repositorio
    git clone https://github.com/TU_USUARIO/SuperTurismo.git
    cd SuperTurismo
   
    2️⃣ Crear un entorno virtual (recomendado)
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

    3️⃣ Instalar dependencias
    pip install -r requirements.txt

    4️⃣ Ejecutar la aplicación
        python main.py
        (La aplicación se abrirá en modo escritorio o en el navegador en http://localhost:8550
.)


📊 Tecnologías Utilizadas

Python 3.10+
 🐍

Flet
 🌐 (UI moderna en Python con estilo Flutter)

SQLite3
 🗄️ (Base de datos embebida y portable)

Pandas
 📈 (Procesamiento de datos)

Matplotlib
 📊 (Visualización de datos)


 🏁 Flujo de Uso

Ingreso Manual → El ingeniero registra precintos, piezas y motivos.

Carga de Excel → Los equipos suben sus reportes semanales.

Validación y Registro → Los datos quedan almacenados en la base local SQLite.

Dashboard → Los ingenieros visualizan estadísticas por temporada, piloto, equipo o pieza.

🤝 Contribución

Este proyecto fue diseñado para un entorno profesional de ingeniería en automovilismo.
Si quieres mejorarlo, puedes contribuir con:

⚡ Mejoras en la interfaz.

📊 Nuevas visualizaciones.

🛠️ Integración con APIs externas (telemetría, sensores).

📜 Licencia

Este proyecto se distribuye bajo la licencia MIT.
Eres libre de usarlo, modificarlo y adaptarlo a tus necesidades.

🏎️ SuperTurismo:
"Donde cada precinto cuenta y cada carrera importa."
