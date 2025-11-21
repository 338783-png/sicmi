# 🔐 SICMI - Services et Identifiants

Documentation complète des services utilisés pour le site SICMI Sarl avec identifiants et configurations.

---

## 📋 TABLE DES MATIÈRES

1. [GitHub Repository](#github-repository)
2. [Render Hosting](#render-hosting)
3. [Cloudinary Media Storage](#cloudinary-media-storage)
4. [PostgreSQL Database](#postgresql-database)
5. [Django Admin](#django-admin)
6. [Variables d'Environnement](#variables-denvironnement)
7. [Commandes Utiles](#commandes-utiles)

---

## 🐙 GITHUB REPOSITORY

### Informations
- **Service**: GitHub
- **URL du repo**: https://github.com/338783-png/sicmi
- **Owner**: 338783-png
- **Repository Name**: sicmi
- **Branch principale**: main
- **Visibilité**: Private/Public

### Identifiants GitHub
```
Username: 338783-png
Email: jordaniekenne@gmail.com
Password: [TON MOT DE PASSE GITHUB]
```

### Configuration Git Locale
```bash
git config user.name "338783-png"
git config user.email "jordaniekenne@gmail.com"
```

### Commandes Git Principales
```bash
# Voir le statut
git status

# Ajouter tous les fichiers modifiés
git add -A

# Commit avec message
git commit -m "Votre message"

# Pousser vers GitHub
git push origin main

# Voir l'historique
git log --oneline

# Voir les différences
git diff
```

---

## 🚀 RENDER HOSTING

### Informations du Service
- **Service**: Render.com
- **URL**: https://dashboard.render.com
- **Type de plan**: Free Tier
- **URL du site déployé**: [Votre URL Render, ex: https://sicmi-site.onrender.com]

### Identifiants Render
```
Email: jordaniekenne@gmail.com
Password: [TON MOT DE PASSE RENDER]
```

### Configuration Render
- **Repository connecté**: 338783-png/sicmi
- **Branch**: main
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn sicmi_site.wsgi:application`
- **Auto-Deploy**: ✅ Activé (déploiement automatique à chaque push)

### Variables d'Environnement Render
À configurer dans Render Dashboard → Environment Variables:

```bash
# Django Configuration
SECRET_KEY=votre-secret-key-django-genere
DEBUG=False
ALLOWED_HOSTS=.onrender.com

# Database (PostgreSQL fourni par Render)
DATABASE_URL=postgresql://user:password@host:5432/database
# Note: Cette variable est automatiquement créée par Render

# Cloudinary
CLOUDINARY_CLOUD_NAME=votre_cloud_name
CLOUDINARY_API_KEY=votre_api_key
CLOUDINARY_API_SECRET=votre_api_secret

# Email (si configuré)
EMAIL_HOST_USER=sicmisarl@gmail.com
EMAIL_HOST_PASSWORD=votre_app_password_gmail
```

### Accéder aux Logs Render
```
Dashboard Render → Votre service → Logs
```

---

## ☁️ CLOUDINARY MEDIA STORAGE

### Informations du Service
- **Service**: Cloudinary
- **URL**: https://cloudinary.com/console
- **Plan**: Free Tier (10GB stockage, 25GB bande passante/mois)

### Identifiants Cloudinary
```
Email: jordaniekenne@gmail.com
Password: [TON MOT DE PASSE CLOUDINARY]
```

### Configuration Cloudinary
Trouve tes identifiants dans: Cloudinary Dashboard → Settings → API Keys

```python
# Dans settings.py (déjà configuré)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'votre_cloud_name',
    'API_KEY': 'votre_api_key',
    'API_SECRET': 'votre_api_secret'
}
```

### Variables d'Environnement Cloudinary
```bash
CLOUDINARY_CLOUD_NAME=votre_cloud_name
CLOUDINARY_API_KEY=123456789012345
CLOUDINARY_API_SECRET=abcdefghijklmnopqrstuvwxyz123456
```

### Accéder aux Médias
- **Console Cloudinary**: https://cloudinary.com/console/media_library
- **URL publique des images**: https://res.cloudinary.com/votre_cloud_name/image/upload/...

---

## 🐘 POSTGRESQL DATABASE

### Informations du Service
- **Service**: PostgreSQL (fourni par Render)
- **Version**: PostgreSQL 15+
- **Plan**: Free Tier (expires après 90 jours - nécessite recréation)

### Identifiants PostgreSQL
```
Host: [hostname].render.com
Port: 5432
Database: [database_name]
Username: [username]
Password: [password]

# URL de connexion complète (dans Render Dashboard)
DATABASE_URL=postgresql://username:password@hostname:5432/database_name
```

### Accéder à la Base de Données

#### Via Render Dashboard
```
Render Dashboard → PostgreSQL → Connect → PSQL Command
```

#### Via Ligne de Commande Locale
```bash
# Installer psql (si nécessaire)
sudo apt install postgresql-client

# Se connecter
psql "postgresql://username:password@hostname:5432/database_name"
```

#### Commandes SQL Utiles
```sql
-- Lister les tables
\dt

-- Voir la structure d'une table
\d sicmi_app_service

-- Compter les enregistrements
SELECT COUNT(*) FROM sicmi_app_service;

-- Voir les services
SELECT id, name, category FROM sicmi_app_service;

-- Quitter
\q
```

### Sauvegarder la Base de Données
```bash
# Backup complet
pg_dump "postgresql://user:pass@host:5432/db" > backup.sql

# Restaurer
psql "postgresql://user:pass@host:5432/db" < backup.sql
```

---

## 🔧 DJANGO ADMIN

### Accéder à l'Admin Django
- **URL Locale**: http://127.0.0.1:8000/admin/
- **URL Production**: https://votre-site.onrender.com/admin/

### Identifiants Superuser Django
```
Username: [TON USERNAME ADMIN]
Email: jordaniekenne@gmail.com
Password: [TON MOT DE PASSE ADMIN]
```

### Créer un Nouveau Superuser
```bash
# En local
python manage.py createsuperuser

# Sur Render (via console)
python manage.py createsuperuser --noinput --username admin --email admin@example.com
```

### Sections Admin Disponibles
- **Services** (`/admin/sicmi_app/service/`)
- **Projects** (`/admin/sicmi_app/project/`)
- **Team Members** (`/admin/sicmi_app/teammember/`)
- **Contact Requests** (`/admin/sicmi_app/contactrequest/`)
- **Ateliers** (`/admin/sicmi_app/atelier/`)
- **Users** (`/admin/auth/user/`)

---

## 🔐 VARIABLES D'ENVIRONNEMENT

### Fichier `.env` Local (NON commité sur GitHub)
Crée un fichier `.env` à la racine du projet:

```bash
# Django
SECRET_KEY=django-insecure-votre-secret-key-locale
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Local (SQLite)
# Pas besoin de DATABASE_URL en local, utilise db.sqlite3

# Cloudinary
CLOUDINARY_CLOUD_NAME=votre_cloud_name
CLOUDINARY_API_KEY=123456789012345
CLOUDINARY_API_SECRET=abcdefghijklmnopqrstuvwxyz123456

# Email (optionnel en local)
EMAIL_HOST_USER=sicmisarl@gmail.com
EMAIL_HOST_PASSWORD=votre_app_password
```

### Variables sur Render
Toutes les variables doivent être configurées dans:
```
Render Dashboard → Your Service → Environment → Add Environment Variable
```

**Variables OBLIGATOIRES sur Render:**
1. `SECRET_KEY` - Clé secrète Django unique
2. `DEBUG` - Mettre à `False` en production
3. `ALLOWED_HOSTS` - `.onrender.com`
4. `DATABASE_URL` - Auto-créée par Render
5. `CLOUDINARY_CLOUD_NAME`
6. `CLOUDINARY_API_KEY`
7. `CLOUDINARY_API_SECRET`

---

## 🛠️ COMMANDES UTILES

### Développement Local

```bash
# Lancer le serveur local
python manage.py runserver

# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Shell Django
python manage.py shell
```

### Déploiement

```bash
# 1. Tester localement
python manage.py check
python manage.py test

# 2. Ajouter et commiter les changements
git add -A
git commit -m "Description des changements"

# 3. Pousser vers GitHub (déclenche auto-deploy sur Render)
git push origin main

# 4. Vérifier les logs sur Render Dashboard
```

### Debugging

```bash
# Voir les erreurs Python
python manage.py check --deploy

# Tester les URLs
python manage.py show_urls

# Vider le cache
python manage.py clear_cache

# Voir les requêtes SQL
python manage.py debugsqlshell
```

---

## 📊 RÉCAPITULATIF DES CONNEXIONS

```
┌─────────────────┐
│   DÉVELOPPEUR   │
│  (jordanie)     │
└────────┬────────┘
         │
         ├──────────────────┐
         │                  │
    ┌────▼─────┐      ┌────▼────────┐
    │  GitHub  │◄─────┤  Git Local  │
    │  (Repo)  │      │  /sicmi_site│
    └────┬─────┘      └─────────────┘
         │
         │ (Auto-Deploy)
         │
    ┌────▼─────────────┐
    │     RENDER       │
    │  (Web Hosting)   │
    └────┬────┬────────┘
         │    │
         │    └─────────────┐
         │                  │
    ┌────▼──────┐    ┌─────▼──────────┐
    │PostgreSQL │    │   Cloudinary   │
    │(Database) │    │ (Media Storage)│
    └───────────┘    └────────────────┘
```

---

## ⚠️ SÉCURITÉ

### ❌ NE JAMAIS COMMITER SUR GITHUB:
- `.env` (fichier d'environnement local)
- `db.sqlite3` (base de données locale)
- Mots de passe en clair
- Clés API dans le code
- `SECRET_KEY` de Django

### ✅ BONNES PRATIQUES:
- Utiliser des variables d'environnement
- Garder `DEBUG=False` en production
- Changer les mots de passe régulièrement
- Utiliser des mots de passe forts (12+ caractères)
- Activer l'authentification à deux facteurs (2FA) sur GitHub et Render

---

## 📞 SUPPORT

### Contacts SICMI
- **Email**: sicmisarl@gmail.com
- **Tél**: +237 675948524 / +237 687013563
- **Développeur**: jordaniekenne@gmail.com

### Ressources
- **Django Documentation**: https://docs.djangoproject.com
- **Render Documentation**: https://render.com/docs
- **Cloudinary Documentation**: https://cloudinary.com/documentation
- **PostgreSQL Documentation**: https://www.postgresql.org/docs/

---

## 📝 NOTES IMPORTANTES

1. **Render Free Tier**: Le site peut se mettre en veille après 15 min d'inactivité. Premier chargement = 50s.
2. **PostgreSQL Free**: Expire après 90 jours, nécessite recréation et migration des données.
3. **Cloudinary Free**: 10GB stockage, 25GB bande passante/mois - surveiller l'usage.
4. **Auto-Deploy**: Chaque `git push origin main` déclenche un déploiement automatique (2-3 min).
5. **Migrations**: Toujours tester localement avant de pousser en production.

---

**Document créé le**: 21 novembre 2025  
**Dernière mise à jour**: 21 novembre 2025  
**Version**: 1.0
