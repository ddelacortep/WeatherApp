# 🌦️ Weather API Containerized

[![CI Pipeline](https://github.com/ddelacortep/WeatherApp/actions/workflows/main_clima.yml/badge.svg)](https://github.com/ddelacortep/WeatherApp/actions)
![Docker Image Size](https://img.shields.io/docker/image-size/ddelacortep/weather-app/latest)
![Docker Pulls](https://img.shields.io/docker/pulls/ddelacortep/weather-app)

Este proyecto es una **API de Clima** robusta construida con **FastAPI**. No es solo una aplicación, sino una demostración de un ciclo completo de **Software Delivery** utilizando prácticas modernas de **DevOps** y **Seguridad (DevSecOps)**.



## 🎯 Objetivos del Proyecto
* **Contenerización Avanzada:** Uso de Docker con *Multi-stage builds* para reducir la superficie de ataque y el tamaño de la imagen final.
* **Automatización CI/CD:** Pipeline automatizado íntegramente en GitHub Actions.
* **Seguridad Integrada:** Escaneo de vulnerabilidades en tiempo real con **Trivy** antes de cada despliegue.
* **Infraestructura como Código:** Configuración preparada para ser desplegada en entornos productivos como AWS (ECS/App Runner).

---

## 🚀 Instalación y Uso Rápido

No necesitas configurar Python ni instalar dependencias. Puedes ejecutar la API directamente desde la imagen pública en Docker Hub:

```bash
docker run -d \
  -p 8080:8000 \
  --name weather-service \
  -e API_KEY="tu_clave_de_openweather" \
  ddelacortep/weather-app:latest
