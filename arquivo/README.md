# Tutorial Flaskk

Este Projeto acadêmico visa a criação de um aplicativo de blog básico chamado Flaskr. Os usuários poderão se registrar, fazer login, criar postagens e editar ou excluir suas próprias postagens.

## captura de tela da página inicial

<div align="center">
    <img src="Img/flaskr_index.jpg"></br>
</div>

Presume-se que você já esteja familiarizado com Python. O tutorial oficial na documentação do Python é uma ótima maneira de aprender ou revisar primeiro.


Este Projeto segue o que consta no tutorial disponível no site do prório Flask, porém planeja-se um upgrade do projeto para o futuro, com uma estilizaçao de paginas mais elaborada.

.. _tutorial: https://flask.palletsprojects.com/tutorial/

## captura de tela da página de login


<div align="center">
    <img src="Img/flaskr_login.jpg"></br>
</div>


## captura de tela da página de edição

<div align="center">
    <img src="Img/flaskr_edit.jpg"></br>
</div>

-------
# Instalação

**Certifique-se de usar a mesma versão do código que a versão dos documentos que você está lendo.** Você provavelmente deseja a versão mais recente com tags, mas a versão padrão do Git é o branch principal. ::

    # clone the repository
    $ git clone https://github.com/pallets/flask
    $ cd flask
    # checkout the correct version
    $ git tag  # shows the tagged versions
    $ git checkout latest-tag-found-above
    $ cd examples/tutorial

Crie uma virtualenv e activate ::

    $ python3 -m venv .venv
    $ . .venv/bin/activate

Ou no Windows cmd::

    $ py -3 -m venv .venv
    $ .venv\Scripts\activate.bat

Instale o Flaskr::

    $ pip install -e .

Ou se você estiver usando o branch principal, instale o Flask a partir do código-fonte antes de instalar o Flaskr ::

    $ pip install -e ../..
    $ pip install -e .


Execute
---

.. code-block:: text

    $ flask --app flaskr init-db
    $ flask --app flaskr run --debug

Open http://127.0.0.1:5000 in a browser.


Teste ::
----


    $ pip install '.[test]'
    $ pytest

Execute com coverage report ::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser


