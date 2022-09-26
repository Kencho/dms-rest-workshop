# Taller de APIs REST

Código fuente de partida para el taller de APIs REST de la asignatura de Diseño y Mantenimiento del Software (Universidad de Burgos, Grado en Ingeniería Informática)

Seguir las instrucciones de la guía del taller disponible en el campus virtual.

## Instalación

Clonar este repositorio en la ruta deseada.

> **Opcional**: Para realizar estos pasos dentro de un entorno virtual ejecutar desde un terminal:
>
> ```bash
> sudo apt install -y python3-venv # Si venv no está instalado
> python3 -m venv .venv
> source .venv/bin/activate
> ```
>
> El terminal reflejará el cambio precediendo el _prompt_ con el nombre del entorno virtual.
> En VS Code, configurar el intérprete de Python a usar en la opción _"Python: Select interpreter"_ en la paleta de comandos (`Ctrl+Shift+P`) y seleccionando el intérprete del entorno virtual `.venv`.

Desde dicha ruta, subdirectorio `backend`, instalar las dependencias con:

```bash
pip3 install -r requirements.txt
```

## Arrancar y parar el servidor

Después de cada cambio, pese a que a menudo se detectarán y recargará automáticamente, será aconsejable reiniciar el servidor.

Para arrancarlo, desde la ruta del backend en el proyecto:

```bash
FLASK_APP=app.py flask run
```

Una vez arrancado, como se indica en las instrucciones que muestra en la salida, puede pararse pulsando Ctrl+C.

> En VS Code es posible arrancarlo y depurarlo desde el propio IDE creando un fichero `.vscode/launch.json` en el directorio raíz del proyecto:
>
> ```json
> {
>     "version": "0.2.0",
>     "configurations": [
>         {
>             "name": "Backend: Dev",
>             "type": "python",
>             "request": "launch",
>             "module": "flask",
>             "env": {
>                 "FLASK_APP": "backend/app.py",
>                 "FLASK_DEBUG": "1"
>             },
>             "args": [
>                 "run",
>                 "--debugger",
>                 "--reload",
>                 "-p",
>                 "5000"
>             ],
>             "jinja": true,
>             "justMyCode": true
>         },
>         {
>             "name": "Backend: Run",
>             "type": "python",
>             "request": "launch",
>             "module": "flask",
>             "env": {
>                 "FLASK_APP": "backend/app.py",
>                 "FLASK_DEBUG": "0"
>             },
>             "args": [
>                 "run",
>                 "--no-debugger",
>                 "--no-reload",
>                 "-p",
>                 "5000"
>             ],
>             "jinja": true,
>             "justMyCode": true
>         }
>     ]
> }
> ```
