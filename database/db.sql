CREATE DATABASE data_base_invmak;

USE data_base_invmak;

-- TABLA DE CLIENTES
CREATE TABLE clientes(
    id INT(11) NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    tipodi VARCHAR(1) NOT NULL,
    numdi VARCHAR(15) NOT NULL,
    edad INT(3) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    direccion VARCHAR(60) NOT NULL,
    email VARCHAR(40) NOT NULL,
    contrasenia VARCHAR(60) NOT NULL    
);

ALTER TABLE clientes
    ADD PRIMARY KEY (id);

ALTER TABLE clientes
    MODIFY id INT(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

DESCRIBE clientes;

-- TABLA DE PRODUCTOS
CREATE TABLE productos(
    codigo_producto INT(11) NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    caracteristicas TEXT,
    precio FLOAT(12) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    cantidad INT(4) NOT NULL          
);

ALTER TABLE productos
    ADD PRIMARY KEY (codigo_producto);

ALTER TABLE productos
    MODIFY codigo_producto INT(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;
    
DESCRIBE productos;

ALTER TABLE clientes
    ADD producto_cod INT(11) NOT NULL;

ALTER TABLE clientes
    ADD registrado_el timestamp NOT NULL DEFAULT current_timestamp;

ALTER TABLE clientes
    ADD CONSTRAINT fk_producto FOREIGN KEY (producto_cod) REFERENCES productos(codigo_producto);

ALTER TABLE clientes
    MODIFY producto_cod INT(11);    