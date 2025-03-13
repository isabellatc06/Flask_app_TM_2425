from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db

barre_recherche_bp = Blueprint('barre_recherche', __name__)

@barre_recherche_bp.route('/recherche', methods=['GET'])
def index():
    produits = []  
    nom = request.args.get("nom", "").strip().lower()  # Passer en GET pour la recherche
    print(f"Recherche: {nom}")

    if nom:
        db = get_db()
        print(f"Connexion à la base: {db}")  # Vérifie la connexion

        produits = db.execute(
            "SELECT * FROM produits WHERE LOWER(nom) LIKE ?", 
            (f"%{nom}%",)
        ).fetchall()
        
        print(f"Produits trouvés: {produits}")  # Vérifie les résultats

    return render_template("search/search.html", produits=produits)
