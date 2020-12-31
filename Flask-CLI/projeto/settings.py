# python imports
import os
import subprocess

# flask imports
import click
from flask import request, Blueprint


# Registrando blueprint
bp_settings = Blueprint('settings', __name__)

@bp_settings.cli.command("startapp")
@click.argument("name")
def create_folder_app(name):
    '''
        Essa função cria uma app dentro
        do projeto, ja com os arquivos
        necessarios para trabalhar.

        Exemplo: flask startapp <nome_da_app>

        Dentro da pasta contém os arquivos: 
            - '__init__.py' -> arquivo __init__.py 
            dentro de um subdiretório será sempre o 
            primeiro a ser executado quando um módulo 
            dentro deste subdiretório for chamado;

            - 'views.py' -> arquivo responsavel por
            conter a logica de cada app;

            - 'models.py' -> arquivo que contém uma classe
            que abstrai em modelo uma tabela do banco de dados;

            - 'forms.py' -> arquivo que pode ser usado
            para abstrair os forms HTML, utilizando a 
            lib Flask-WTForms.

        Foi utilizado a função click do 
        flask, responsável por criar
        comandos e argumentos para a 
        aplicação.
    '''

    # Atribuindo o argumento recebido
    # na variavel "name"
    name=name

    try:
        # Acessando a pasta 'app'
        here = os.path.dirname(os.path.dirname(__file__))
        
        # Setando o caminho e o nome
        # dos arquivos que serão criados
        filepath_init = os.path.join(here, f'{name}', '__init__.py')
        filepath_views = os.path.join(here, f'{name}', 'views.py')
        filepath_models = os.path.join(here, f'{name}', 'models.py')
        filepath_forms = os.path.join(here, f'{name}', 'forms.py')

        # Criando pasta
        os.mkdir(os.path.join(here, f'{name}'))
        try:
            # Criando os arquivos
            f = open(filepath_init, 'w')
            f = open(filepath_views, 'w')
            f = open(filepath_models, 'w')
            f = open(filepath_forms, 'w')

            print('App criada com sucesso')
        except IOError as e:
            print(e)
    except IsADirectoryError as e:
        print(e)