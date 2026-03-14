from flask import Flask, jsonify
import sqlite3
from flask import request

app = Flask(__name__)

# 🚨 FAILLE DE SÉCURITÉ VOLONTAIRE 🚨
# Un développeur a laissé ces identifiants "en dur" dans le code
DB_PASSWORD = "SuperSecretPassword123!"
AWS_API_KEY = "AKIAIOSFODNN7EXAMPLE"
# Faux token GitHub pour déclencher l'alerte
GITHUB_TOKEN = "ghp_1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

@app.route('/')
def home():
    # En réalité, l'application utiliserait le mot de passe ici pour se connecter
    return jsonify({
        "status": "success",
        "message": "Bienvenue sur l'API SuperBoutique !",
        "warning": "Cette application n'est pas sécurisée."
    })

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/recherche')
def recherche():
    utilisateur = request.args.get('nom')
    conn = sqlite3.connect('mabase.db')
    cursor = conn.cursor()
    
    # 🚨 FAILLE DE SÉCURITÉ (Injection SQL) 🚨
    # On insère directement ce que l'utilisateur a tapé dans la requête.
    # Un pirate pourrait taper :  "nom'; DROP TABLE utilisateurs;--"
    requete = f"SELECT * FROM utilisateurs WHERE nom = '{utilisateur}'"
    cursor.execute(requete)
    
    return "Recherche terminée"