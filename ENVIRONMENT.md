# Configuración de Base de Datos PostgreSQL
DB_NAME=phonexa_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

# Configuración de Django
SECRET_KEY=tu_clave_secreta_mas_segura_aqui
DEBUG=True

#INSTALACIÓN
pip install -r requirements.txt

#EJECUTAR MIGRACIONES
python manage.py makemigrations
python manage.py migrate

#EJECUTAR 
python manage.py runserver