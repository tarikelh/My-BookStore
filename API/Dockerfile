# Utilisez une image de base officielle Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /api

# Copier le fichier de configuration des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le contenu du projet
COPY . .

# Exposer le port que l'application va utiliser
EXPOSE 8000

# Définir la commande par défaut pour démarrer l'application
CMD ["python", "Back/manage.py", "runserver", "0.0.0.0:8000"]
