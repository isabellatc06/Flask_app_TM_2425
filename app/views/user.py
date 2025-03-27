from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.utils import *
from app.db.db import get_db, close_db
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from functools import wraps

# Routes /user/...
user_bp = Blueprint('user', __name__, url_prefix='/user')

def get_db():
    db = sqlite3.connect('Flask_app_TM_2425/app/db/app.db')
    db.row_factory = sqlite3.Row
    return db



# Route /user/profile accessible uniquement à un utilisateur connecté grâce au décorateur @login_required --> affiche profile
@user_bp.route('/profile', methods=('GET', 'POST'))
@login_required 
def show_profile():
    # Affichage de la page principale de l'application
    return render_template('user/profile.html')

@user_bp.route('/profile_')
def diriger():
    id_users = session.get('user_id')  
    
    if not id_users:
        flash("Vous devez être connecté pour accéder à cette page.", "error")
        return redirect(url_for("auth.login"))
    
    # Connexion à la base de données et récupération des données de l'utilisateur
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE id_users = ?", (id_users,)).fetchone()
    
    
    
    # Passer les données de l'utilisateur au template
    return render_template('user/donnes.html', user=user)
    


@user_bp.route('/profile_view', methods=['GET', 'POST'])
def show_changes():
    id_users = session.get('user_id')  # Récupérer l'ID de l'utilisateur connecté avec la bonne clé
    print("ID utilisateur récupéré :", id_users)  # Debug

    if not id_users:
        flash("Vous devez être connecté pour accéder à cette page.", "error")
        return redirect(url_for("auth.login"))

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE id_users = ?", (id_users,)).fetchone()

    if request.method == 'POST':
        # Récupérer les champs du formulaire ou utiliser les valeurs actuelles
        username = request.form.get('username') or user['username']
        password = request.form.get('password')  # Peut être vide
        rue = request.form.get('rue') or user['rue']
        no_rue = request.form.get('no_rue') or user['no_rue']
        code_postal = request.form.get('code_postal') or user['code_postal']
        ville = request.form.get('ville') or user['ville']

        # Validation des données (par exemple, vérifier que le nom d'utilisateur fait plus de 3 caractères)
        if len(username) < 3:
            flash("Le nom d'utilisateur doit contenir au moins 3 caractères.", "error")
            return redirect(url_for('user.show_changes'))

        # Hash du mot de passe uniquement s'il est modifié
        password_hashed = generate_password_hash(password) if password else user['password']

        # Requête SQL pour mettre à jour l'utilisateur
        try:
            db.execute("""
                UPDATE users
                SET username = ?, password = ?, rue = ?, no_rue = ?, code_postal = ?, ville = ?
                WHERE id_users = ?
            """, (username, password_hashed, rue, no_rue, code_postal, ville, id_users))
            db.commit()  # Appliquer les changements
            flash("Votre profil a été mis à jour avec succès !", "success")
            return redirect(url_for('user.show_changes'))  # Redirige vers la même page pour voir les modifications
        except Exception as e:
            db.rollback()  # Annule la transaction en cas d'erreur
            print("Erreur SQL : ", e)  # Affiche l'erreur dans la console
            flash("Erreur lors de la mise à jour du profil.", "error")

    return render_template('user/profile_view.html', user=user)



