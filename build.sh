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

echo "👥 Chargement des membres de l'équipe..."
python manage.py load_team_members

echo "🏭 Chargement des ateliers et équipements..."
python manage.py load_ateliers

echo "📦 Chargement des services..."
python manage.py load_services

echo "🏗️ Chargement des projets..."
python manage.py load_projects

echo "🖼️ Migration des images vers Cloudinary..."
python manage.py migrate_images_to_cloudinary || echo "⚠️ Migration images ignorée (pas de fichiers locaux en production)"

echo "✅ Build terminé avec succès!"
