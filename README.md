# Taller de frontend

Código fuente de partida para el taller de frontend de la asignatura de Diseño y Mantenimiento del Software (Universidad de Burgos, Grado en Ingeniería Informática)

Seguir las instrucciones de la guía del taller disponible en el campus virtual.

## Instalación

Clonar este repositorio en la ruta deseada.

Desde dicha ruta, subdirectorio `backend`, instalar las dependencias con:

```bash
pip3 install -r requirements.txt
```

## Arrancar y parar el servidor

Después de cada cambio, pese a que a menudo se detectarán y recargará automáticamente, será aconsejable reiniciar el servidor.

Para arrancarlo, desde la ruta del backend en el proyecto:

FLASK_APP=app.py flask run

Una vez arrancado, como se indica en las instrucciones que muestra en la salida, puede pararse pulsando Ctrl+C.
