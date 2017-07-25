import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/greeting/', methods=['GET', 'POST', 'DELETE'])
def greeting():
    name = 'Guest'
    if request.method  == 'GET' and os.path.isfile('name.txt'):
        file = open('name.txt', 'r')
        name = file.read()
    elif request.method == 'POST':
        name = post_name(request.form['name'])
    elif request.method == 'DELETE':
        delete_name()
    return 'Hello, {0} \n'.format(name)

def post_name(name):
    file = open('name.txt', 'w')
    file.write(name)
    return name

def delete_name():
    os.remove('name.txt')
