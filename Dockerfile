# Etapa 1: Constructor (Builder)
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
# Instalamos dependencias en una carpeta temporal
RUN pip install --user --no-cache-dir -r requirements.txt

# Etapa 2: Ejecución (Runtime) - La imagen final será mínima
FROM python:3.11-slim-bookworm
WORKDIR /app

# Copiamos solo lo necesario desde el builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Aseguramos que los binarios de Python sean visibles
ENV PATH=/root/.local/bin:$PATH
ENV API_KEY=""

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]