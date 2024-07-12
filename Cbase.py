#!/usr/bin/env python3

#importamos libreria
import sqlite3

#Creamos y conectamos la base de datos.

def coneccion(base):
    con = sqlite3.connect(base)
    #Cremos el cursor
    cursor = con.cursor()
    #cerrar la coneccion

#creamos las tablas
def crear_tablas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cargos (
            id_cargo INT PRIMARY KEY auto_increment NOT NULL,
            cargo varchar (20) not null
        );

        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            nombre VARCHAR(50) NOT NULL,
            telefono VARCHAR(15) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS proveedores (
            id_proveedor INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            nombre VARCHAR(50) NOT NULL,
            telefono VARCHAR(15) NOT NULL,
            tipo_de_productos VARCHAR(100)
        );

        CREATE TABLE IF NOT EXISTS empleados (
            id_personal INT PRIMARY KEY NOT NULL,
            nombre VARCHAR(50) NOT NULL,
            id_cargo INT NOT NULL,
            telefono VARCHAR(15) NOT NULL,
            FOREIGN KEY (id_cargo) REFERENCES cargos(id_cargo)
        );
        CREATE TABLE IF NOT EXISTS articulos (
            id_articulo INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            nombre VARCHAR (50) NOT NULL,
            especificacion VARCHAR (200),
            id_proveedor INT NOT NULL,
            FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor)
        );

        CREATE TABLE IF NOT EXISTS inventario (
            id_transaccion INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            id_articulo INT NOT NULL,
            id_personal INT NOT NULL,
            cantidad INT NOT NULL,
            fecha DATE NOT NULL,
            notas VARCHAR (200),
            FOREIGN KEY (id_articulo) REFERENCES articulos(id_articulo),
            FOREIGN KEY (id_personal) REFERENCES empleados(id_personal)
        );

        CREATE TABLE IF NOT EXISTS servicios (
            id_servicio INT PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            fecha DATE NOT NULL,
            telefono_extra VARCHAR (45),
            cliente_id INT NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id_cliente),
            id_personal INT NOT NULL,
            FOREIGN KEY (id_personal) REFERENCES empleados(id_personal)
        );

        CREATE TABLE estado_servicio (
            id_estado INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            descripcion VARCHAR(50) NOT NULL
        );
        ''')

    conn.commit()

    Print("Se han creado las tablas")

conneccion()
crear tablas()
con.close()




