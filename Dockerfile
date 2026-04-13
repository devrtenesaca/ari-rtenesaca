# 1. Usa una imagen base oficial de Python (ligera)
FROM python:3.9-slim

# 2. Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copia el archivo requirements.txt primero para aprovechar la caché de Docker
COPY requirements.txt .

# 4. Instala la librería 'requests' dentro del contenedor
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia el script Python y el archivo urls.txt al contenedor
COPY main.py urls.txt .

# 6. Comando por defecto para ejecutar el script cuando el contenedor inicie
CMD ["python", "main.py"]