# 🤖 Keep-Alive Robot pour SICMI

Ce dossier contient les solutions pour garder le site SICMI actif sur Render et éviter la mise en veille.

## 🎯 Problème

Render free tier met les services en veille après **15 minutes d'inactivité**. Le premier chargement après la veille prend **~50 secondes**.

## ✅ Solutions

### 1. UptimeRobot (Recommandé - 100% Gratuit)

**Avantages** :
- ✅ Gratuit à vie
- ✅ Aucun code à maintenir
- ✅ Interface web simple
- ✅ Surveillance 24/7
- ✅ Alertes email en cas de panne

**Configuration** :
1. Créer un compte sur https://uptimerobot.com
2. Ajouter un nouveau monitor :
   - **Type** : HTTP(s)
   - **URL** : `https://sicmi-site.onrender.com`
   - **Monitoring Interval** : 5 minutes
   - **Monitor Timeout** : 30 secondes
3. Activer les notifications email (optionnel)

### 2. Cron-Job.org (Alternative gratuite)

**Configuration** :
1. Créer un compte sur https://cron-job.org
2. Créer un nouveau cronjob :
   - **URL** : `https://sicmi-site.onrender.com`
   - **Schedule** : `*/5 * * * *` (toutes les 5 minutes)
   - **Timeout** : 30 secondes

### 3. Script Python Local (keep_alive.py)

**Utilisation** :
```bash
# Installer les dépendances
pip install requests

# Lancer le script
python keep_alive.py

# Ou en arrière-plan sur Linux/Mac
nohup python keep_alive.py > /dev/null 2>&1 &
```

**Note** : Cette solution nécessite un ordinateur toujours allumé.

### 4. GitHub Actions (Automatique dans le cloud)

Créer `.github/workflows/keep-alive.yml` :

```yaml
name: Keep Site Alive

on:
  schedule:
    # Toutes les 5 minutes
    - cron: '*/5 * * * *'
  workflow_dispatch:

jobs:
  ping:
    runs-on: ubuntu-latest
    steps:
      - name: Ping SICMI Site
        run: |
          curl -s -o /dev/null -w "Status: %{http_code}\n" https://sicmi-site.onrender.com
```

## 📊 Comparaison des Solutions

| Solution | Coût | Maintenance | Fiabilité | Difficulté |
|----------|------|-------------|-----------|------------|
| **UptimeRobot** | Gratuit | Aucune | ⭐⭐⭐⭐⭐ | Facile |
| **Cron-Job.org** | Gratuit | Aucune | ⭐⭐⭐⭐ | Facile |
| **GitHub Actions** | Gratuit | Faible | ⭐⭐⭐⭐ | Moyenne |
| **Script Python** | Gratuit | Élevée | ⭐⭐⭐ | Difficile |

## 🎖️ Solution Recommandée

**UptimeRobot** est la meilleure option car :
- Aucun code à maintenir
- Surveillance professionnelle
- Alertes automatiques
- Statistiques de disponibilité
- Gratuit pour toujours

## 📝 Configuration UptimeRobot (Détaillée)

1. **Créer un compte** :
   - Aller sur https://uptimerobot.com
   - Cliquer sur "Sign Up Free"
   - Utiliser l'email : `jordaniekenne@gmail.com`

2. **Ajouter le monitor SICMI** :
   - Cliquer sur "+ Add New Monitor"
   - Remplir :
     ```
     Monitor Type: HTTP(s)
     Friendly Name: SICMI Site
     URL: https://sicmi-site.onrender.com
     Monitoring Interval: 5 minutes
     Monitor Timeout: 30 seconds
     ```
   - Cliquer sur "Create Monitor"

3. **Configuration des alertes (optionnel)** :
   - Aller dans "Alert Contacts"
   - Ajouter votre email
   - Vous recevrez des notifications si le site est down

4. **Vérifier le statut** :
   - Le dashboard montre :
     - Uptime % (temps de disponibilité)
     - Response time (temps de réponse)
     - Status history (historique)

## 🔧 Utilisation du Script Python

Si vous préférez le script local :

```bash
# Installation
pip install requests

# Lancer (console)
python keep_alive.py

# Lancer en arrière-plan (Linux/Mac)
nohup python keep_alive.py > keep_alive.log 2>&1 &

# Vérifier les logs
tail -f keep_alive.log

# Arrêter
pkill -f keep_alive.py
```

**Logs disponibles** : Le script crée `keep_alive.log` avec l'historique des pings.

## ⚠️ Important

- **Render free tier** : Le site peut quand même se mettre en veille si pas de trafic pendant 15 min
- **Pings toutes les 5 minutes** : Empêche la mise en veille automatique
- **Premier chargement** : Peut prendre 50s si le site était endormi
- **Limite mensuelle** : Render free tier a 750 heures/mois (31 jours × 24h = 744h) - largement suffisant

## 📈 Amélioration Future

Pour éliminer complètement le problème :
- **Render Starter Plan** ($7/mois) : Pas de mise en veille
- **Railway** : Alternative avec plan gratuit généreux
- **Fly.io** : Autre alternative avec keep-alive intégré

## 🆘 Support

En cas de problème :
1. Vérifier que l'URL est accessible : https://sicmi-site.onrender.com
2. Consulter les logs Render : https://dashboard.render.com
3. Vérifier les logs du robot (si script Python)
4. Contacter le support Render si down prolongé

---

**Créé le** : 22 novembre 2025  
**Pour** : SICMI Sarl - Site Web  
**Maintenu par** : jordaniekenne@gmail.com
