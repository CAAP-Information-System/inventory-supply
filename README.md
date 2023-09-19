# Inventory Supply Management System

## Getting Started
The Inventory Management System (IMS) is a practical data management application which provides the elements of every data input to  overlook throughout the process and this can be used to easily track the procurement of the supplies for the agency. The inventory system is developed for a faster way of recording the data to the system.

# Technical Usage
## Framework
![Django](https://static.djangoproject.com/img/logos/django-logo-negative.1d528e2cb5fb.png)
The system uses a basic Django-Python web application framework which enables a faster and eaiser data manipulation for the end users. The system also implements REST APIs (*under development*) which will soon use as a optimizable API for bigger use of data in the future.
<br>
>Installed applications used for the system development

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventorySupplyApp',
    'rest_framework',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_filters',
]
```


## Database
Using MySQL as simpler and easier way to manipulate data.

DATABASE_URL:
```
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'inventorysupply_db',  
        'USER': 'root',  
        'PASSWORD': '',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}  
```

