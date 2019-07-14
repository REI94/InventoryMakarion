# MakarionWeb
Plataforma de ventas online Makarion

MakarionWeb es un proyecto diseñado como una tienda de ventas online, que le permite a las empresas hacer mayor publicidad
de sus productos y servicios, obteniendo de esta manera nuevos clientes potenciales y realizar ventas virtuales,
sin la necesidad de que exista contacto presencial entre los clientes y las empresas.

## Para poder ejecutar el proyecto debe tener instalado:

python==3.7 o superior
Django==2.2.2
django-annoying==0.10.4
django-crispy-forms==1.7.2
Pillow==6.1.0
psycopg2==2.8.3
pytz==2019.1
sqlparse==0.3.0

Y usar PostgreSQL como gestor de base de datos, aunque pueden usarse otros gestores modificando MakarionWeb/settings.py
en el apartado DATABASES (con cualquier base de datos necesita especificar la contraseña en este apartado y si gusta cambiar
el nombre de la base de datos).

Una vez tenga instalados los programas indicados y configurado el apartado DATABASES, puede ejecutar el proyecto ubicándose
con una terminal en el directorio principal (donde se encuentra el archivo manage.py) y ejecutar el comando:

python manage.py runserver

Y con su navegador web preferido, visitar la dirección:

http://127.0.0.1:8000/
