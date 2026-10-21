# GalaxyRVR Control Center

Interface web de contrôle pour le rover SunFounder GalaxyRVR, déployable sur Unraid/Synology via Docker Compose.

## Ce que fait ce projet
- Interface web moderne (PC + Meta Quest 3) pour piloter le rover
- Serveur Python FastAPI, WebSocket vers l'ESP32-CAM (port 8765, JSON)
- Modes : manuel, évitement, suivi ; LED RGB, servos, batterie, vidéo
- Remappage clavier depuis l'interface
- Déploiement Docker Compose sur Unraid, intégration Home Assistant possible
- Mock rover inclus pour tester sans matériel

## Structure
- web/ : interface + serveur + tests + mock
- galaxy-rvr/ : firmware Arduino d'origine (SunFounder)

## Démarrage rapide
cd web && cp .env.example .env && docker compose up -d --build
Ouvrir http://IP_SERVEUR:8081

## Tests
cd web && ./run_tests.sh
