

#### Key Features
- 1 . Register
- 2 . Login
- 3 . File Upload
- 4 . Form Validation
- 5 . CRUD Application
- 6 . Ajax CRUD Application
- 7 . File Upload
- 8 . CSV Import
- 9 . CSV Export

# Step for Set Up
``` 
 1. git clone https://github.com/gowthamand/django-crud-ajax-login-register-fileupload

 2. Change settings.py MYSQL CONFIGURATIONS (name, user, password)

 3.  cd django-crud-ajax-login-register-fileupload

 4. pip3 install -r requirements.txt

 5. python3 manage.py migrate

 6. python3 manage.py makemigrations

 7. python3 manage.py migrate

 8. python3 manage.py runserver

 9. Login to http://127.0.0.1:8000

 10. python3 manage.py createsuperuser (enter username, email, password)

```


#MYSQL
sudo apt-get install python-dev python3-dev
sudo apt-get install libmysqlclient-dev
python3 -m pip install PyMySQL
pip install pymysql
pip install mysqlclient
=======================
import pymysql

pymysql.install_as_MySQLdb() = init.py
