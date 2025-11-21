#!/usr/bin/env bash
# exit on error
set -o errexit

echo "📦 Installation des dépendances..."
pip install -r requirements.txt

echo "🔧 Collection des fichiers statiques..."
python manage.py collectstatic --no-input

echo "🗄️ Migration de la base de données..."
python manage.py migrate

echo "👤 Création du superutilisateur..."
python manage.py create_admin

echo "✅ Build terminé avec succès!"
