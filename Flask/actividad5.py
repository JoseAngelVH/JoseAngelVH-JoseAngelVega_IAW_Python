from flask import Flask, render_template, request

app = Flask(__name__)

alumnos = []

@app.route("/")
def inicio():
    return render_template("formulario.html")

@app.route("/guardar")
def guardar():
    nombre = request.args.get("nombre")
    nota = request.args.get("nota")

    alumnos.append({
        "nombre": nombre,
        "nota": nota
    })

    return render_template("lista.html", alumnos=alumnos)

if __name__ == "__main__":
    app.run(debug=True)