#!/usr/bin/env python3
"""
Script pour garder le site SICMI actif sur Render
Pinge le site toutes les 5 minutes pour éviter la mise en veille
"""

import requests
import time
import logging
from datetime import datetime

# Configuration
SITE_URL = "https://sicmi-site.onrender.com"
PING_INTERVAL = 300  # 5 minutes en secondes (300s)
TIMEOUT = 30  # Timeout pour les requêtes en secondes

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('keep_alive.log'),
        logging.StreamHandler()
    ]
)

def ping_site():
    """Envoie une requête GET au site pour le garder actif"""
    try:
        logging.info(f"🔄 Ping du site {SITE_URL}...")
        response = requests.get(SITE_URL, timeout=TIMEOUT)
        
        if response.status_code == 200:
            logging.info(f"✅ Site actif - Status: {response.status_code} - Temps: {response.elapsed.total_seconds():.2f}s")
            return True
        else:
            logging.warning(f"⚠️ Status inhabituel: {response.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        logging.error(f"❌ Timeout après {TIMEOUT}s")
        return False
    except requests.exceptions.ConnectionError:
        logging.error(f"❌ Erreur de connexion - Le site est peut-être en démarrage")
        return False
    except Exception as e:
        logging.error(f"❌ Erreur: {str(e)}")
        return False

def main():
    """Boucle principale du script"""
    logging.info("=" * 50)
    logging.info("🤖 Démarrage du robot Keep-Alive pour SICMI")
    logging.info(f"📍 Site: {SITE_URL}")
    logging.info(f"⏱️ Intervalle: {PING_INTERVAL}s ({PING_INTERVAL/60:.1f} minutes)")
    logging.info("=" * 50)
    
    ping_count = 0
    success_count = 0
    
    try:
        while True:
            ping_count += 1
            logging.info(f"\n--- Ping #{ping_count} ---")
            
            if ping_site():
                success_count += 1
            
            # Statistiques
            success_rate = (success_count / ping_count) * 100
            logging.info(f"📊 Stats: {success_count}/{ping_count} réussis ({success_rate:.1f}%)")
            
            # Attente avant le prochain ping
            logging.info(f"💤 Attente de {PING_INTERVAL/60:.1f} minutes...")
            time.sleep(PING_INTERVAL)
            
    except KeyboardInterrupt:
        logging.info("\n" + "=" * 50)
        logging.info(f"⏹️ Arrêt du robot")
        logging.info(f"📊 Statistiques finales: {success_count}/{ping_count} pings réussis")
        logging.info("=" * 50)

if __name__ == "__main__":
    main()
