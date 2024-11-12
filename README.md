# Raspberry Pi Pico Temperature Monitor Project

This project demonstrates an environmental monitoring system built using a **Raspberry Pi Pico**, **DHT22 sensor**, **KY-011 two-color LED**, and **KY-006 piezo buzzer**. The system collects temperature and humidity data from the DHT22 sensor and provides visual and auditory feedback based on specific environmental conditions.

## Table of Contents
- [Overview](#overview)
- [Components](#components)
- [Wiring](#wiring)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview
The goal of this project is to use a Raspberry Pi Pico to monitor and react to changes in environmental conditions (temperature and humidity) using:
- **DHT22 Sensor**: for temperature and humidity data.
- **KY-011 LED Module**: to visually indicate temperature thresholds.
- **KY-006 Piezo Buzzer**: to provide auditory alerts.

## Components
- **Raspberry Pi Pico**
- **DHT22 Temperature and Humidity Sensor**
- **KY-011 Two-color LED Module**
- **KY-006 Piezo Buzzer Module**
- Jumper wires and breadboard

## Wiring
Below is the wiring configuration for connecting the components to the Raspberry Pi Pico:

| Component        | Pico Pin (GPIO) | Notes                           |
|------------------|-----------------|---------------------------------|
| DHT22 Data Pin   | GP16            | Data pin for temperature and humidity readings |
| KY-011 LED Red   | GP15            | Red channel of the LED (high temperature)      |
| KY-011 LED Green | GP14            | Green channel of the LED (normal temperature)  |
| KY-006 Buzzer    | GP17            | Emits sound for alert notification             |
| Ground           | GND             | Common ground for all components              |
| Power (3.3V)     | 3V3             | Power supply for DHT22 and KY modules          |

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/RaspberryPiPico-EnvMonitor.git
   cd RaspberryPiPico-EnvMonitor
