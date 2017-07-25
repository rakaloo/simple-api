# Simple Flask API #
Returns a greeting of 'Hello, Guest' or 'Hello, <name>' if a name has been provided via a POST request.  The name persists until it is deleted or overwritten.

# Application Setup #
Install requirements:
`$ pip install -r requirements.txt`
Start server:
`$ FLASK_APP=app.py flask run`
Ping server:
* GET request
`$ curl http://127.0.0.1:5000/greeting/`
* POST request
`curl http://127.0.0.1:5000/greeting/ --data 'name=<insert_name_here>'`>
* DELETE request
`curl http://127.0.0.1:5000/greeting/ -X 'DELETE'`