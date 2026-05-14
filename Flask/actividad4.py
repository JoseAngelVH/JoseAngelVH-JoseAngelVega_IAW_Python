from flask import Flask, request

app = Flask(__name__)

# Lista para guardar alumnos
alumnos = []

@app.route("/")
def formulario():
    return """
    <h1>Registro de Alumnos</h1>

    <form action="/guardar">
        <label>Nombre del alumno:</label><br>
        <input type="text" name="nombre"><br><br>

        <label>Nota:</label><br>
        <input type="number" name="nota"><br><br>

        <button type="submit">Guardar</button>
    </form>

    <br>
    <a href="/lista">Ver alumnos</a>
    """

@app.route("/guardar")
def guardar():
    nombre = request.args.get("nombre", "")
    nota = request.args.get("nota", "")

    # Guardar en la lista
    alumnos.append({
        "nombre": nombre,
        "nota": nota
    })

    return f"""
    <h1>Alumno guardado</h1>

    <p>{nombre} - Nota: {nota}</p>

    <a href="/">Agregar otro alumno</a><br><br>
    <a href="/lista">Ver lista de alumnos</a>
    """

@app.route("/lista")
def lista():
    html = "<h1>Lista de alumnos</h1><ul>"

    for alumno in alumnos:
        html += f"<li>{alumno['nombre']} - Nota: {alumno['nota']}</li>"

    html += "</ul><a href='/'>Volver</a>"

    return html

if __name__ == "__main__":
    app.run(debug=True)