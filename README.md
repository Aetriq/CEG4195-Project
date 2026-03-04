<h1 align="center">Lightweight ESP32-based 3D Printer Nozzle Clumping Detection</h1>

<p align="center">
  CEG4195 Project <br/>
  Faculty of Electrical and Computer Engineering @   University of Ottawa
  <br/>
</p>
</p>

<p align="center">
 

## Project Description
A very lightweight and quick nozzle based clumping detection for Klipper-based 3D printers. Unlike other print failure detecting software, this system is done at the macro nozzle level to identify and resolve potential extrusion failiures mid-print. It will check the nozzle every fixed amount of grams of filament extruded and attempt to fix itself with the components 'on hand' before automatically pausing the print and notifying the operator.

---

## Features
- Based on the ESP32-S based ESP32-CAM with an OV2640 Camera. Should work on any ESP32 with a camera module. Quality/FPS is not a priority here as long as the camera can take close-up shots.
- Instead of being a secondary MCU, it connects directly with the onboard moonraker API for communication.
- Very customizable firmware. Can set thresholds, custom gcode actions, etc.


## Steps to Install
TBD

