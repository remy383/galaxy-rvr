# GalaxyRVR

Arduino UNO firmware for the GalaxyRVR robot car, works with the SunFounder Controller APP.

Current version: **2.0.3**

- [What this project does](#what-this-project-does)
- [Présentation (FR)](#présentation-fr)
- [Dev Environment](#dev-environment)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Firmware Flashing](#firmware-flashing)
- [Docs](#docs)
- [About SunFounder](#about-sunfounder)

## What this project does

GalaxyRVR is the firmware that runs the SunFounder GalaxyRVR, a Mars-rover style robot car. It runs on an Arduino UNO, drives the motors, and talks to an ESP32-CAM AI camera module that provides WiFi, a live video stream and a WebSocket link to your phone.

What the robot can do:

- **Remote control**: drive the car from the SunFounder Controller APP (or Robo Pilot / Mammoth Coding in v2) over WiFi, with live camera view.
- **Obstacle avoidance**: the car steers around obstacles using the ultrasonic sensor and IR obstacle sensors.
- **Obstacle following**: the car follows an object or hand placed in front of it.
- **Lighting**: RGB LED strip with preset colors.
- **Camera gimbal**: the camera pan/tilt servos are controlled by software PWM.
- **Battery monitoring**: reads battery voltage and percentage.

How it works: the main sketch runs a small state machine. `STATE_IDLE` waits for the APP to connect (LED blinks), then `STATE_APP` handles one of three modes: `MODE_APP_CONTROL`, `MODE_OBSTACLE_AVOIDANCE` or `MODE_OBSTACLE_FOLLOWING`. The APP sends control frames (motor, RGB, servo, front light, avoidance mode) over WebSocket.

The repository also contains step-by-step tutorial sketches (`lesson_codes/`), Scratch projects (`scratch_codes/`) and a factory electrical test (`test/`).

## Présentation (FR)

GalaxyRVR est le firmware du robot SunFounder GalaxyRVR (rover de type Mars). Il tourne sur Arduino UNO, pilote les moteurs et communique avec le module caméra ESP32-CAM (WiFi, flux vidéo, WebSocket) pour être contrôlé depuis un smartphone.

Fonctions : pilotage à distance via l'application SunFounder Controller, évitement d'obstacles (ultrasons + capteurs infrarouges), suivi d'objet, bandeau LED RGB, support caméra motorisé (servos) et mesure de la batterie. Le dépôt inclut aussi des exemples de cours, des projets Scratch et un test électrique.

## Dev Environment

| Item | Version |
|------|---------|
| Board | Arduino UNO |
| IDE | Arduino IDE 2.x |
| AVR Boards | 1.8.3 |

Dependencies:

- IRLremote
- SoftPWM
- Servo
- ArduinoJson
- **SunFounder_AI_Camera >= 1.2.2** — required for 1.4.x camera support, the reply-copy fix and
  the complete IP address printed at startup; the sketch fails to compile with anything older
  (see [CHANGELOG.md](CHANGELOG.md))

## Quick Start

1. Open `galaxy-rvr/galaxy-rvr.ino` in Arduino IDE
2. Select Board: Arduino UNO, pick the correct port
3. Compile and upload
4. Install SunFounder Controller APP on your phone, connect to WiFi `GalaxyRVR` (password `12345678`)

## Project Structure

```
galaxy-rvr/
├── galaxy-rvr/                   # Main firmware
│   ├── galaxy-rvr.ino            # Entry point (setup/loop/state machine/WS handler)
│   ├── galaxy-rvr.h              # Central config (pins, constants, includes)
│   ├── cmd_code_config.hpp       # Mode definitions, voice command table
│   ├── car_control.cpp/h         # Motor driver
│   ├── rgb.cpp/h                 # RGB LED strip
│   ├── ir_obstacle.cpp/h         # IR obstacle avoidance sensor
│   ├── ultrasonic.cpp/h          # Ultrasonic distance sensor
│   ├── soft_servo.cpp/h          # Software PWM servo (camera gimbal)
│   ├── battery.h                 # Battery voltage / percentage
│   └── test.h                    # Per-module test routines
├── lesson_codes/                 # Tutorial examples (by chapter)
│   ├── 5_car_move/               # Car movement
│   ├── 6_read_ir/                # IR sensor read
│   ├── 6_ir_avoid/               # IR obstacle avoidance
│   ├── 7_read_ultrasonic/        # Ultrasonic read
│   ├── 7_ultrasonic_avoid/       # Ultrasonic avoidance
│   ├── 8_ultrasonic_ir_avoid/    # Ultrasonic + IR avoidance
│   ├── 8_ultrasonic_ir_follow/   # Ultrasonic + IR follow
│   ├── 9_rgb_*/                  # RGB LED control
│   ├── 10_servo*/                # Servo control
│   ├── 11_camera_*/              # Camera control
│   ├── 12_app_*/                 # APP interaction
│   └── 13_*battery*/             # Battery monitoring
├── test/
│   └── electric-test/            # Factory electrical test
├── ai-camera-firmware.v1.5.3-ota.bin  # ESP32-CAM firmware image
├── update-arduino-firmware.bat    # One-click flash script (Windows)
├── LICENSE
└── Readme.md
```

## Firmware Flashing

### Option 1: One-click script (Windows)

```bat
update-arduino-firmware.bat
```

The script uses `avrdude` to flash `galaxy-rvr.ino.2.0.0.hex`.

### Option 2: Arduino IDE

Open `galaxy-rvr/galaxy-rvr.ino`, compile and upload.

### ESP32-CAM firmware

The AI Camera module requires its own firmware. See [ai-camera-firmware](https://github.com/sunfounder/ai-camera-firmware) for source and instructions.

## Docs

https://docs.sunfounder.com/projects/galaxy-rvr/en/latest/

French docs: https://docs.sunfounder.com/projects/galaxy-rvr/fr/latest/

## About SunFounder

SunFounder focuses on STEAM education with open-source robots, dev boards, kits, and modules. We help students and hobbyists learn programming and engineering through hands-on practice.

Website: [www.sunfounder.com](https://www.sunfounder.com)

Contact: [service@sunfounder.com](mailto:service@sunfounder.com)
