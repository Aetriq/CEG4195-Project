<h1 align="center">Lightweight ESP32-based 3D Printer Nozzle Clumping Detection</h1>

<p align="center">
  CEG4195 Project <br/>
  Faculty of Electrical and Computer Engineering @   University of Ottawa
  <br/>
</p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Author-Alex%20Gordon (Aetriq on Github)-blue" alt="Author Badge"/>
  <img src="https://img.shields.io/badge/Status-In%20Development-orange" alt="Status Badge"/>
</p>

## Project Description
A very lightweight and quick nozzle based clumping detection for Klipper-based 3D printers. Unlike other print failure detecting software, this system is done at the macro nozzle level to identify and resolve potential extrusion failiures mid-print. It will check the nozzle every fixed amount of grams of filament extruded and attempt to fix itself with the components 'on hand' before automatically pausing the print and notifying the operator.

---

<p align="center">
  <img src="https://github.com/Aetriq/CEG4195-Project/blob/main/img/repo-img/topviewrender.png?raw=true" alt="Repo img" width="45%"/>
  <img src="https://github.com/Aetriq/CEG4195-Project/blob/main/img/repo-img/coolcloseuprender.png?raw=true" alt="Repo img" width="45%"/>
</p>

---

## Features
- Based on the ESP32-S based ESP32-CAM with an OV2640 Camera. Should work on any ESP32 with a camera module. Quality/FPS is not a priority here as long as the camera can take close-up shots.
- Instead of being a secondary MCU, it connects directly with the onboard moonraker API for communication.
- Very customizable firmware. Can set thresholds, custom gcode actions, etc.


## Steps to Install
Soon... 

---

## License & Academic Attribution
As stated above, this project was developed as a university project for CEG4195 at the University of Ottawa. 

The code, documentation, and assets in this repository are provided for portfolio and educational review purposes. This project **may not be explicitly shared, reproduced, or submitted as original work by others without proper attribution** to the original author. If you wish to use or build upon this work, please provide a clear reference to this repository. Please respect the academic integrity regarding plagiarism and uncredited code reuse; any repositories or reuse of my code without explicit attribution will be taken down in accordance to the University of Ottawa's [Academic Regulation A-4 – Academic Integrity and Academic Misconduct](https://www.uottawa.ca/about-us/leadership-governance/policies-regulations/a-4-academic-integrity-academic-misconduct).