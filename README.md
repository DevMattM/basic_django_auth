# Intro

This is a basic example of a Django authentication page.
It uses a the Django form class to create a basic HTML form to collect username and password
and then passes those fields to a template where it is rendered by the server.

In the database are two users, an admin and a regular user.
The admin username is:

    username: bmiteam
    pw: bmitest

The regular user is:

    username: testuser1
     pw: dcba4321

You can create new users either using the Django CLI, or easily through
the admin interface: http://127.0.0.1:8000/admin/

Some URLS that are available in this demo:

http://127.0.0.1:8000/admin/ - admin login, preinstalled with Django

http://127.0.0.1:8000/login/ - basic login form using Django form class

http://127.0.0.1:8000/success/ - a page to indicate a successful login, locked down until signed in

http://127.0.0.1:8000/logout/ - page to logout, preinstalled with Django

# Get Started
To get started, create a virtual environment and install the requirements (from file). In the basic_login base directory with the manage.py file run: 
```CMD
python manage.py runserver
```

From here, you should be able to access the provided links.

# Other
There are only a handful of files that were manually edited, the rest were boilerplate code provided by Django automatically.
Edited files were:
* basic_login/urls.py
* basic_login/settings.py
* basic_login/login/templates/*
* basic_login/login/forms.py
* basic_login/login/views.py