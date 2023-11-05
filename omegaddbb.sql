create database temporario1;
use temporario1;

CREATE TABLE IF NOT EXISTS  marca(
id_marca INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS  bateria(
id_bateria INT PRIMARY KEY AUTO_INCREMENT,
tipo VARCHAR(10),
capacidad VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS  camara(
id_camara INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS  cliente(
id_cliente INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(20) NOT NULL,
segundo_nombre VARCHAR(20),
apellido VARCHAR(20) NOT NULL,
segundo_apellido VARCHAR(20),
mail VARCHAR(100) NOT NULL UNIQUE,
dni VARCHAR(15) NOT NULL,
direccion VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS  equipo(
id_equipo INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(20),
descripcion TEXT,
marca_id INT NOT NULL,
bateria_id INT NOT NULL,
camara_frontal INT NOT NULL,
camara_trasera INT NOT NULL,
FOREIGN KEY (marca_id) REFERENCES marca(id_marca),
FOREIGN KEY (bateria_id) REFERENCES bateria(id_bateria),
FOREIGN KEY (camara_frontal) REFERENCES camara(id_camara),
FOREIGN KEY (camara_trasera) REFERENCES camara(id_camara)
);

CREATE TABLE IF NOT EXISTS  facturas(
id_factura INT PRIMARY KEY AUTO_INCREMENT,
fecha datetime default current_timestamp,
precio_total DECIMAL(10,2) NOT NULL,
id_cliente int NOT NULL,
FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE IF NOT EXISTS  cuerpo_factura(
id_cuerpo INT PRIMARY KEY AUTO_INCREMENT,
precio_unitario DECIMAL(10,2) NOT NULL,
cantidad int,
id_factura int NOT NULL,
id_equipo int NOT NULL,
FOREIGN KEY (id_factura) REFERENCES facturas(id_factura),
FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo)
);








