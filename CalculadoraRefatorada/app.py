from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        return calcular()
    return render_template('calculadora.html' ,etapas="",resultados="")




if __name__ == '__main__':
    # Ativa o modo de depuração para atualizar o código automaticamente
    app.run(debug=True)
