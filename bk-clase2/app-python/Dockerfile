# ==========================
# STAGE 1: BUILD (compilación)
# ==========================
FROM python:3.11-alpine AS builder

# Variables de entorno para instalación
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copiamos archivos necesarios
COPY requirements.txt .

# Instalamos dependencias en una carpeta temporal
RUN mkdir -p /install && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt

# ==========================
# STAGE 2: RUNTIME (producción)
# ==========================
FROM python:3.11-alpine

# Variables de entorno para runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_ENV=production \
    PORT=5000

WORKDIR /app

# Copiamos solo lo necesario desde el build stage
COPY --from=builder /install /usr/local
COPY app.py .

# Crear un usuario no root
RUN adduser -D appuser
USER appuser

# Exponer el puerto (documentado)
EXPOSE 5000

# HEALTHCHECK (opcional, recomendado)
HEALTHCHECK CMD wget --no-verbose --tries=1 --spider http://localhost:5000/ || exit 1

# Labels de metadata
LABEL maintainer="Alvaro Chambi <alvaro.chambi@hotmail.com>" \
      version="1.0" \
      description="Aplicación Flask con multi-stage Dockerfile"

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
