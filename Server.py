from flask import Flask

app = Flask(__name__)

alunos = []

from Routes import *

from ErroHandlers import *


if __name__ == "__main__":
    app.run(port=5000)