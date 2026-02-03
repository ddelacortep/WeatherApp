# 🌦️ Weather App API - Deploy Automatizado en AWS

Este proyecto es una **API REST** construida con **FastAPI** que proporciona datos climáticos en tiempo real. Lo más destacado es su **arquitectura DevOps**, que permite un ciclo completo de Integración y Despliegue Continuo (CI/CD) desde el código hasta la nube.



## 🚀 Características del Proyecto
* **Backend:** FastAPI (Python 3.11).
* **Contenerización:** Docker para portabilidad total.
* **Seguridad:** Escaneo de vulnerabilidades con **Trivy**.
* **Automatización:** GitHub Actions (CI/CD).
* **Infraestructura:** Desplegado en **AWS EC2 (Ubuntu)**.

---

## 🛠️ Arquitectura y Pipeline CI/CD

El flujo de trabajo automatizado sigue estos pasos tras cada `git push`:

1.  **Construcción:** GitHub Actions crea la imagen de Docker.
2.  **Seguridad:** **Trivy** analiza la imagen. Si detecta fallos críticos, el despliegue se detiene.
3.  **Registro:** La imagen se sube a **Docker Hub**.
4.  **Despliegue (SSH):** GitHub se conecta a mi instancia de AWS, limpia el entorno antiguo (contenedores e imágenes) y levanta la nueva versión automáticamente.

---

## 🌍 Cómo consumir la API

La API está activa y disponible públicamente en AWS. Puedes consultarla directamente o integrarla en cualquier frontend.

**URL Base:** `http://3.237.34.41`

### 1. Consultar el clima de una ciudad
* **Endpoint:** `/clima`
* **Método:** `GET`
* **Parámetros:** `ciudad` (ej: `Madrid`, `Barcelona`, `Tokyo`)
* **Ejemplo:** [http://3.237.34.41/clima?ciudad=Barcelona](http://3.237.34.41/clima?ciudad=Barcelona)

### 2. Formato de Respuesta
```json
{
  "ciudad": "Barcelona",
  "pais": "ES",
  "temperatura": "15°C",
  "descripcion": "nubes dispersas",
  "humedad": "60%",
  "viento": "4.1 m/s",
  "proyecto": "Weather App API - DevOps Portfolio"
}