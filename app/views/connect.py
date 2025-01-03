from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from app.db.db import get_db, close_db

# Routes /...
connect_bp = Blueprint('connect', __name__)

# Route pour dire qu'on est connecté
@connect_bp.route('/connect', methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        # Logique pour traiter la connexion si nécessaire
        return redirect('/')
    return render_template('connect/connect.html')

@connect_bp.route('/connect2', methods=['GET', 'POST'])
def connect2():
    if request.method == 'POST':
        # Logique pour traiter la connexion si nécessaire
        return redirect('/')
    return render_template('connect/connect2.html')


    