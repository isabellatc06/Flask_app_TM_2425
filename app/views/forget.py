from flask import (Blueprint, app, flash, g, redirect, render_template, request, session, url_for)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from app.config import EMAIL_HOST, EMAIL_PORT, EMAIL_PASSWORD, EMAIL_ADDRESS

# Routes /...
forget_bp = Blueprint('forget', __name__)

def send_email(to_address, subject, message, cc_addresses=None):
    # Création de l'objet email
    email = MIMEMultipart()
    email['From'] = EMAIL_ADDRESS
    email['To'] = to_address
    email['Subject'] = subject

    # Ajout des adresses en copie
    if cc_addresses:
        email['Cc'] = ', '.join(cc_addresses)


    # Ajout du corps de l'email en version HTML (cela permet d'utiliser des tags html dans le message)
    # Pour utiliser une simple chaîne de caractère, il suffit de remplacer par MIMEText(message,'plain')
    email.attach(MIMEText(message, 'html'))

    # Connexion au serveur SMTP et envoi de l'email
    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        # server.set_debuglevel(1)  # Activer les messages de débogage
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        # Envoi de l'email à tous les destinataires (To, Cc)
        server.sendmail(email['From'], [to_address] + cc_addresses, email.as_string())
        server.quit()
        print("Email envoyé avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")



def send_test_email():
    try:
        # Connexion au serveur SMTP
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Création de l'email
        subject = "Test d'envoi d'email"
        body = "Ceci est un email de test envoyé depuis Flask."
        msg = MIMEText(body, 'plain')
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = "isabellatc@outlook.es"  # Remplace par une adresse valide
        msg['Subject'] = subject

        # Envoi de l'email
        server.sendmail(EMAIL_ADDRESS, "isabellatc@outlook.es", msg.as_string())
        server.quit()

        print("Email envoyé avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

send_test_email()

# Route /
@forget_bp.route('/forget', methods=['GET', 'POST'])
def forget():
    if request.method == 'POST':
        # Exemple de récupération de l'adresse email depuis le formulaire
        to_address = request.form.get('email')
        subject = "Réinitialisation de mot de passe"
        message = """
            <html>
                <body>
                    <p>Bonjour,</p>
                    <p>Voici le lien pour réinitialiser votre mot de passe :</p>
                    <a href="{{reset.reset}}">Réinitialiser mon mot de passe</a>
                </body>
            </html>
        """

        if to_address:
            send_email(to_address, subject, message, cc_addresses=[])
            return "Email envoyé avec succès !"
        else:
            flash("Veuillez entrer une adresse email.")
            return render_template('forget/forget.html')
    else:
        return render_template('forget/forget.html')
