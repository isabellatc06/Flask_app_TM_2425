from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db

# Routes /...
femme_bp = Blueprint('femme', __name__)

# Route pour les robes
@femme_bp.route('/femme_robes', methods=['GET', 'POST'])
def femme_robes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_robes",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/robes.html', produits=produits)


#Route pour les tops et t-shirt
@femme_bp.route('/femme_tops', methods=['GET', 'POST'])
def femme_tops():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_tops",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/tops.html', produits=produits)

#Route pour les chemises et blusons
@femme_bp.route('/femme_chemises', methods=['GET', 'POST'])
def femme_chemises():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_chemises",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/chemises.html', produits=produits)


#Route pour les sweats et sweats à capuche 
@femme_bp.route('/femme_sweats', methods=['GET', 'POST'])
def femme_sweats():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_sweats",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/sweats.html', produits=produits)

#Route pour les pulls et gilets
@femme_bp.route('/femme_pulls', methods=['GET', 'POST'])
def femme_pulls():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_pulls",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/pulls.html', produits=produits)


#Route pour les vestes et blazers
@femme_bp.route('/femme_vestes', methods=['GET', 'POST'])
def femme_vestes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_vestes",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/vestes.html', produits=produits)


#Route pour les pantalons et leggins
@femme_bp.route('/femme_pantalons', methods=['GET', 'POST'])
def femme_pantalons():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_pantalons",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/pantalons.html', produits=produits)


#Route pour les jeans
@femme_bp.route('/femme_jeans', methods=['GET', 'POST'])
def femme_jeans():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_jeans",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/jeans.html', produits=produits)


#Route pour les jupes et shorts
@femme_bp.route('/femme_jupes', methods=['GET', 'POST'])
def femme_jupes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_jupes",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/jupes.html', produits=produits)

#Route pour les combinaisons
@femme_bp.route('/femme_combinaisons', methods=['GET', 'POST'])
def femme_combinaisons():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_combinaisons",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/combinaisons.html', produits=produits)

#Route pour les maillots de bain
@femme_bp.route('/femme_maillots', methods=['GET', 'POST'])
def femme_maillots():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_maillots",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/maillots.html', produits=produits)


#Route pour les pyjamas et nuisettes
@femme_bp.route('/femme_pyjamas', methods=['GET', 'POST'])
def femme_pyjamas():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_pyjamas",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/pyjamas.html', produits=produits)


#Route pour les chaussures
@femme_bp.route('/femme_chaussures', methods=['GET', 'POST'])
def femme_chaussures():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("femme_chaussures",))
    produits = cursor.fetchall()
    close_db()
    return render_template('femme/chaussures.html', produits=produits)