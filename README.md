## Overview

CarPi is an addition to my car that I am developing which primarily consists of a Raspberry Pi 3 B+ and a 7" touchscreen display.

## Current Features
#### Hardware
- Raspberry Pi 3B+
  - Wifi + Bluetooth connectivity
- 7" HDMI Touchscreen display (from Adafruit; power and touchscreen data over USB connected to Pi)
- HifiBerry AMP2 connected to built-in speakers
  - Good sound quality &  integrated 12V -> 5V power supply for the Pi, no power issues so far
#### Software
- Raspbian Stretch
- Custom Python/Pygame application for playing music (and controlling some features of the Pi, such as Wifi)
- RetroPie install (currently running only a PS1 emulator)

## Planned Features (Near future)
#### Hardware
- Backup camera (170* FOV NoIR camera with CSI-HDMI extenders)
- MCP3008 ADC
- USB Microphone
- Adafruit Ultimate GPS hat for navigation data
#### Software
- Camera feed in Pygame interface
- Steering wheel button connection (via ADC)
- Voice commands
- Custom navigation interface using TomTom navigation

## Setup
This project is not yet in a position to be widely distributed, but if you're willing to check it out I have hardware and software setup instructions below.

#### Hardware
Here is the list of parts you will need to build a base model CarPi:

| Name                                    | Source   | Price | Link                                                                               |
|-----------------------------------------|----------|-------|------------------------------------------------------------------------------------|
| Raspberry Pi 3B+                        | Adafruit | $35   | https://www.adafruit.com/product/3775                                              |
| HDMI 7" Display (800x480 - Touchscreen) | Adafruit | $90   | https://www.adafruit.com/product/2407                                              |
| DIY HDMI or USB Ribbon Cable (Qty 2)    | Adafruit | $3x2  | https://www.adafruit.com/product/3562                                              |
| Right-angle HDMI Plug                   | Adafruit | $6.50 | https://www.adafruit.com/product/3549                                              |
| Straight HDMI Plug                      | Adafruit | $6.50 | https://www.adafruit.com/product/3548                                              |
| Right-angle USB Micro Plug              | Adafruit | $5    | https://www.adafruit.com/product/4105                                              |
| Straight USB A Plug                     | Adafruit | $5    | https://www.adafruit.com/product/4109                                              |
| M2.5 Standoffs (for Amp2; Qty 2)        | Adafruit | $1.50x2 | https://www.adafruit.com/product/2336                              |
| HifiBerry Amp2                          | Amazon   | $48   | https://www.amazon.com/HiFiBerry-Hifiberry-AMP2-Amp2/dp/B076DLCRHF |

That totals $157 from Adafruit and $48 from Amazon. You can cut $35 off your Adafruit purchase if you would like to use a Raspberry Pi 3B+ you already have.
> Note: You will also need a microSD card for the Raspberry Pi. Buy whatever size and brand fits you. This was tested with a 16GB microSD card (8GB might work). A power supply is recommended for setup and testing, but is not required (the Amp2 has a built-in power supply that will work as long as everything is connected properly).

The hardware setup is straightforward:
1. Screw the standoffs onto the Amp2. (Place the male side of the standoffs through the Amp2 so the female side rests against the Raspberry Pi)
2. Plug the Amp2 into the GPIO header of the Raspberry Pi
3. Connect one of the ribbon cables to each HDMI plug
4. Connect the other ribbon cable to each USB plug
5. Plug in the HDMI cable to the Raspberry Pi and the display (with the right-angle connector connected to the display)
6. Connect the USB cable to the Raspberry Pi and the display (with the right-angle Micro USB connector connected to the display)
7. Connect the + and - wires for each speaker to the Amp2
8. Connect the 12V and GND wires from your car to the Amp2

> Note: If you are connecting four speakers to the system, you will need to run them in parallel or series. With 4Ω speakers, connect the left speakers together in series (+ to -), which connects to the left channel, and the right speakers together in series, which connects to the right channel. With 8Ω speakers, connect the left speakers together in parallel (+ to +; - to -), which both connect to the left channel, and the right speakers together in parallel, which both connect to the right channel.

#### Software
There will be an image file in Releases. This file will allow you to flash an SD card with a working copy of the software. There is no additional setup, it should just work (assuming the hardware is setup properly). The root password is carpi.
