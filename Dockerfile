# Usa una imagen base de Python
FROM python:3.9

# Configura el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt y las dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de la aplicación
COPY src/ /app/

# Exponer el puerto en el contenedor
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]