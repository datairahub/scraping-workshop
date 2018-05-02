# WEB SCRAPING

Taller de extracción automatizada de datos de páginas web

*Web scraping* es una técnica que emplea diferentes tecnologías para extraer datos o información de una página web. Se usa para recoger datos sin estructura y convertirlos en datos estructurados para posteriormente ser tratados en bases de datos u hojas de cálculo. El taller es una aproximación práctica al *scraping* con el objetivo de permitir a los asistentes el tratamiento de información útil para sus propios proyectos.

**I Edición**: 6-7 febrero 2018 [Montera34](https://montera34.com/), [Hirikilabs](http://hirikilabs.tabakalera.eu/), (Tabakalera, San Sebastián). [Enlace a la convocatoria](https://www.tabakalera.eu/es/web-scraping-como-extraer-datos-estructurados-de-una-web)

**II Edición**: 11-12 de mayo de 2018 [Aedi](http://www.aedisevilla.es/), (WorkInCompany, Sevilla). [Enlace a la convocatoria](http://www.aedisevilla.es/events/web-scraping/)

## Estructura

##### I Bloque 
- (1h) Introducción: presentación de la actividad, puesta en contexto y explicación del objetivo del taller.
- (1h) Introducción al scraping: Explicación funcionamiento web (HTML, JSON, APIs...), e introducción de formas de almacenamiento de la información obtenida.
- (2h) Desarrollo scraper: Explicación y puesta en práctica de herramientas iniciales para hacer scraping (postman, python, beautifulsoup, etc)

##### II Bloque
- (3h) Desarrollo scraper: Continuación de la sesión del día anterior.
- (1h) Introducción a técnicas avanzadas de scraping: Ejecución de Javascript, uso de proxies, otras cuestiones surgidas en el desarrollo del taller.

## Requerimientos

- Tener python2 instalado

Los ejercicios están preparados para ejecutarse con Python2, pero con pequeños cambios puede ejecutarse con Python3. Si no lo tienes instalado en tu portátil, te pedimos que lo instales antes del taller para aprovechar mejor el tiempo que estemos juntos. Según el sistema operativo que tengas, puedes seguir una de los siguientes tutoriales:

### Linux

**Instalar python**
- Abre una terminal
- Comprueba si ya tienes instalado python tecleando:
    ```sh
    python -version
    ```
- Si no lo tienes instalado teclea:
    ```sh
    sudo apt-get install python
    ```

**Instalar pip**
- Abre una terminal
- Entra en la consola de python tecleando:
    ```sh
    python
    ```
- Comprueba que tienes pip instalado:
    ```python
    pip import
    ```
- Si no lo tienes, ejecuta:
    ```sh
    sudo apt-get install python-pip
    ```

### Windows

**Instalar python**
- Descarga python pinchando [aqui](https://www.python.org/downloads/release/python-2715/)
- Ejecuta el archivo descargado y sigue las instrucciones.
- Si te da error, intenta seguir este [tutorial](https://www.quora.com/How-do-I-install-Python-in-Windows-8-1)
- Confirmar tecleando en consola CMD:
    ```sh
    python -version
    ```

**Instalar pip**
- Sigue estas [instrucciones](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows#12476379)
- Si te da error, intenta añadir al PATH la localización de pip. Prueba a meter el full path:  `C:\Python27\Scripts\pip`
- Confirmar tecleando en la consola de python:
    ```python
    pip import
    ```

> **Windows Vista**: Para que python funcione en Windows Vista tenemos que añadirlo al “path” de manera que al escribir “python” en la linea de comandos (CMD) lo reconozca. Añadir a PATH significa decirle al ordenador dónde tiene que buscar el progama python.

**Instalar módulos python con pip**
- Teclear:
    ```python
    pip install bs4
    ```
- Si da error, tecleando
    ```cmd
    C:\Python27\Scripts\pip install bs4
    ```

> Windows 10: para instalar un paquete, usar `py -m pip install bs4`

### Mac
**Instalar python**
- Descarga python pinchando en este [enlace](https://www.python.org/ftp/python/3.6.4/python-3.6.4-macosx10.6.pkg)
- Ejecuta el archivo descargado y sigue las instrucciones.

**Instalar módulos python con pip**
- Para instalar librerías o módulos de Python, que añaden funcionalidades adicionales, se puede user pip desde la línea de comandos del sistema operativo, no desde la consola de Python:
    ```sh
    pip install nombre-modulo
    ```

## Recursos de interés

#### Módulos Python que utilizaremos

[Urllib](https://docs.python.org/2/library/urllib.html), [Requests](http://docs.python-requests.org/en/master/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

#### Otras herramientas que utilizaremos

[POSTMAN](https://www.getpostman.com/), [Selenium](http://www.seleniumhq.org/)

#### Introducción a HTML

[Curso HTML básico de Codeacademy](https://www.codecademy.com/courses/web-beginner-en-HZA3b/0/1?curriculum_id=50579fb998b470000202dc8b), [Mensajes HTML](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages), [Tipos de peticiones HTML](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods), [Cabeceras HTML](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)

#### Tutoriales

[How to fake and rotate User Agents using Python 3](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/), [How to Solve Simple Captchas](https://www.scrapehero.com/how-to-solve-simple-captchas-using-python-tesseract/), [Urllib Proxies](https://docs.python.org/3.5/howto/urllib2.html#proxies)

#### Otras herramientas

[Scrapy](https://scrapy.org/), [PhantomJS](http://phantomjs.org/)