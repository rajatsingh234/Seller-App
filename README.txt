Seller App

Task:
An action must have start time, end time, start price, item name and finally -
user_id of the user who won the auction

Requirements:
Python 3.6 or later
Django 3.1 or later
SQLite or other supported database

Installation:
Install django:
    python -m pip install django
change directory:
    cd Seller-App
Run Server:
    python manage.py runserver
REST api:
    pip install djangorestframework

Visit http://127.0.0.1:8000/ in your browser to access the app.
Visit http://127.0.0.1:8000/admin (user id=admin password=admin) to check stored data.
Visit http://127.0.0.1:8000/all to check all data.

Features:
This project is made using Python Django framework.
It consists of an app auction.
auction consists a model Auction in auction\models.py that stores the information (tart time, end time, start price, item name and user_id).
To store the information in the db a function create_auction() in auction\views.py is created.
for api and CRUD Operations django REST framework is used and functions are created in auction\views.py