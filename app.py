from flask import Flask
from packaging.organizer import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    solver = Organizer()
    solver.solve()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
    solver = Organizer()
    solver.solve()