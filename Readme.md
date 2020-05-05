# Django Example Application

## Install Package
```
pip install -r requirements.txt
```

## Migrate Database
```
py manage.py makemigrations backend
py manage.py migrate
```
### ** Please create database & user before run application **

## Run Application
```
py manage.py runserver
```

## Manage Database via Django Admin (Optional)
```
py manage.py createsuperuser
```
### Input : username, email, password, confirm password
### Login at http://localhost:8000/admin/login