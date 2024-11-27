from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

# Routes /...
reset_bp = Blueprint('reset', __name__)

# Route /
@reset_bp.route('/resett', methods=['GET'])
def reset():
    # Affichage de la page de réinisialization du mot de passe de l'application
    return render_template('reset/reset.html')
