import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Logica da tela de cadastro
@bp.route('/register', methods=('GET', 'POST'))
def register():
    # Para metodo POST
    if request.method == 'POST':
        # Variaveis
        username = request.form['usename']
        password = request.form['password']
        db = get_db()
        error = None

        # Validação de campos
        if not username:
            error = 'Preencha o campo de nome de usuário'
        elif not password:
            error = 'Preencha o campo de senha'
        
        # Não havendo erro nos campos
        if error is None:
            try:
                # salva dados no db
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)", 
                    (username,generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Usuário {username} ja cadastrado."
            else:
                # redireciona para tela de login
                return redirect(url_for("auth.login"))
        
        # exibe o erro caso ocorra
        flash(error)

    # renderiza o a pagina encontrada em auth/register.html
    return render_template('auth/register.html')

# Logica para tela de login
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        # variaveis
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?',
            (username,)
        ).fetchone()

        # validação dos dados de login
        if user is None:
            error = 'Nome de usuário invalido'
        elif not check_password_hash(user['passwod'], password):
            error = 'Senha invalida'
        
        # Não havendo erro nos campos
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        # exibe o erro caso ocorra
        flash(error)
    
    # renderiza a pagina encontrada em auth/login
    return render_template('auth/login.html')

# recuperar informações do usuario logado
@bp.before_app_request
def load_logged_in_user():
    # variaveis
    user_id = session.get('user_id')

    # validar usuario logado
    if user_id is None:
        g.user = None
    # busca dados do usuario no db
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE ID = ?',
            (user_id)
        ).fetchone()

# Logica de logout
@bp.rout('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Certificar que tem um usuario logado
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view