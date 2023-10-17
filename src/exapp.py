from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreact'
mongo = PyMongo(app)

CORS(app)

# Database
db = mongo.db.pythonreact

# Routes
@app.route('/')
def index():
  return '<h1>Hola Mundo</h1>'

# inicializar
if __name__ == "__main__":
    app.run(debug=True)