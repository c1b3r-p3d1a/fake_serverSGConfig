# fake_serverSGConfig
#### by  &copy;c1b3r-p3d1a

La herramienta que ves arriba está diseñada para facilitarte el proceso de instalación del servidor de Blockdash, Lavaland y Laser Tracer de 32 personas de Stumble Guys. 

Cabe recalcar que el servidor es de backbone-client-api.azurewebsites.net y no mío. Yo solamente he creado una herramienta para facilitar su instalación y su desarrollo normal. Link original de Mediafire [AQUÍ](https://www.mediafire.com/file/7tsmw4wjvm4cafx/StumbleFakeServer.zip/file)

## Programas necesarios

- Python3
- Pip (Python)

## Instalación de la herramienta
Hay dos formas:
- Mediante link directo=> https://github.com/c1b3r-p3d1a/fake_serverSGConfig/archive/refs/heads/main.zip
- Mediante Git=> ```git clone https://github.com/c1b3r-p3d1a/fake_serverSGConfig.git```

### Windows
Cuando la tienes instalada vas a la barra de búsqueda y buscas "CMD" y le das a 'ejecutar como administrador'
<img src=https://github.com/c1b3r-p3d1a/fake_serverSGConfig/blob/main/img/cmd.jpg></img>

Vas al directorio donde tienes la herramienta ```cd C:\Users\tu-usuario\donde-la-tengas\fake_serverSGConfig```
**IMPORTANTE**: Antes de hacer este paso, descomprime la carpeta si lo has descargado mediante link directo.

Cuando estés en la carpeta, escribe ```pip install -r requirements.txt``` para instalar las librerías necesarias.

Cuando lo tengas todo instalado, ya puedes ir al siguiente paso.


## Ejecución de la herramienta

Después de haber hecho todos los pasos anteriores, simplemente escribe en la temrinal ```python fake_serverSGConfig_es_ES.py```
Te saldrá algo como esto:

<img src="https://github.com/c1b3r-p3d1a/fake_serverSGConfig/blob/main/img/inicio.jpg"></img>
<img src="https://github.com/c1b3r-p3d1a/fake_serverSGConfig/blob/main/img/opciones.jpg"></img>

Si es la primera vez que lo ejecutas, pulsa la primera opción y te lo configurará solo.
Cuando tengas instalado el certificado del server, simplemente enciende el servidor con la opción 2 y luego con la opción 4 inicia el juego. 

**IMPORTANTE**: Cuando tengas los esrvidores de Blockdash, etc. solo te saldrán esos torneos. A veces hay que meterse dos veces en la sección de torneos para que "espabile" el servidor. Cuando quieras dejarlo todo normal, simplemente vuelve a ejecutar el programa como **ADMINISTRADOR** y le das a la opción 3. Si tienes dudas sobre el estado de tu servidor, ejecuta la opción 5. También como podréis observar, hay un archivo llamado "status_of_server.txt". Ese archivo no lo modifiquéis por que sino no funcionará la opción 5. Pero por si acaso, he programado un backup que detecta si modificas el archivo y lo deja normal, por si os confundís y lo modificáis.


Y sería eso.
