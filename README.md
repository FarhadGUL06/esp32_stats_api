# ESP32 Stats API Downloader

Platform: Python Flask

Release Date: 17.04.2023

This API can update / get information stored in server
updated by my Adafruit QT Py ESP32-C3 using

  - BMI085: for accel & Gyro IMU
  - BME680: Environmental Sensor
  - LTR308: Ambient Light Sensor


# API Call

At this time, this API is locally hosted on port 5001

1. Update BME680 - Environmental Sensor information from ESP32:

http://localhost:5001/bme_update?api_key={your_api_key}&payload={your_payload}

2. Get BME680 - Environmental Sensor information from Pico in my case:

http://localhost:5001/bme_get?api_key={your_api_key}

3. Update BMI085 - Accel & Gyro IMU information from ESP32:

http://localhost:5001/bmi_update?api_key={your_api_key}&payload={your_payload}

4. Get BMI085 - Accel & Gyro IMU information from Pico in my case:

http://localhost:5001/bmi_get?api_key={your_api_key}

5. Update LTR308 - Ambient Light Sensor information from ESP32:

http://localhost:5001/ltr_update?api_key={your_api_key}&payload={your_payload}

6. Get LTR308 - Ambient Light Sensor information from Pico in my case:

http://localhost:5001/ltr_get?api_key={your_api_key}

The API Key can be stored in .env file of the project. You must create your own as:

```
API_KEY="api_test"
```

# Used resources

1. https://pythonbasics.org/flask-rest-api/

2. https://chat.openai.com/

