from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db
import sqlite3

# Routes /...
produit_bp = Blueprint('produit', __name__)

def get_db():
    db = sqlite3.connect('Flask_app_TM_2425/app/db/app.db')
    db.row_factory = sqlite3.Row
    return db



@produit_bp.route('/produit/<categorie>', methods=['GET', 'POST'])
def produit_categorie(categorie):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", (categorie,))
    produits = cursor.fetchall()
    close_db()
    titre_page = categorie.replace('_', ' ').capitalize()
    
    return render_template('produit/produit.html', produits=produits, titre=titre_page)



@produit_bp.route('/produit/<int:id>', methods=['GET'])
def produit_view(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id_produits, nom, description, taille, prix, chemin_vers_le_fichier_img FROM produits WHERE id_produits = ?", (id,))
    produit = cursor.fetchone()
    close_db()

    if produit is None:
        return "Produit non trouvé", 404

    titre_page = produit["nom"].replace('_', ' ').capitalize()
    return render_template("produit/produit_view.html", produit=produit, titre=titre_page)


