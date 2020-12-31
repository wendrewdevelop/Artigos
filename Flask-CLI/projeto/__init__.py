# flask imports
from flask import Flask


def create_app():
    '''
        Função para criar um aplicativo Flask
    '''

    # Instanciando a o objeto Flask()
    app = Flask(__name__)

    from .settings import bp_settings
    app.register_blueprint(bp_settings)

    # flask custom commands
    with app.app_context():
        from .settings import create_folder_app
        app.cli.add_command(create_folder_app)

    # retornando o objeto app
    return app