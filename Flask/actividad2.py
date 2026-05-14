from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def formulario():
    return """
    <h1>Sumadora</h1>
    <form action="/sumar">
        <input type="number" name="a" placeholder="Número 1">
        <input type="number" name="b" placeholder="Número 2">
        <button type="submit">Sumar</button>
    </form>
    """

@app.route("/sumar")
def sumar():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    resultado = a + b

    return f"""
    <h1>Resultado</h1>
    <p>{a} + {b} = {resultado}</p>
    <a href="/">Volver</a>
    """

if __name__ == "__main__":
    app.run(debug=True)