from dotenv import load_dotenv
import os #  permite acceder a funcionalidades dependientes del Sistema Operativo
# os.chdir(nuevo)
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo #, ObjectId
from flask_cors import CORS

from bson import ObjectId
# ObjectId(id) // conversión del id

# para descargar archivos de colab
# from google.colab import files
# files.download(url_de_descarga)

load_dotenv()

print(os.environ.get("USER"))

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get("URI")
mongo = PyMongo(app)

CORS(app)

# Database
db = mongo.db.pythonreact

# Routes
@app.route('/')
def index():
  online_users = mongo.db.users.find({"online": True})
  # print(online_users) # <pymongo.cursor.Cursor object at 0x0000025991CAC920>
  return '<h1>Hola Mundo</h1>'


# db.collection.metod()

# Post
@app.route('/users', methods=['POST']) # ver dato email unico ****
def createUser():
  print(request.json) # configurar headers en postman
  # print(request.json['name'])
  # return 'recivido'
  # # insert_one
  # id = db.users.insert_one({ 

  existe_email = db.users.find_one({'email': request.json['email']})
  # if existe_email == True:
  print(existe_email, '38')

  if existe_email == None:     
    db.users.insert_one({
      'name': request.json['name'],
      'email': request.json['email'],
      'password': request.json['password']
    })
    # print('algo')
    # newObjectId = ObjectId() # "652edc4e8357246c08971190"
    # print(jsonify(str(ObjectId(id))))
    # print(str(ObjectId(id)))
    return jsonify(str(ObjectId())) # "652ee2c38b043dc4de85cc65"
    # return 'recivido'
  else:
    return jsonify({"message": 'ya existe email'})


@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in db.users.find(): # ********************************* conectar servicio MongoDB *********************************
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'email': doc['email'],
            'password': doc['password']
        })
    print('datos enviados OK')
    return jsonify(users)

@app.route('/users/<id>', methods=['GET'])
def getUser(id):
  user = db.users.find_one({'_id': ObjectId(id)})
  print(user)
  return jsonify({
      '_id': str(ObjectId(user['_id'])),
      'name': user['name'],
      'email': user['email'],
      'password': user['password']
  })


@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
  db.users.delete_one({'_id': ObjectId(id)})
  return jsonify({'message': 'User Deleted'})

@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
  print(request.json) # datos recibidos
  db.users.update_one({'_id': ObjectId(id)}, {"$set": {
    'name': request.json['name'],
    'email': request.json['email'],
    'password': request.json['password']
  }})
  return jsonify({'message': 'User Updated'})

# inicializar
if __name__ == "__main__":
    app.run(debug=True)

# python src/app.py