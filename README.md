## To Run the Server
Run the following command in your terminal. 
Make sure you are under the project directory ("PictureBook/").
```
python manage.py runserver
```

## Backend Management
- The base of the urls is in "PictureBook/urls.py"
### Django Admin
- Create a superuser by running the following command and follow the instructions.
  ```
  python manage.py createsuperuser
  ```
- Go to http://127.0.0.1:8000/admin and login.
### Library
- "library/urls.py" decides the urls and corresponding views.
- "library/views.py" decides which template to be rendered to and its inputs.

## Frontend Management
- HTML files are under "library/templates/library/"
