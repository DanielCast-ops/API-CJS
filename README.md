Este es un manual basico para el manejo de la api para la empresa CJS Technology

# Requisitos
flask
sqlite3
python3

# Notas

Esta api esta dibidida en 3 archivos principales que gestionan la creacion y el manejo de los datos asi como la expocicion de los mismos. 

Cbase.py se encarga de la creacion de la base de datos en sqlite3
controlador.py se encarga de la gestion de la base de datos utilizando POO
app.py se encarga de la api, sus rutas y expocicion. 

!!!Nota importante!!!
TOMAR EN CUENTA QUE AL MOMENTO SOLO SE CUENTAN CON LAS RUTAS PARA LA TABLA CARGOS
!!Nota importante!!!

por motivos de tiempo, aunque en el codigo del controlador.py se disponen de funciones para el manejo de todas las tablas de la base de datos, al momento de realizar la ultima actulizacion solo se cuentan con las rutas para la tabla de cargos. 

Debido a lo anterior, este manual se enfoca en la tabla de cargos exclusivamente. 


# Manual Básico de la API

### Descripción General
Esta API permite gestionar una tabla de "cargo" con las siguientes operaciones:
- **Crear un cargo** (`POST /cargo`)
- **Obtener un cargo por ID** (`GET /cargo/<id>`)
- **Actualizar un cargo** (`PUT /cargo/<id>`)
- **Eliminar un cargo** (`DELETE /cargo/<id>`)

### Endpoints y Ejemplos

#### 1. Crear un Cargo
- **URL**: `/cargo`
- **Método HTTP**: `POST`
- **Descripción**: Crea un nuevo cargo.
- **Encabezados**: 
  - `Content-Type: application/json`
- **Cuerpo de la Solicitud**:
  ```json
  {
    "cargo": "Nombre del Cargo"
  }
  ```
- **Respuesta Exitosa**:
  - **Código**: `201 CREATED`
  - **Cuerpo**:
    ```json
    {
      "id": 1
    }
    ```

**Ejemplo usando `curl`**:
```sh
curl -X POST http://127.0.0.1:5000/cargo -H "Content-Type: application/json" -d '{"cargo": "XXXXX"}'
```

#### 2. Obtener un Cargo por ID
- **URL**: `/cargo/<id>`
- **Método HTTP**: `GET`
- **Descripción**: Obtiene un cargo por su ID.
- **Parámetros de URL**:
  - `id` (integer): ID del cargo.
- **Respuesta Exitosa**:
  - **Código**: `200 OK`
  - **Cuerpo**:
    ```json
    {
      "id": 1,
      "cargo": "Desarrollador"
    }
    ```
- **Respuesta de Error**:
  - **Código**: `404 NOT FOUND`
  - **Cuerpo**:
    ```json
    {
      "error": "Cargo no encontrado"
    }
    ```

**Ejemplo usando `curl`**:
```sh
curl -X GET http://127.0.0.1:5000/cargo/1
```

#### 3. Actualizar un Cargo
- **URL**: `/cargo/<id>`
- **Método HTTP**: `PUT`
- **Descripción**: Actualiza un cargo existente.
- **Encabezados**: 
  - `Content-Type: application/json`
- **Parámetros de URL**:
  - `id` (integer): ID del cargo.
- **Cuerpo de la Solicitud**:
  ```json
  {
    "cargo": "Nombre Actualizado del Cargo"
  }
  ```
- **Respuesta Exitosa**:
  - **Código**: `200 OK`
  - **Cuerpo**:
    ```json
    {
      "id": 1,
      "cargo": "Nombre Actualizado del Cargo"
    }
    ```
- **Respuesta de Error**:
  - **Código**: `404 NOT FOUND`
  - **Cuerpo**:
    ```json
    {
      "error": "Cargo no encontrado"
    }
    ```

**Ejemplo usando `curl`**:
```sh
curl -X PUT http://127.0.0.1:5000/cargo/1 -H "Content-Type: application/json" -d '{"cargo": "Senior Developer"}'
```

#### 4. Eliminar un Cargo
- **URL**: `/cargo/<id>`
- **Método HTTP**: `DELETE`
- **Descripción**: Elimina un cargo existente.
- **Parámetros de URL**:
  - `id` (integer): ID del cargo.
- **Respuesta Exitosa**:
  - **Código**: `200 OK`
  - **Cuerpo**:
    ```json
    {
      "mensaje": "Cargo eliminado"
    }
    ```
- **Respuesta de Error**:
  - **Código**: `404 NOT FOUND`
  - **Cuerpo**:
    ```json
    {
      "error": "Cargo no encontrado"
    }
    ```

**Ejemplo usando `curl`**:
```sh
curl -X DELETE http://127.0.0.1:5000/cargo/1
```

### Configuración y Ejecución del Servidor Flask

1. **Instalación de Dependencias**:
   - Asegúrate de tener `Flask` y `sqlite3` instalados en tu entorno de Python.
   - Puedes instalarlos con el siguiente comando:
     ```sh
     pip install Flask sqlite3
     ```

2. **Ejecución del Servidor**:
   - Navega hasta el directorio donde se encuentra tu archivo `app.py`.
   - Ejecuta el servidor Flask con el siguiente comando:
     ```sh
     python app.py
     ```

   - El servidor estará disponible en `http://127.0.0.1:5000`.

### Código de la API

A continuación se muestra el código completo de la API hasta el momento, se pueden consultar los archivos, controlador.py y cbase.py para mas informacion del codigo:

```python
# app.py

from flask import Flask, request, jsonify
from controlador import Cargo

app = Flask(__name__)
cargo = Cargo('mi_base_de_datos.db')

@app.route('/cargos/<int:id>', methods=['GET'])
def obtener_cargo(id):
    resultado = cargo.obtener_cargo(id)
    if resultado:
        return jsonify(resultado)
    else:
        return jsonify({"error": "Cargo no encontrado"}), 404

@app.route('/cargos', methods=['POST'])
def crear_cargo():
    data = request.get_json()
    nuevo_cargo_id = cargo.crear_cargo(data['cargo'])
    return jsonify({"id": nuevo_cargo_id}), 201

@app.route('/cargos/<int:id>', methods=['PUT'])
def actualizar_cargo(id):
    data = request.get_json()
    cargo_actualizado = cargo.actualizar_cargo(id, data['cargo'])
    if cargo_actualizado:
        return jsonify({"id": id, "cargo": data['cargo']})
    else:
        return jsonify({"error": "Cargo no encontrado"}), 404

@app.route('/cargos/<int:id>', methods=['DELETE'])
def eliminar_cargo(id):
    cargo_eliminado = cargo.eliminar_cargo(id)
    if cargo_eliminado:
        return jsonify({"mensaje": "Cargo eliminado"})
    else:
        return jsonify({"error": "Cargo no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

Este manual te proporcionará una guía básica para interactuar con tu API de Flask y realizar las operaciones CRUD en la tabla de "cargo". Si necesitas más detalles o alguna otra funcionalidad, no dudes en pedírmelo.
