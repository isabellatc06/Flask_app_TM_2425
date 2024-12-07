from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db

# Routes /...
garcon_bp = Blueprint('garcon', __name__)

# Route pour les vetements d'exterieur
@garcon_bp.route('/garcon_vetements', methods=['GET', 'POST'])
def garcon_vetements():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("garcon_vetements",))
    produits = cursor.fetchall()
    close_db()
    return render_template('garcon/vetements.html', produits=produits)


# Route pour les t-shirts et debardeurs
@garcon_bp.route('/garcon_debardeurs', methods=['GET', 'POST'])
def garcon_debardeurs():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("garcon_debardeurs",))
    produits = cursor.fetchall()
    close_db()
    return render_template('garcon/debardeurs.html', produits=produits)

# Route pour les pulls et gilets
@garcon_bp.route('/garcon_pulls', methods=['GET', 'POST'])
def garcon_pulls():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("garcon_pulls",))
    produits = cursor.fetchall()
    close_db()
    return render_template('garcon/pulls.html', produits=produits)


# Route pour les pantalons
@garcon_bp.route('/garcon_pantalons', methods=['GET', 'POST'])
def garcon_pantalons():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("garcon_pantalons",))
    produits = cursor.fetchall()
    close_db()
    return render_template('garcon/pantalons.html', produits=produits)


# Route pour les jeans
@garcon_bp.route('/garcon_jeans', methods=['GET', 'POST'])
def garcon_jeans():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("garcon_jeans",))
    produits = cursor.fetchall()
    close_db()
    return render_template('garcon/jeans.html', produits=produits)


# Route pour les maillots de bain
@garcon_bp.route('/garcon_maillots', methods=['GET', 'POST'])
def garcon_maillots():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("garcon_maillots",))
    produits = cursor.fetchall()
    close_db()
    return render_template('garcon/maillots.html', produits=produits)


# Route pour les pyjamas
@garcon_bp.route('/garcon_pyjamas', methods=['GET', 'POST'])
def garcon_pyjamas():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("garcon_pyjamas",))
    produits = cursor.fetchall()
    close_db()
    return render_template('garcon/pyjamas.html', produits=produits)



# Route pour les chaussures
@garcon_bp.route('/garcon_chaussures', methods=['GET', 'POST'])
def garcon_chaussures():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("garcon_chaussures",))
    produits = cursor.fetchall()
    close_db()
    return render_template('garcon/chaussures.html', produits=produits)


