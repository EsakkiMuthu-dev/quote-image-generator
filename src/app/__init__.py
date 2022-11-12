from flask import Flask
from src.app.routes import Routes

class Web():

    def __init__(self) -> None:
        self.app = Flask(__name__)

    def start(self) -> None:
        Routes(self.app)
        
        self.app.run(debug=True)

    def flask_app(self):
        return self.app