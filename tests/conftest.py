'''
    Configurações pra execução dos testes
'''

import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    '''
        Redireciona temporariamente o banco de dados para o teste
        Cria as tabelas e insere os dados para o teste
        Terminado o teste fecha e remove o direcionamento para o teste
    '''
    db_fd, db_path = tempfile.mkstemp() 
    app = create_app({
        'TESTING':True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    '''
        Permite a execução do teste sem executar o servidor
    '''
    return app.test_client()

@pytest.fixture
def runner(app):
    '''
        Permite executar os comando registrados no app
    '''
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client) -> None:
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username':username, 'password':password}
        )
    
    def logout(self):
        return self._client.get('/auth/logout')
    
@pytest.fixture
def auth(client):
    return AuthActions(client)
