from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db

# Routes /...
produit_bp = Blueprint('produit', __name__)



@produit_bp.route('/produit/<categorie>', methods=['GET', 'POST'])
def produit_categorie(categorie):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", (categorie,))
    produits = cursor.fetchall()
    close_db()
    titre_page = categorie.replace('_', ' ').capitalize()
    
    return render_template('produit/produit.html', produits=produits, titre=titre_page)


@produit_bp.route('/produit/<slug>', methods=['GET'])
def produit_view(slug):
    db = get_db()
    produit = db.execute(
        "SELECT * FROM produits WHERE LOWER(nom) = ?", (slug.lower(),)
    ).fetchone()

    if produit is None:
        return "Produit non trouvé", 404

    produit_dict = dict(produit)
    return render_template("produit/produit_view.html", produit=produit_dict)





