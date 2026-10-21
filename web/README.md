# GalaxyRVR Control Center

Interface web de contrôle pour le rover SunFounder GalaxyRVR, déployable sur Unraid/Synology via Docker Compose.

## Fonctions
- Pilotage clavier/souris (remappable) et joystick virtuel
- Modes : contrôle manuel, évitement d'obstacles, suivi d'objet
- LED RGB, servos caméra, batterie, flux vidéo ESP32-CAM
- WebSocket vers le rover (port 8765, JSON)
- Mock rover pour tester sans matériel
- Compatible Meta Quest 3 (navigateur)

## Déploiement Unraid
1. Copier le dossier dans /mnt/user/appdata/galaxyrvr/
2. cp .env.example .env puis renseigner ROVER_IP
3. docker compose up -d --build
4. Ouvrir http://IP_UNRAID:8081

## Tests
./run_tests.sh
