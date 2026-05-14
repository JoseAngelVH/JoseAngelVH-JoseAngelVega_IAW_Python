from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Crear base de datos y tabla
def crear_bd():
    conexion = sqlite3.connect("alumnos.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            nota INTEGER
        )
    """)

    conexion.commit()
    conexion.close()

crear_bd()

@app.route("/")
def inicio():
    return render_template("formulario6.html")

@app.route("/guardar")
def guardar():

    nombre = request.args.get("nombre")
    nota = request.args.get("nota")

    # Guardar en la base de datos
    conexion = sqlite3.connect("alumnos.db")
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO alumnos (nombre, nota) VALUES (?, ?)",
        (nombre, nota)
    )

    conexion.commit()
    conexion.close()

    # Leer alumnos
    conexion = sqlite3.connect("alumnos.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, nota FROM alumnos")
    alumnos = cursor.fetchall()

    conexion.close()

    return render_template("lista6.html", alumnos=alumnos)

if __name__ == "__main__":
    app.run(debug=True)