from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db


# Routes /...
home_bp = Blueprint('home', __name__)



# Route /
@home_bp.route('/', methods=('GET', 'POST'))
def landing_page():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits")
    produits = cursor.fetchall()

    id_produits = request.args.get('id_produits')
    nom = request.args.get('nom')
    description = request.args.get('description')
    taille = request.args.get('taille')
    prix = request.args.get('prix')
    id_categorie_produits = request.args.get('id_categorie_produits')
    chemin_vers_le_fichier_img = request.args.get('chemin_vers_le_fichier_img')

    
    
    return render_template('home/index.html', produits=produits)

# Gestionnaire d'erreur 404 pour toutes les routes inconnues
@home_bp.route('/<path:text>', methods=['GET', 'POST'])
def not_found_error(text):
    return render_template('home/404.html'), 404
