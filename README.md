# Preparación de requirements y entorno virtual para el proyecto Django 
![Alt text](doc-img/django.png)

## Crear el entorno virtual

```bash
python3 -m venv .venv
```

## Activar el entorno desde VSCode

![Alt text ](doc-img/image-2.png) ![Alt text](doc-img/image-1.png)
```bash
source .venv/bin/activate
```


![Alt text](doc-img/image.png)
```bash
.\venv\Scripts\activate
```

## Instalación de requierements. Esto instalara django y los paquetes necesarios para ejecutar el proyecto.

```bash
pip3 install -r requirements.txt
```

## Servidor

```bash
python manage.py runserver
```

- Ejecuta el servidor. Para pararlo: control + c (cmd + c en Mac)

- Abrir el navegador y ejecutar el servidor Django en la dirección `127.0.0.1:8000`


## Pagina WEB - funcionalidades

La pagina cuenta con la siguiente estructura:

"HOME" Cuenta con una barra para navegar las distintas secciones. En parte inferiores contamos con botones descriptivos de su funcionalidad.

"CLIENTES" Refleja los clientes dados de alta, cuenta con botones descriptivos segun funcionalidad.

"COMPRAS" Refleja la compras realizadas, cuenta con botones descriptivos segun funcionalidad.

"STOCK" Refleja el stock disponible, cuenta con botones descriptivos segun funcionalidad.

"LOGIN" Inicia sesion, cuenta con botones descriptivos segun funcionalidad.

"ABOUT" Refleja algo de mi

"LOGOUT" Cierra sesion iniciada