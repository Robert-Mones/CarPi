## Overview

CarPi is an addition to my car that I am developing which primarily consists of a Raspberry Pi 3 B+, a 7" touchscreen display, and an amp.

## Current Features
#### Hardware
- Raspberry Pi 3B+
  - Wifi + Bluetooth connectivity
- 7" HDMI Touchscreen display
  - Power and touchscreen data over USB connected to Pi
- HifiBerry AMP2
  - Connected to built-in car speakers
  - Good sound quality &  integrated 12V -> 5V power supply for the Pi, no power issues so far
- Wide-angle NoIR Camera
  - 175* FOV and no IR filter
  - CSI-HDMI Extension Boards
  - 15ft HDMI Cable
#### Software
- Raspbian Stretch
- Custom Python/Pygame application
  - Music interface
  - Camera feed
  - Settings (wifi, restart, and shutdown)
- RetroPie install (currently running only a PS1 emulator)

## Planned Features (Near future)
#### Hardware
- MCP3008 ADC
  - Temperature sensor
- USB Microphone
- Adafruit Ultimate GPS Hat
#### Software
- Read from ADC
  - Steering wheel button control
  - Battery (alternator) voltage
  - Temperature sensor
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
> Note: You will also need a microSD card for the Raspberry Pi. Buy whatever size and brand fits you. This was tested with a 16GB microSD card (8GB might work). A wall power supply is recommended for setup and testing, but is not required (the Amp2 has a built-in power supply that will work as long as everything is connected properly).

The hardware setup is straightforward:
1. Screw the standoffs onto the Amp2. Place the male side of the standoffs through the Amp2 so the female side rests against the Raspberry Pi.
2. Plug the Amp2 into the GPIO header of the Raspberry Pi
3. Connect one of the ribbon cables to each HDMI plug
4. Connect the other ribbon cable to each USB plug
5. Plug in the HDMI cable to the Raspberry Pi and the display (with the right-angle connector connected to the display)
6. Connect the USB cable to the Raspberry Pi and the display (with the right-angle Micro USB connector connected to the display)
7. Connect the + and - wires for each speaker to the Amp2
8. Connect the 12V and GND wires from your car to the Amp2

> Note: If you are connecting four speakers to the system, you will need to run them in parallel or series. With 4Ω speakers, connect the left speakers together in series (+ to -), which connects to the left channel, and the right speakers together in series, which connects to the right channel. With 8Ω speakers, connect the left speakers together in parallel (+ to +; - to -), which both connect to the left channel, and the right speakers together in parallel, which both connect to the right channel.
> <br/> ![Parallel or Series Speakers](https://qph.fs.quoracdn.net/main-qimg-7294d343ed91f1c92c748c4abb63e1b2)
> <br/> (Stolen from Quora: https://www.quora.com/How-do-I-properly-connect-3-speakers-in-parallel-series. Just follow the diagram for wiring two speakers per channel or read the answer if you need to wire three per channel)

#### Software
There is not an easy setup package ready yet, but you may clone this repository and run init.py. Make sure you have *mplayer* installed.

## Advanced Setup
This will describe the hardware and software steps for going beyond just the Pi, a touchscreen, and the amp.

#### Hardware
Right now the only "advanced" feature is the backup camera, which was recently added to my car (and the software package).

| Name | Source | Price | Link |
|---|---|---|---|
| SainSmart NoIR 175* Wide-Angle Camera | Amazon | $30 | https://www.amazon.com/SainSmart-Camera-Module-Angle-Raspberry/dp/B075WT43CC |
| Arducam CSI to HDMI Cable Extension | Amazon | $14 | https://www.amazon.com/Arducam-Extension-Module-Raspberry-Specific/dp/B06XDNBM63 |
| AmazonBasics 15ft HDMI Cable | Amazon | $11 | https://www.amazon.com/AmazonBasics-Rated-Wall-Installation-Cable/dp/B014I8TOTC |

> Note: Any HDMI cable should work, but I need one that is 15ft long. I will test this and a few other cables and update this file with my results.
> 
> I have tested the AmazonBasics cable listed above and it worked well. Only thing to note about the cable is it is rather thick, heavy, and hard to bend/shape. Keep this in mind if you will need to make tight bends.

This will add $55 to the price (entirely from Amazon), but it could vary depending on the HDMI cable you choose to buy.
