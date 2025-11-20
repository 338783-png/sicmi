# Guide de déploiement sur Render

## 1. Préparer le dépôt GitHub
✅ Déjà fait !

## 2. Créer un compte sur Render
- Allez sur https://render.com
- Inscrivez-vous avec votre compte GitHub

## 3. Créer une base de données PostgreSQL
1. Dans le dashboard Render, cliquez sur "New +"
2. Sélectionnez "PostgreSQL"
3. Configurez :
   - **Name**: sicmi-db
   - **Database**: sicmi_db
   - **User**: sicmi_user
   - **Region**: Frankfurt (EU Central) - le plus proche
   - **Plan**: Free
4. Cliquez sur "Create Database"
5. **Copiez l'URL interne de connexion** (Internal Database URL)

## 4. Créer le Web Service
1. Dans le dashboard, cliquez sur "New +"
2. Sélectionnez "Web Service"
3. Connectez votre repository GitHub `338783-png/sicmi`
4. Configurez :
   - **Name**: sicmi-site
   - **Region**: Frankfurt (EU Central)
   - **Branch**: main
   - **Root Directory**: (laissez vide)
   - **Runtime**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn sicmi_site.wsgi:application`
   - **Plan**: Free

## 5. Ajouter les variables d'environnement
Dans l'onglet "Environment" du Web Service, ajoutez :

```
SECRET_KEY=<générez-une-clé-secrète-django>
DEBUG=False
DATABASE_URL=<collez-l-url-postgres-interne>
EMAIL_HOST_USER=jordanietane2@gmail.com
EMAIL_HOST_PASSWORD=<votre-mot-de-passe-application>
PYTHON_VERSION=3.12.3
```

Pour générer une SECRET_KEY :
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## 6. Déployer
1. Cliquez sur "Create Web Service"
2. Render va automatiquement :
   - Cloner votre repo
   - Installer les dépendances
   - Exécuter les migrations
   - Collecter les fichiers statiques
   - Démarrer l'application

## 7. Configuration finale
Une fois déployé, votre site sera accessible à :
`https://sicmi-site.onrender.com`

### Notes importantes :
- Le plan gratuit met l'app en veille après 15 min d'inactivité
- Le premier chargement après veille prend ~50 secondes
- Les fichiers media uploadés seront perdus au redémarrage (utilisez Cloudinary pour la production)
- La base de données gratuite expire après 90 jours

## 8. Tester l'email
Testez le formulaire de contact sur le site déployé pour vérifier que les emails fonctionnent.
