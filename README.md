# API Yatube

### Description
This API was created for my Yatube social network project. It implements a registration system using a token. Only the author or administrator can create and edit posts. <br>

***With it you can:***
- Create new posts
- Write comments
- Create thematic groups
- Subscribe to authors

### Technologies

- Python 3.7
- Django 2.2.6
- Django REST Framework
- Simple JWT
- ReDoc

### Quick start

1. Install and activate the virtual environment
2. Install all packages from [requirements.txt](https://github.com/nick-rebrik/Yatube/blob/master/requirements.txt)<br>
  ```pip install -r requirements.txt```
3. Run in command line:<br>
  ```python manage.py collectstatic```<br>
  ```python manage.py makemigrations```<br>
  ```python manage.py migrate```<br>
  ```python manage.py runserver```
 4. Get your [token](http://127.0.0.1:8000/api/v1/token/) and start using API:<br>
   ```http://127.0.0.1:8000/api/v1/token/```
   
### API URLs

- ```http://127.0.0.1:8000/api/v1/redoc/``` - ReDoc page
- ```http://127.0.0.1:8000/api/v1/token/``` - Get token
- ```http://127.0.0.1:8000/api/v1/token/refresh/``` - Refresh token
- ```http://127.0.0.1:8000/api/v1/posts/<id>/``` - Post page 
- ```http://127.0.0.1:8000/api/v1/posts/<id>/comments``` - Leave a comment on the post
- ```http://127.0.0.1:8000/api/v1/group/``` - Create a group
- ```http://127.0.0.1:8000/api/v1/follow/``` - Subscribe to user
