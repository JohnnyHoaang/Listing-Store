# python-project2

## Description

This project is a product listing website. The website will provide functionalities to manage user accounts and groups, administration, messaging and displaying a catalog of posts.

## Setup

- Run db-setup.bat to configure the database and set the environment variable DJANGO_PWD=django
- Run setup.bat to create the virtual environment and install the dependencies
- In the command line, type:

```
python manage.py shell
exec(open('web_admin_app/create_groups').read())
exit()
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Go in your browser and type the url:  http://localhost:8000/ to see the website locally

## Link to our GitLab Repo

https://gitlab.com/veronika.pontolillo/python-project2

## Links to Heroku

- Dan: https://dan-python420-product-app.herokuapp.com/
- Johnny:
- Maria:
- Veronika:

## Contributors

Dan Willis Njoumene (2033804)
Johnny
Maria
Veronika
