from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Página Inicial. Vá para <a href="/decorator">/decorator</a> para ver a explicação.'

@app.route('/decorator')
def explicar_decorator():
    explicacao = """
    O que é um Decorator em Python?
    Um <b>decorator</b> é uma função que recebe outra função como argumento e estende o seu comportamento sem modificá-la explicitamente. <br>
    
    Para que serve? <br>
    Eles são usados para "embrulhar" funções e executar códigos antes ou depois da função original, sendo ideais para: <br>
        
            Logs e monitoramento <br>
            Controle de autenticação/permissões <br>
            Cache de dados <br>
        
    

    Como é utilizado no Flask?<br>
    No Flask, o uso mais comum é o <code>@app.route('/')</code>.  <br>
    Neste caso, o decorator registra a função que vem logo abaixo dele como a responsável por lidar com as requisições enviadas para aquele endereço (URL) específico. <br>
    """
    return explicacao

if __name__ == '__main__':
    app.run(debug=True)