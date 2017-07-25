from flask import Flask, request
app = Flask(__name__)

@app.route('/greeting/')
def greeting():
  return 'Hello, Guest'
