
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
# Instalamos dependencias en una carpeta temporal
RUN pip install --user --no-cache-dir -r requirements.txt


FROM python:3.11-slim-bookworm
WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV API_KEY=""

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]