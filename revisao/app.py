import os

from flask import Flask, render_template

from controllers import dashboard_bp, jogador_bp
from dados_jogadores import popular_dados
from models import db, Jogador



def criar_app():
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )

    pasta = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(pasta, "jogadores.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(jogador_bp)

    with app.app_context():
        db.create_all()
        popular_dados()

    return app


app = criar_app()

@app.route("/")
def index():
    jogador = Jogador.listar()
    return render_template("index.html", jogador=jogador,)

if __name__ == "__main__":
    app.run(debug=True)