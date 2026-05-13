from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    explicacao = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - [Seu Nome]</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .header {
            text-align: center;
        }
        .contact-info {
            font-style: normal;
            margin-bottom: 20px;
        }
        .section {
            margin-bottom: 20px;
        }
        .item {
            margin-bottom: 15px;
        }
        .item-title {
            font-weight: bold;
        }
        .item-subtitle {
            color: #7f8c8d;
            font-style: italic;
        }
        ul {
            margin-top: 5px;
        }
    </style>
</head>
<body>

    <header class="header">
        <h1>[Seu Nome Completo]</h1>
        <address class="contact-info">
            Telefone: (00) 99999-9999 | 
            E-mail: [seu.email@exemplo.com]<br>
            Cidade - Estado
        </address>
    </header>

    <section class="section">
        <h2>Experiência de Trabalho</h2>
        
        <div class="item">
            <div class="item-title">[Cargo] - [Nome da Empresa]</div>
            <div class="item-subtitle">[Mês/Ano Início] – [Mês/Ano Fim ou Atual]</div>
            <ul>
                <li>Responsável por [descrição de atividade].</li>
                <li>Conquista: [resultado alcançado].</li>
            </ul>
        </div>

        <div class="item">
            <div class="item-title">[Cargo Anterior] - [Nome da Empresa]</div>
            <div class="item-subtitle">[Mês/Ano Início] – [Mês/Ano Fim]</div>
            <ul>
                <li>Execução de [descrição de atividade].</li>
            </ul>
        </div>
    </section>

    <section class="section">
        <h2>Escolaridade</h2>
        <div class="item">
            <div class="item-title">[Nome do Curso/Graduação]</div>
            <div class="item-subtitle">[Nome da Instituição] - [Ano de Conclusão]</div>
        </div>
        <div class="item">
            <div class="item-title">[Ensino Médio ou outra formação]</div>
            <div class="item-subtitle">[Nome da Instituição] - [Ano de Conclusão]</div>
        </div>
    </section>

    <section class="section">
        <h2>Cursos e Certificações</h2>
        <ul>
            <li>[Nome do Curso] - [Instituição] ([Ano])</li>
            <li>[Nome do Curso] - [Instituição] ([Ano])</li>
        </ul>
    </section>

    <section class="section">
        <h2>Idiomas</h2>
        <ul>
            <li><strong>Inglês:</strong> [Nível: ex: Fluente, Avançado, Intermediário, Básico]</li>
            <li><strong>Espanhol:</strong> [Nível: ex: Fluente, Avançado, Intermediário, Básico]</li>
        </ul>
    </section>

</body>
</html>


    """
    return explicacao


if __name__ == "__main__":
    app.run(debug=True)
