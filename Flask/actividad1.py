from flask import Flask

app = Flask(__name__)

@app.route("/saludo")
def hola():
    return "Hola, Mundo, Soy José Ángel Vega"

if __name__ == "__main__":
    app.run(debug=True)