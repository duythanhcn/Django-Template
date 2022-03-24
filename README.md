1. Install python 3
2. Install virtual environment
```
python3 -m pip install --user virtualenv
python3 -m virtualenv --help
```
3. Create Project folder
4. Creates virtual enviroment named venv
```
virtualenv --python=python3 venv
python3 -m venv venv
```
5. Activate the virtual enviroment named venv
Must run before all action
```
source venv/bin/activate
```
6. Install packages
```
pip3 install -r requirements.txt
```
Update dependences
```
pip3 freeze > requirements.txt
```
OR
```
pip3 install Django
pip3 install djangorestframework
pip3 install psycopg2 #OR# pip3 install psycopg2-binary
pip3 install django-environ
pip3 install -U drf-yasg
pip3 install packaging
pip3 install djangorestframework-camel-case
```
7. Create Django Project
```
django-admin.py startproject project_name .
```
8. Create Application
```
django-admin.py startapp app_name
python3 manage.py createsuperuser --email admin@example.com --username admin
```
9. Migration
```
python3 manage.py makemigrations app_name
python3 manage.py migrate app_name --database=default
```
10. Start server
```
cp env/.env.development DjangoProject/.env
python3 manage.py runserver 0:80
```
11. Start PostGres
```
pg_ctl -D /usr/local/var/postgres start
pg_ctl -D /usr/local/var/postgres stop
```
12. Enable PostGIS
```
CREATE EXTENSION postgis;
SELECT PostGIS_Version();
```