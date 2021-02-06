# WEB SCRAPING

Taller de extracción automatizada de datos de páginas web

*Web scraping* es una técnica que emplea diferentes tecnologías para extraer datos o información de una página web. Se usa para recoger datos sin estructura y convertirlos en datos estructurados para posteriormente ser tratados en bases de datos u hojas de cálculo. El taller es una aproximación práctica al *scraping* con el objetivo de permitir a los asistentes el tratamiento de información útil para sus propios proyectos.

#### Ediciones realizadas

**I Edición**: 6-7 febrero 2018, organizado por [Montera34](https://montera34.com/) e [Hirikilabs](http://hirikilabs.tabakalera.eu/) en Tabakalera (Donostia/San Sebastián)
- [Enlace a la convocatoria](https://www.tabakalera.eu/es/web-scraping-como-extraer-datos-estructurados-de-una-web) (Hirikilabs)
- [Enlace a la convocatoria](https://montera34.com/project/liberar-datos-scraping-hirikilabs/) (Montera34)
- [Wiki de la sesión](https://wiki.montera34.com/taller-web-scraping-hirikilabs)
- [Presentación en PDF](https://drive.google.com/file/d/1BIBtPx_3jmzzdteznUkrT53xNYX9e5a9/view?usp=sharing)

**II Edición**: 11-12 de mayo de 2018, organizado por [AEDI](http://www.aedisevilla.es/) en WorkInCompany (Sevilla).
- [Enlace a la convocatoria](http://www.aedisevilla.es/events/web-scraping/)

## Preparación previa

##### Requerimientos
- Tener python instalado

##### Recomendaciones
- Tener instalado algún editor de código (como [VSCode](https://code.visualstudio.com/))

> Los ejercicios están preparados para ejecutarse con Python3, pero con algunos cambios puede ejecutarse con Python2

### Instalación en Windows

##### Instalar python
- Descarga python pinchando [aqui](https://www.python.org/downloads/release/python-2715/)
- Ejecuta el archivo descargado y sigue las instrucciones.
- Si te da error, intenta seguir este [tutorial](https://www.quora.com/How-do-I-install-Python-in-Windows-8-1)
- Confirmar tecleando en consola CMD:
    ```sh
    python -version
    ```

##### Instalar pip
- Sigue estas [instrucciones](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows#12476379)
- Si te da error, intenta añadir al PATH la localización de pip. Prueba a meter el full path:  `C:\Python27\Scripts\pip`
- Confirmar tecleando en la consola de python:
    ```python
    pip import
    ```

> **Windows Vista**: Para que python funcione en Windows Vista tenemos que añadirlo al “path” de manera que al escribir “python” en la linea de comandos (CMD) lo reconozca. Añadir a PATH significa decirle al ordenador dónde tiene que buscar el progama python.

##### Instalar módulos python con pip

- Teclear:
    ```python
    pip install nombre_del_modulo
    ```
- Si da error, tecleando
    ```cmd
    C:\Python27\Scripts\pip install nombre_del_modulo
    ```
    > Windows 10: para instalar un paquete, usar `py -m pip install nombre_del_modulo`

### Instalación en Mac

##### Instalar python
- Descarga python pinchando en este [enlace](https://www.python.org/ftp/python/3.6.4/python-3.6.4-macosx10.6.pkg)
- Ejecuta el archivo descargado y sigue las instrucciones.

##### Instalar módulos python con pip
- Para instalar librerías o módulos de Python, que añaden funcionalidades adicionales, se puede user pip desde la línea de comandos del sistema operativo, no desde la consola de Python:
    ```sh
    pip install nombre-modulo
    ```

### Instalación en Linux

##### Instalar python
- Abre una terminal
- Comprueba si ya tienes instalado python tecleando:
    ```sh
    python -version
    ```
- Si no lo tienes instalado teclea:
    ```sh
    sudo apt-get install python
    ```

##### Instalar pip
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

## Recursos de interés

- Editores de código
    - [VSCode](https://code.visualstudio.com/)
    - [Sublime Text](https://www.sublimetext.com/3)
    - [Atom](https://atom.io/)
    - [Notepad++](https://notepad-plus-plus.org/download/v7.5.6.html)

- Módulos de Python
    - [Urllib](https://docs.python.org/2/library/urllib.html)
    - [Requests](http://docs.python-requests.org/en/master/)
    - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- Otras herramientas
    - [Postman](https://www.getpostman.com/)
    - [Selenium](http://www.seleniumhq.org/)
    - [Scrapy](https://scrapy.org/)
    - [PhantomJS](http://phantomjs.org/)

- Introducción a HTML
    - [Selectores CSS](https://css-tricks.com/how-css-selectors-work/)
    - [Curso HTML básico de Codeacademy](https://www.codecademy.com/courses/web-beginner-en-HZA3b/0/1?curriculum_id=50579fb998b470000202dc8b)
    - [Mensajes HTML](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages)
    - [Tipos de peticiones HTML](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods)
    - [Cabeceras HTML](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)

- Otras guías y tutoriales de interés
    - [How to fake and rotate User Agents using Python 3](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/)
    - [How to Solve Simple Captchas](https://www.scrapehero.com/how-to-solve-simple-captchas-using-python-tesseract/)
    - [Configure Proxies](https://docs.python.org/3.5/howto/urllib2.html#proxies)
