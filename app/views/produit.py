from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db

# Routes /...
produit_bp = Blueprint('produit', __name__)


'''
# Route pour les robes
@femme_bp.route('/femme_robes', methods=['GET', 'POST'])
def femme_robes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_robes",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/robes.html', produits=produits)
'''


@produit_bp.route('/produit/<categorie>', methods=['GET', 'POST'])
def produit_categorie(categorie):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", (categorie,))
    produits = cursor.fetchall()
    close_db()
    
    # Titre de la page dynamique
    titre_page = categorie.replace('_', ' ').capitalize()
    
    return render_template('produit/produit.html', produits=produits, titre=titre_page)

