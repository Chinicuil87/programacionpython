from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return "Hola desde Flask"