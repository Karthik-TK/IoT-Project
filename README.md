# IoT Based Global Industrial Process Monitoring through Raspberry Pi

This project demonstrates how to use Raspberry Pi for global industrial process monitoring and control using IoT. The system integrates various sensors such as temperature sensors, PIR (Passive Infrared) motion detectors, IR (Infrared) sensors for vehicle parking management, and gas leakage detection sensors. The system allows real-time monitoring and control through both a website and a mobile app.

## Tools and Technologies Used

- **Hardware**:
  - Raspberry Pi 3
  - Sensors (Temperature, PIR, IR, Gas Leakage)
  - LCD Display

- **Software**:
  - Python (for scripting on Raspberry Pi)
  - App Inventor (for mobile app development)
  - Cloud Platform (for data storage)
  
## Features

- **Industrial Process Monitoring**: Monitors various environmental and industrial parameters such as temperature, motion, gas leakage, and vehicle parking status in real-time.
- **Power Management**: Controls the lighting based on motion detection using PIR sensors to save energy.
- **Vehicle Parking Management**: Finds available parking spots in real-time using IR sensors, reducing parking time.
- **Data Storage**: All sensor data is collected, processed, and stored in the cloud, providing access from any location.
- **Website and Mobile Access**: The data from all sensors is accessible through both a web-based dashboard and a mobile application.

## Project Overview

This project uses the Internet of Things (IoT) technology to monitor and control industrial processes remotely. IoT enables devices to sense and collect data from the surrounding environment, which is then processed and made accessible online for monitoring and decision-making.

The key components of the system include:

- **Temperature Sensors**: Monitor temperature variations in industrial settings.
- **PIR Sensors**: Detect human presence and automatically turn on/off lights for energy conservation.
- **IR Sensors**: Detect available parking spaces, aiding in real-time vehicle parking management.
- **Gas Leakage Sensors**: Alert users to the presence of harmful gases in the environment.

The Raspberry Pi serves as the central hub to collect data from these sensors, which is then displayed on an LCD screen for local monitoring and stored in the cloud for remote access. Whenever a sensor detects a significant change (e.g., temperature, motion, gas leakage), the system automatically updates the data on the cloud, ensuring that real-time information is always available.

A Python script is developed for Raspberry Pi to handle sensor readings, process the data, and manage communication between the sensors, cloud, and mobile app. The mobile app (created with App Inventor) provides users with an intuitive interface to monitor and control the system from their smartphones.

## Installation and Setup

### Hardware Requirements:
- Raspberry Pi 3 or higher
- Temperature sensor (e.g., DHT11/DHT22)
- PIR motion sensor
- IR sensor for parking management
- Gas leakage sensor (MQ series)
- LCD Display
- Jumper wires and breadboard (for sensor connections)

### Software Requirements:
- Python 3.x
- App Inventor (for mobile app)
- Cloud Storage Service (e.g., Google Firebase, AWS, etc.)

### Steps:
1. **Setting up Raspberry Pi**:
   - Install Raspberry Pi OS on your Raspberry Pi.
   - Connect the sensors to the GPIO pins of the Raspberry Pi according to the sensor specifications.

2. **Install Required Python Libraries**:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
    ```
4. **Upload the Python Script**:
  - Upload the Python script to the Raspberry Pi. The script is responsible for reading sensor data and sending it to the cloud.

5. **Cloud Setup**:
  - Choose a cloud service (e.g., Google Firebase or AWS IoT) to store sensor data.
  - Set up the necessary API keys and authentication for cloud communication.

6. **Mobile App Setup**:
  - Develop the mobile app using App Inventor or download a pre-existing template.
  - Configure the app to receive data from the cloud and display the sensor readings.
  
7. **Running the System**:
  - Once everything is set up, power up the Raspberry Pi, and the system will begin monitoring the sensors, updating the cloud, and providing access via the web and mobile app.

### Data Flow Overview

- Sensor Data Collection: Sensors continuously monitor environmental conditions (temperature, motion, gas, parking spots).
- Data Processing: The Raspberry Pi processes the data using Python scripts.
- Cloud Storage: Processed data is uploaded to the cloud in real-time.
- User Access: The web interface and mobile app fetch the sensor data from the cloud for user interaction.
