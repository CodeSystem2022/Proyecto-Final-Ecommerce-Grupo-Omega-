from flask import Flask ,jsonify ,request
from flask_cors import CORS      
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/Omega_project'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Producto(db.Model):
    __tablename__ = 'equipos'

    id = db.Column(db.Integer,primary_key=True)
    marca = db.Column(db.String(50))
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Float())
    stock = db.Column(db.Integer)
    imagen = db.Column(db.Text())
    imagen2 = db.Column(db.Text())
    imagen3 = db.Column(db.Text())
    caracteristicas = db.Column(db.String(400))
    pantalla = db.Column(db.String(100))
    procesador = db.Column(db.String(100))
    ram = db.Column(db.Integer)
    almacenamiento = db.Column(db.Integer)
    expansion = db.Column(db.String(100))
    camara_frontal = db.Column(db.String(100))
    camara_trasera = db.Column(db.String(100))
    bateria = db.Column(db.Integer)
    sistema = db.Column(db.String(100))
    perfil = db.Column(db.String(100))
    peso = db.Column(db.String(100))
    
    
    def __init__(self,marca,nombre,precio,stock,imagen,imagen2,imagen3,caracteristicas,pantalla,procesador,ram,almacenamiento,expansion,camara_frontal,camara_trasera,bateria,sistema,perfil,peso):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.imagen = imagen
        self.imagen2 = imagen2
        self.imagen3 = imagen3
        self.caracteristicas = caracteristicas
        self.pantalla = pantalla
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.expansion = expansion
        self.camara_frontal = camara_frontal
        self.camara_trasera = camara_trasera
        self.bateria = bateria
        self.sistema = sistema
        self.perfil = perfil
        self.peso = peso

with app.app_context():
    db.create_all()
    
class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','marca','nombre','precio','stock','imagen','imagen2','imagen3','caracteristicas','pantalla','procesador','ram','almacenamiento','expansion','camara_frontal','camara_trasera','bateria','sistema','perfil','peso')


producto_schema=ProductoSchema() # El objeto producto_schema es para traer un producto
productos_schema=ProductoSchema(many=True) # El objeto productos_schema es para traer multiples registros de producto

@app.route('/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    resultado = productos_schema.dump(productos)
    return jsonify(resultado)

@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro

@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto) 

@app.route('/productos', methods=['POST'])
def create_producto():
    marca = request.json['marca']
    nombre = request.json['nombre']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    imagen2 = request.json['imagen2']
    imagen3 = request.json['imagen3']
    caracteristicas = request.json['caracteristicas']
    pantalla = request.json['pantalla']
    procesador = request.json['procesador']
    ram = request.json['ram']
    almacenamiento= request.json['almacenamiento']
    expansion = request.json['expansion']
    camara_frontal = request.json['camara_frontal']
    camara_trasea = request.json['camara_trasera']
    bateria = request.json['bateria']
    sistema = request.json['sistema']
    perfil = request.json['perfil']
    peso = request.json['peso']
    
    nuevo_producto = Producto(marca,nombre, precio, stock, imagen,imagen2,imagen3,caracteristicas,pantalla,procesador,ram,almacenamiento,expansion,camara_frontal,camara_trasea,bateria,sistema,perfil,peso)
    db.session.add(nuevo_producto)
    db.session.commit()
    return producto_schema.jsonify(nuevo_producto)

@app.route('/productos/<id>',methods=['PUT'])
def update_producto(id):
    producto = Producto.query.get(id)
    
    marca = request.json['marca']
    nombre = request.json['nombre']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    imagen2 = request.json['imagen2']
    imagen3 = request.json['imagen3']
    caracteristicas = request.json['caracteristicas']
    pantalla = request.json['pantalla']
    procesador = request.json['procesador']
    ram = request.json['ram']
    almacenamiento= request.json['almacenamiento']
    expansion = request.json['expansion']
    camara_frontal = request.json['camara_frontal']
    camara_trasea = request.json['camara_trasera']
    bateria = request.json['bateria']
    sistema = request.json['sistema']
    perfil = request.json['perfil']
    peso = request.json['peso']
    
    producto.marca = marca
    producto.nombre = nombre
    producto.precio = precio
    producto.stock = stock
    producto.imagen = imagen
    producto.imagen2 = imagen2
    producto.imagen3 = imagen3
    producto.caracteristicas = caracteristicas
    producto.pantalla = pantalla
    producto.procesador = procesador
    producto.ram = ram
    producto.almacenamiento = almacenamiento
    producto.expansion = expansion
    producto.camara_frontal = camara_frontal
    producto.camara_trasera = camara_trasea
    producto.bateria = bateria
    producto.sistema = sistema
    producto.perfil = perfil
    producto.peso = peso
    
    db.session.commit()
    return producto_schema.jsonify(producto)

if __name__ == '__main__':
    app.run(debug=True, port=5000)