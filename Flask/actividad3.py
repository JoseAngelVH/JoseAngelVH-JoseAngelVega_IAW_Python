from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def formulario():
    return """
    <h1>Registro de Alumno</h1>

    <form action="/mostrar">
        <label>Nombre del alumno:</label><br>
        <input type="text" name="nombre"><br><br>

        <label>Nota:</label><br>
        <input type="number" name="nota"><br><br>

        <button type="submit">Enviar</button>
    </form>
    """

@app.route("/mostrar")
def mostrar():
    nombre = request.args.get("nombre", "")
    nota = request.args.get("nota", "")

    return f"""
    <h1>Datos del Alumno</h1>

    <p><strong>Nombre:</strong> {nombre}</p>
    <p><strong>Nota:</strong> {nota}</p>

    <a href="/">Volver</a>
    """

if __name__ == "__main__":
    app.run(debug=True)