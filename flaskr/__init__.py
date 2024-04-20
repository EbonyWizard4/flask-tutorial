import os
from flask import Flask

def create_app(test_config=None):
    # Cria e configura o aplicativo
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KET='dev', DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),)

    if test_config is None:
        # Carrega a configuração da instância, se existir, quando não estiver testando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carrega a configuração do teste se aprovado
        app.config.from_mapping(test_config)

    # Garantir que a pasta da instancia existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Uma pagina simples que diz hello!
    @app.route('/hello')
    def hello():
        return 'Hello, World! Im learn flask!'
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
