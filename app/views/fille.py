from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db

# Routes /...
fille_bp = Blueprint('fille', __name__)

# Route pour les robes
@fille_bp.route('/fille_robes', methods=['GET', 'POST'])
def fille_robes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("fille_robes",))
    produits = cursor.fetchall()
    close_db()
    return render_template('fille/robes.html', produits=produits)


# Route pour les vetements d'exterieur
@fille_bp.route('/fille_vetements', methods=['GET', 'POST'])
def fille_vetements():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("fille_vetements",))
    produits = cursor.fetchall()
    close_db()
    return render_template('fille/vetements.html', produits=produits)


# Route pour les pulls et gilets
@fille_bp.route('/fille_pulls', methods=['GET', 'POST'])
def fille_pulls():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("fille_pulls",))
    produits = cursor.fetchall()
    close_db()
    return render_template('fille/pulls.html', produits=produits)


# Route pour les pantalons
@fille_bp.route('/fille_pantalons', methods=['GET', 'POST'])
def fille_pantalons():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("fille_pantalons",))
    produits = cursor.fetchall()
    close_db()
    return render_template('fille/pantalons.html', produits=produits)



# Route pour les jeans
@fille_bp.route('/fille_jeans', methods=['GET', 'POST'])
def fille_jeans():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("fille_jeans",))
    produits = cursor.fetchall()
    close_db()
    return render_template('fille/jeans.html', produits=produits)


# Route pour les jupes et shorts
@fille_bp.route('/fille_jupes', methods=['GET', 'POST'])
def fille_jupes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("fille_jupes",))
    produits = cursor.fetchall()
    close_db()
    return render_template('fille/jupes.html', produits=produits)


# Route pour les maillots de bain
@fille_bp.route('/fille_maillots', methods=['GET', 'POST'])
def fille_maillots():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("fille_maillots",))
    produits = cursor.fetchall()
    close_db()
    return render_template('fille/maillots.html', produits=produits)



# Route pour les pyjamas
@fille_bp.route('/fille_pyjamas', methods=['GET', 'POST'])
def fille_pyjamas():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("fille_pyjamas",))
    produits = cursor.fetchall()
    close_db()
    return render_template('fille/pyjamas.html', produits=produits)


# Route pour les chaussures
@fille_bp.route('/fille_chaussures', methods=['GET', 'POST'])
def fille_chaussures():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("fille_chaussures",))
    produits = cursor.fetchall()
    close_db()
    return render_template('fille/chaussures.html', produits=produits)