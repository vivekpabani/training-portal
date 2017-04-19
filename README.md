# training-portal
A web based training portal for various topics

### Instructions

Run following commands to build and run application on localhost and test.
``` bash
$ git clone https://github.com/vivekpabani/training-portal.git
$ cd training-portal
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

This will start development server at http://127.0.0.1:8000/ .
