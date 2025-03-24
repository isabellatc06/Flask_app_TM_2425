from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db


# Routes /...
home_bp = Blueprint('home', __name__)



# Route /
@home_bp.route('/', methods=('GET', 'POST'))
def landing_page():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits LIMIT 20")
    produits = cursor.fetchall()
  
    return render_template('produit/produit.html', produits=produits)

# Gestionnaire d'erreur 404 pour toutes les routes inconnues
@home_bp.route('/<path:text>', methods=['GET', 'POST'])
def not_found_error(text):
    return render_template('home/404.html'), 404
