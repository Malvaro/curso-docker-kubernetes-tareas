from flask import Flask, jsonify
import os

app = Flask(__name__)

# Endpoint 1: raíz
@app.route('/')
def home():
    return jsonify({"mensaje": "Docker - Bienvenido Endpoint 1: Saludo General"}), 200

# Endpoint 2: saludo con nombre
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return jsonify({"saludo": f"Hola, {nombre}! (Docker - Endpoint 2: Saludo personalizado)"}), 200

if __name__ == '__main__':
    # Puerto configurable (por defecto 5000)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
