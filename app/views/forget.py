from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

# Routes /...
forget_bp = Blueprint('forget', __name__)

# Route /
@forget_bp.route('/forget', methods=['GET'])
def forget():
    # Affichage de la page de réinisialization du mot de passe de l'application
    return render_template('forget/forget.html')
