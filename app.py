from flask import Flask, jsonify

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