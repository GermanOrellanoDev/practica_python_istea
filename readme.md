# Clima de una ciudad por consola

## Descripción

Este proyecto permite consultar el clima actual de una ciudad desde la consola. El usuario ingresa el nombre de una ciudad y el programa muestra la temperatura, la sensación térmica, la humedad y una descripción de las condiciones meteorológicas.

El proyecto está desarrollado en Python y utiliza un servicio meteorológico en línea para obtener los datos.

## Tecnologías y librerías

- Python 3
- requests: para realizar solicitudes HTTP y obtener los datos del clima.
- colorama: instalada para permitir el uso de colores en la consola.

## Requisitos previos

- Tener Python 3 instalado.
- Tener conexión a Internet.

## Instalación

1. Clonar o descargar este repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Crear un entorno virtual:

   ```bash
   python -m venv .venv
   ```

4. Activar el entorno virtual en Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Instalar las dependencias:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Ejecución

Ejecutar el siguiente comando desde la carpeta del proyecto:

```bash
python main.py
```

Ingresar el nombre de la ciudad cuando el programa lo solicite.

## Integrantes

- Mikhail Acevedo 
- Christopher Perez
- Santiago Cagigas
- Germán Orellano

## Manejo de errores

El programa contempla el manejo de errores relacionados con entradas inválidas, problemas de conexión y respuestas inesperadas del servicio meteorológico.