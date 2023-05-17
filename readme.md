## RIA - Laboratorio 2

### Control de asistencias

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

- **Python**: Python 3.11
- **Django**: Django 4.2

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local:

1. Clona el repositorio del proyecto desde GitHub:
    git clone https://github.com/enzofalcon/RIA_lab2.git
2. Descarga e instala la versión requerida de Python
    https://www.python.org/downloads/
3. Instala el framework Django
    pip install Django==4.2.1
4. Realiza las migraciones de la base de datos:
    python manage.py migrate
5. Crear un superusuario:
    python manage.py createsuperuser
6. Inicia el servidor de desarrollo:
    python manage.py runserver
7. Ingresa desdetu nevagor:
    http://127.0.0.1:8000/admin
8. Ingresa las credenciales del superusuario
9. Crea los grupos:
    Grupo_ESTUDIANTES
    Grupo_DOCENTES
    Grupo_BEDELIAS

## Créditos

Este proyecto fue creado por los siguientes autores principales:

- [Giuliana Ricco 4.717.338-3](giu.ricco@hotmail.com)
- [Francisco Risso 5.286.863-8](frisso2001@gmail.com)
- [Enzo Falcón 3.976.634-4](enalfaga@gmail.com)

Agradecimientos especiales a:
- [Andrés Pastorini](apastorini@gmail.com)

Recursos utilizados en este proyecto:

- [Python](https://www.python.org): Lenguaje de programación utilizado para desarrollar este proyecto.
- [Django](https://www.djangoproject.com): Framework web utilizado para desarrollar este proyecto.
- [Bootstrap](https://getbootstrap.com): Biblioteca de CSS y JS utilizada para el diseño responsivo.

## Licencia

Este proyecto está bajo la [Licencia MIT](https://opensource.org/licenses/MIT).

La Licencia MIT es una licencia de software libre permisiva que permite el uso, modificación y redistribución del código fuente, tanto con fines académicos como comerciales.

### Términos de la Licencia MIT

MIT License

Derechos de autor (c) 2023 Tecnólogo en informática

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), para utilizar el Software sin restricciones, incluyendo, sin limitación, los derechos de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de copias del Software, y para permitir a las personas a las que se les proporcione el Software hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de derechos de autor anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO, PERO NO LIMITADO A, LAS GARANTÍAS DE COMERCIABILIDAD, APTITUD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, QUE SURJA DE, O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS NEGOCIOS EN EL SOFTWARE.