FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código del proyecto
COPY . .

# Crear directorio para archivos estáticos
RUN mkdir -p /app/staticfiles

# Coleccionar archivos estáticos
RUN python manage.py collectstatic --noinput --clear

# Exponer puerto
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["gunicorn", "backend_analytics_server.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
