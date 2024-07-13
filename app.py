#!/usr/bin/env python3
from Cbase import crear_base
from flask import Flask, jsonify, request
from controlador import Cargo, Cliente, Proveedor, Empleado, Articulo, Inventario, Servicio, EstadoServicio

app = Flask(__name__)

base = 'CJS.db'

# instamciamos las clases del controlador
cargo = Cargo(base)
cliente = Cliente(base)
proveedor = Proveedor(base)
empleado = Empleado(base)
articulo = Articulo(base)
inventario = Inventario(base)
servicio = Servicio(base)
estado_servicio = EstadoServicio(base)



#utilizamos la funcion de Cbase para inicializar la base de datos.

crear_base(base)

