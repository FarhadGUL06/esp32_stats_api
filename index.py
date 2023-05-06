'''
My personal Youtube API used to play music
for Pico W as a mono mp3 song
'''
import os
import time
import subprocess
import importlib
import sys
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_file

load_dotenv()

api_key = os.environ.get("API_KEY")
app = Flask(__name__)
try:
    @app.route('/bme_update', methods=['GET'])
    def bme_update():
        '''
        Update current BME (Temp, Humid etc) stats
        '''
        # Secure the connection with api_key
        provided_api_key = request.args.get('api_key')
        if provided_api_key != api_key:
            return jsonify({'error': 'Invalid API key'})

        # Save the payload to local file
        try:
            payload = request.args.get('payload')
            f = open("bme_stats.txt", "w")
            f.write(payload)
            f.close()
            return jsonify({'success': 'Stats updated'})
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @app.route('/bme_get', methods=['GET'])
    def bme_get():
        '''
        Get current BME (Temp, Humid etc) stats
        '''
        # Secure the connection with api_key
        provided_api_key = request.args.get('api_key')
        if provided_api_key != api_key:
            return jsonify({'error': 'Invalid API key'})

        # Get the payload from local file
        try:
            f = open("bme_stats.txt", "r")
            payload = f.read()
            f.close()
            return jsonify({'success': payload})
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @app.route('/bmi_update', methods=['GET'])
    def bmi_update():
        '''
        Update current BME (Temp, Humid etc) stats
        '''
        # Secure the connection with api_key
        provided_api_key = request.args.get('api_key')
        if provided_api_key != api_key:
            return jsonify({'error': 'Invalid API key'})

        # Save the payload to local file
        try:
            payload = request.args.get('payload')
            f = open("bmi_stats.txt", "w")
            f.write(payload)
            f.close()
            return jsonify({'success': 'Stats updated'})
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @app.route('/bmi_get', methods=['GET'])
    def bmi_get():
        '''
        Get current BMI (gyro, acceleration) stats
        '''
        # Secure the connection with api_key
        provided_api_key = request.args.get('api_key')
        if provided_api_key != api_key:
            return jsonify({'error': 'Invalid API key'})

        # Get the payload from local file
        try:
            f = open("bmi_stats.txt", "r")
            payload = f.read()
            f.close()
            return jsonify({'success': payload})
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @app.route('/ltr_update', methods=['GET'])
    def ltr_update():
        '''
        Update current LTR (Ambient Light Sensor) stats
        '''
        # Secure the connection with api_key
        provided_api_key = request.args.get('api_key')
        if provided_api_key != api_key:
            return jsonify({'error': 'Invalid API key'})

        # Save the payload to local file
        try:
            payload = request.args.get('payload')
            f = open("ltr_stats.txt", "w")
            f.write(payload)
            f.close()
            return jsonify({'success': 'Stats updated'})
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @app.route('/ltr_get', methods=['GET'])
    def ltr_get():
        '''
        Get current LTR (Ambient Light Sensor) stats
        '''
        # Secure the connection with api_key
        provided_api_key = request.args.get('api_key')
        if provided_api_key != api_key:
            return jsonify({'error': 'Invalid API key'})

        # Get the payload from local file
        try:
            f = open("ltr_stats.txt", "r")
            payload = f.read()
            f.close()
            return jsonify({'success': payload})
        except Exception as e:
            return jsonify({'error': str(e)})

    app.run(host='0.0.0.0' , port=5001)
except OSError as app_exception:
    importlib.reload(sys)
