from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db.db import get_db, close_db
import os

# Création d'un blueprint contenant les routes ayant le préfixe /auth/...
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Route /auth/register
@admin_bp.route('/produits_admin', methods=('GET', 'POST'))
def admin():

    # Si des données de formulaire sont envoyées vers la route /register (ce qui est le cas lorsque le formulaire d'inscription est envoyé)
    if request.method == 'POST':

        # On récupère les champs 'username' et 'password' de la requête HTTP
        nom = request.form['nom']
        description = request.form['description']
        taille = request.form['taille']
        prix = request.form['prix']
        chemin_vers_le_fichier_img = request.form['chemin_vers_le_fichier_img']
        categorie = request.form['categorie']

        if not categorie:
            flash("Veuillez sélectionner une catégorie.", "error")
            return redirect(url_for("admin.admin"))

        # On récupère la base de donnée
        db = get_db()

        # Si le nom d'utilisateur et le mot de passe ont bien une valeur
        # on essaie d'insérer l'utilisateur dans la base de données
        if nom and description and taille and prix and chemin_vers_le_fichier_img and categorie:

            db.execute("INSERT INTO produits (nom, description, taille, prix, chemin_vers_le_fichier_img, categorie) VALUES (?, ?, ?, ?, ?, ?)",(nom, description, taille, prix, chemin_vers_le_fichier_img, categorie))
            # db.commit() permet de valider une modification de la base de données
            db.commit()
            # On ferme la connexion à la base de données pour éviter les fuites de mémoire
            close_db()
                
            
            return redirect(url_for("admin.admin"))
         
        
    else:
        # Si aucune donnée de formulaire n'est envoyée, on affiche le formulaire d'inscription
        return render_template('admin/admin.html')