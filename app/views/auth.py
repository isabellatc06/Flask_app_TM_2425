from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db, close_db
import os
from functools import wraps


# Création d'un blueprint contenant les routes ayant le préfixe /auth/...
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


def admin_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None or g.user['role'] != 'admin':

            flash("Accès réservé aux administrateurs.", "error")
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@auth_bp.route("/check_login")
def check_login():
    if "user" in session:
        return redirect(url_for("user.show_profile"))  
    else:
        return redirect(url_for("auth.login")) 
        

# Route d'administration
@auth_bp.route('/admin')
@admin_required
def admin():
    return render_template('auth/admin2.html')


# Route /auth/register
@auth_bp.route('/register', methods=('GET', 'POST'))
def register():

    # Si des données de formulaire sont envoyées vers la route /register (ce qui est le cas lorsque le formulaire d'inscription est envoyé)
    if request.method == 'POST':

        # On récupère les champs 'username' et 'password' de la requête HTTP
        username = request.form['username']
        password = request.form['password']
        rue = request.form['rue']
        no_rue = request.form['no_rue']
        code_postal = request.form['code_postal']
        ville = request.form['ville']

        # On récupère la base de donnée
        db = get_db()

        # Si le nom d'utilisateur et le mot de passe ont bien une valeur
        # on essaie d'insérer l'utilisateur dans la base de données
        if username and password and rue and no_rue and code_postal and ville:
            try:
                db.execute("INSERT INTO users (username, password, rue, no_rue, code_postal, ville) VALUES (?, ?, ?, ?, ?, ?)",(username, generate_password_hash(password), rue, no_rue, code_postal, ville))
                # db.commit() permet de valider une modification de la base de données
                db.commit()
                # On ferme la connexion à la base de données pour éviter les fuites de mémoire
                close_db()
                
            except db.IntegrityError:

                # La fonction flash dans Flask est utilisée pour stocker un message dans la session de l'utilisateur
                # dans le but de l'afficher ultérieurement, généralement sur la page suivante après une redirection
                error = f"Utilisateur {username} déjà enregistré."
                flash(error)
                return redirect(url_for("auth.register"))
            
            return redirect(url_for("user.show_profile"))
         
        else:
            error = "Nom d'utilisateur ou mot de passe invalide"
            flash(error)
            return redirect(url_for("auth.login"))
    else:
        # Si aucune donnée de formulaire n'est envoyée, on affiche le formulaire d'inscription
        return render_template('auth/register.html')

# Route /auth/login
@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        close_db()

        error = None
        if user is None:
            error = "Nom d'utilisateur incorrect"
        elif not check_password_hash(user['password'], password):
            error = "Mot de passe incorrect"

        if error is None:
            
            session['user_id'] = user['id_users']
            print("Utilisateur connecté, ID :", session['user_id']) 
            

            # Redirige les admins vers l'espace admin
            if user['role'] == 'admin':
                return redirect(url_for('auth.admin'))
            
            # Redirige les utilisateurs normaux vers leur profil
            return redirect(url_for("user.show_profile"))
        
        flash(error)
        return redirect(url_for("auth.login"))
    else:
        return render_template('auth/login.html')

# Route /auth/logout
@auth_bp.route('/logout')
def logout():
    # Se déconnecter consiste simplement à supprimer le cookie session
    session.clear()

    # On redirige l'utilisateur vers la page principale une fois qu'il s'est déconnecté
    return redirect(url_for("home.landing_page"))


# Fonction automatiquement appelée à chaque requête (avant d'entrer dans la route) sur une route appartenant au blueprint 'auth_bp'
# La fonction permet d'ajouter un attribut 'user' représentant l'utilisateur connecté dans l'objet 'g' 

@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
        print("Utilisateur non connecté")
    else:
        db = get_db()
        g.user = db.execute(
            'SELECT id_users, username, role FROM users WHERE id_users = ?', (user_id,)
        ).fetchone()
        
        close_db()





    





