from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db

# Routes /...
homme_bp = Blueprint('homme', __name__)

# Route pour les t-shirts et polos
@homme_bp.route('/homme_polos', methods=['GET', 'POST'])
def homme_polos():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_polos",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/polos.html', produits=produits)

#Route pour les chemises
@homme_bp.route('/homme_chemises', methods=['GET', 'POST'])
def homme_chemises():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_chemises",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/chemises.html', produits=produits)


#Route pour les sweats et hoodies
@homme_bp.route('/homme_sweats', methods=['GET', 'POST'])
def homme_sweats():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_sweats",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/sweats.html', produits=produits)


#Route pour les mailles
@homme_bp.route('/homme_mailles', methods=['GET', 'POST'])
def homme_mailles():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_mailles",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/mailles.html', produits=produits)



#Route pour les vestes et manteaux 
@homme_bp.route('/homme_vestes', methods=['GET', 'POST'])
def homme_vestes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_vestes",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/vestes.html', produits=produits)


#Route pour les pantalons 
@homme_bp.route('/homme_pantalons', methods=['GET', 'POST'])
def homme_pantalons():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_pantalons",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/pantalons.html', produits=produits)


#Route pour les jeans 
@homme_bp.route('/homme_jeans', methods=['GET', 'POST'])
def homme_jeans():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_jeans",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/jeans.html', produits=produits)



#Route pour les shorts et bermudas
@homme_bp.route('/homme_shorts', methods=['GET', 'POST'])
def homme_shorts():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_shorts",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/shorts.html', produits=produits)



#Route pour les joggins
@homme_bp.route('/homme_joggins', methods=['GET', 'POST'])
def homme_joggins():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_joggins",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/joggins.html', produits=produits)



#Route pour les maillots de bain
@homme_bp.route('/homme_maillots', methods=['GET', 'POST'])
def homme_maillots():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_maillots",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/maillots.html', produits=produits)



#Route pour les pyjamas
@homme_bp.route('/homme_pyjamas', methods=['GET', 'POST'])
def homme_pyjamas():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_pyjamas",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/pyjamas.html', produits=produits)


#Route pour les chaussures
@homme_bp.route('/homme_chaussures', methods=['GET', 'POST'])
def homme_chaussures():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produits WHERE categorie = ?", ("homme_chaussures",))
    produits = cursor.fetchall()
    close_db()
    return render_template('homme/chaussures.html', produits=produits)