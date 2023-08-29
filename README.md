# Django REST Framework Complete Authentication API with Simple JWT
## To Run this Project follow below:

1. Create a virtual environment:
```
# On Windows
python -m venv env
env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate
```

```
pip install djangorestframework
```
Add 'rest_framework' to your INSTALLED_APPS setting.
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
2 Set up the database:
```
python manage.py migrate
```
3. Create a superuser (admin) account:
```
python manage.py createsuperuser
```
4. Run the development server:
```
python manage.py runserver
```
5. Access the application:
Open your web browser and go to http://localhost:8000/ to access the project.
