## Overview

CarPi is an addition to my car that I am developing which primarily consists of a Raspberry Pi 3 B+ and a 7" touchscreen display.

## Current Features
#### Hardware
- Raspberry Pi 3B+
  - Wifi + Bluetooth connectivity
- 7" HDMI Touchscreen display (from Adafruit; power and touchscreen data over USB connected to Pi)
- HifiBerry AMP2 connected to built-in speakers
  - Good sound quality + integrated 12V -> 5V power supply for the Pi, no power issues so far
#### Software
- Raspbian Stretch
- Custom Python/Pygame application for playing music (and controlling some features of the Pi, such as Wifi)
- RetroPie install (currently running only a PS1 emulator)

## Planned Features (Near future)
#### Hardware
- Backup camera (170* FOV NoIR camera with CSI-HDMI extenders)
- Adafruit Ultimate GPS hat for navigation data
#### Software
- Camera feed in Pygame interface
- Custom navigation interface using TomTom navigation
