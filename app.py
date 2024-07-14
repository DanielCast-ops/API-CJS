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

#incertamos las rutas de cargo

# Rutas para Cargo
@app.route('/cargo', methods=['POST'])
def crear_cargo():
    data = request.get_json()
    nuevo_cargo_id = cargo.crear_cargo(data['cargo'])
    return jsonify({'id_cargo': nuevo_cargo_id}), 201

@app.route('/cargo/<int:id_cargo>', methods=['GET'])
def obtener_cargo(id_cargo):
    cargo_obtenido = cargo.obtener_cargo(id_cargo)
    if cargo_obtenido:
        return jsonify(cargo_obtenido)
    return jsonify({'mensaje': 'Cargo no encontrado'}), 404

@app.route('/cargo/<int:id_cargo>', methods=['PUT'])
def actualizar_cargo(id_cargo):
    data = request.get_json()
    cargo.actualizar_cargo(id_cargo, data['cargo'])
    return jsonify({'mensaje': 'Cargo actualizado'}), 200

@app.route('/cargo/<int:id_cargo>', methods=['DELETE'])
def eliminar_cargo(id_cargo):
    cargo.eliminar_cargo(id_cargo)
    return jsonify({'mensaje': 'Cargo eliminado'}), 200

# Similarmente, se crean las rutas para Cliente, Proveedor, Empleado, Articulo, Inventario, Servicio, EstadoServicio

if __name__ == '__main__':
    app.run(debug=True)
