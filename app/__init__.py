from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Import blueprints or routes here, if any
from app import routes  # Example import

if __name__ == '__main__':
    app.run(debug=True)