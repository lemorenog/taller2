# 1. Usar una imagen base oficial de Python (ligera)
FROM python:3.9-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de requerimientos
COPY requirements.txt .

# 4. Instalar las dependencias (solo Flask en este caso)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo el código de la aplicación (app.py, etc.)
COPY . .

# 6. Exponer el puerto 80 (porque tu app.py corre en el puerto 80)
EXPOSE 80

# 7. El comando para ejecutar la aplicación cuando el contenedor inicie
CMD ["python", "app.py"]