# Simple Flask API #
Returns a greeting of 'Hello, Guest' or 'Hello, {name}' if a name has been posted.  The name persists until it is deleted or overwritten.

# Application Setup #
Install requirements: \n
`$ pip install -r requirements.txt`
Start server: \n
`$ FLASK_APP=app.py flask run`
Ping server: \n
* GET request
`$ curl http://127.0.0.1:5000/greeting/`
* POST request
`curl http://127.0.0.1:5000/greeting/ --data 'name=<insert_name_here>'`>
* DELETE request
`curl http://127.0.0.1:5000/greeting/ -X 'DELETE'`