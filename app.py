from asgiref.wsgi import WsgiToAsgi
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name = name)


asgi_app = WsgiToAsgi(app)