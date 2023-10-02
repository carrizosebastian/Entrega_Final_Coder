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

**http://localhost:8000/** - El link "home" cuenta con una barra para navegar las distintas secciones. En parte inferiores contamos con botones descriptivos de su funcionalidad.

**http://localhost:8000/cliente** - El link "CLIENTES" refleja los clientes dados de alta, cuenta con botones descriptivos segun funcionalidad.

**http://localhost:8000/compras** - El link "COMPRAS" refleja la compras realizadas, cuenta con botones descriptivos segun funcionalidad.

**http://localhost:8000/stock** - El link "STOCK" refleja el stock disponible, cuenta con botones descriptivos segun funcionalidad.

**http://127.0.0.1:8000/about/** - El link "ABOUT" refleja mi nombre#   p r e _ e n t r e g a _ 3  
 