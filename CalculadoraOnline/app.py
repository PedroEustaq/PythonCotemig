from flask import Flask, render_template
from calculadora import calcular

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('calculadora.html', etapas = '', resultados = '')



@app.route("/calcular", methods=['POST'])
def calcular_route():
    return calcular()



if __name__ == '__main__':
    # Ativa o modo de depuração para atualizar o código automaticamente
    app.run(debug=True)
