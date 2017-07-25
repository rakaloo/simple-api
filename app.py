from flask import Flask, request
app = Flask(__name__)

@app.route('/greeting/', methods=['GET', 'POST'])
def greeting():
    name = 'Guest'
    if request.method == 'POST':
        name = post_name(request.form['name'])
    return 'Hello, {0} \n'.format(name)

def post_name(name):
    file = open('name.txt', 'w')
    file.write(name)
    return name