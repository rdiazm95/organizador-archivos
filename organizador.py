import os
import shutil

def organizar_archivos(directorio):
    """
    Organiza los archivos de un directorio en carpetas según su extensión.
    
    Ejemplo:
    - documento.pdf  --> /PDF/
    - foto.jpg       --> /JPG/
    - script.py      --> /PY/
    """

    if not os.path.exists(directorio):
        print(f"❌ El directorio '{directorio}' no existe.")
        return

    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)

        # Saltar directorios
        if os.path.isdir(ruta_archivo):
            continue

        # Obtener extensión (sin el punto, en mayúsculas)
        _, extension = os.path.splitext(archivo)
        if extension:
            extension = extension[1:].upper()  # "pdf" -> "PDF"
        else:
            extension = "SIN_EXTENSION"

        carpeta_destino = os.path.join(directorio, extension)

        # Crear carpeta si no existe
        os.makedirs(carpeta_destino, exist_ok=True)

        # Mover archivo
        shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))

    print("✅ Archivos organizados correctamente.")


if __name__ == "__main__":
    ruta = input("👉 Ingresa la ruta del directorio a organizar: ").strip()
    organizar_archivos(ruta)
