# 🗂️ Organizador de Archivos por Extensión

Este es un script en **Python** que organiza automáticamente los archivos de un directorio en carpetas según su extensión.  
Por ejemplo:  

- `documento.pdf` → `/PDF/`  
- `foto.jpg` → `/JPG/`  
- `script.py` → `/PY/`  
- `notas` (sin extensión) → `/SIN_EXTENSION/`  

---

## 🚀 Cómo usarlo

### 1. Requisitos
- Tener **Python 3.7+** instalado en tu sistema.  
  Verifica con:  
  ```bash
  python --versión

2. Clonar el repositorio

git clone https://github.com/TU-USUARIO/organizador-archivos.git
cd organizador-archivos

3. Ejecutar el script

En la terminal:

python organizador.py

Se pedirá la ruta del directorio a organizar:

👉 Ingresa la ruta del directorio a organizar: C:\Users\TuUsuario\Downloads

📂 Ejemplo

Antes:

Descargas/
├── documento.pdf
├── foto.jpg
├── musica.mp3
├── notas
├── script.py


Después de ejecutar el script:

Descargas/
├── PDF/
│   └── documento.pdf
├── JPG/
│   └── foto.jpg
├── MP3/
│   └── musica.mp3
├── SIN_EXTENSION/
│   └── notas
├── PY/
    └── script.py

⭐ Características

Organización automática por extensión.

Maneja archivos sin extensión.

Crea carpetas solo si son necesarias.

Compatible con Windows, Linux y macOS.

📌 Ideas de mejora

Añadir una interfaz gráfica (GUI) con Tkinter o PyQt.

Permitir configurar carpetas personalizadas (ej: todo lo de imágenes → “IMÁGENES”).

Integrar con un programador de tareas para que se ejecute automáticamente.