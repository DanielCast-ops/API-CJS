#!/usr/bin/env python3

#importamos librerias

import sqlite3

#creamos la clase que contrlara la  base de datos utilizando POO

class base_de_datos:
    def __init__(self, nombredb)
    self.nombredb = nombredb
    self.conexion = sqlite3.connect(nombre.db)
    self.cursor = self.conexion.cursor()

    #realizamos funcion que nos permita gestionar las consultas.

    def realizar_consulta(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        return self.cursor.fechall()

    #realizamos funcion que nos permita ajecutar diferentes sentencias (incert, delete, update etc.)

    def realizar_sentencia(self, sentencia, parametros=()):
        self.cursor.execute(sentencia,parametros)
        self.conexion.commit()
        return self.cursor.lastrowid

    #creamos funcion que cierre la coneccion

    def cerrar_conexion(self):
        self.conexion.close()

#creamos cada una de las clases que se encargara de manejar las tablas de la bd.

class Cargo:
    def __init__(self, nombre_db):
        self.base_de_datos = BaseDeDatos(nombre_db)

    def crear_cargo(self, cargo):
        consulta = 'INSERT INTO cargos (cargo) VALUES (?)'
        return self.base_de_datos.ejecutar_sentencia(consulta, (cargo,))

    def obtener_cargo(self, id_cargo):
        consulta = 'SELECT * FROM cargos WHERE id_cargo = ?'
        resultado = self.base_de_datos.ejecutar_consulta(consulta, (id_cargo,))
        if resultado:
            return {'id_cargo': resultado[0][0], 'cargo': resultado[0][1]}
        else:
            return None

        #pendiente adicionar las funciones para actualizar y eliminar
