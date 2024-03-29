"""
Flask application to print live temperature data with socket.io
Aim is to create a web app that is constantly updated with temperatures sent by the raspberry pi.
@date=July 20th, 2019
@author=henry garant
"""

import socket
import pprint
from flask_socketio import SocketIO
from flask import Flask, render_template
from Theory.peroni_bottle import peroni_bottle
from Theory.chill_timer import ChillTimer


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
chill_timer = None
calculated_chill = False

# turn the flask app into a socketio app
socketio = SocketIO(app)

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('start')
def on_start(started):
	print('Client started')
	socketio.emit('start', started)

@socketio.on('running')
def on_running(started):
	socketio.emit('running', started)

@socketio.on('data')
def test_data(data):
	
	if not calculated_chill:
		#perform Theory calculation
		global chill_timer
		chill_timer = ChillTimer(drink=peroni_bottle, start_temp=data['tempC_probe'], atm_temp=data['tempC_amb'])
		print("\nCalculated Theory\n")

	if chill_timer:
		#inject Theory calculated data
		data["theory_tempC"] = chill_timer.get_temperature_at_second(data["elapsed_time"])
		data["theory_remaining_time"] = chill_timer.get_remaining_time_until_temp(desired_temp=peroni_bottle['perfect'], curr_temp=data["tempC_probe"])
		data["chill"] = chill_timer.get_chill_zone(data['tempC_probe'])
	
	print("\nReceived Data")
	print("-----------------------------------------------")
	pprint.pprint(data)
	print("-----------------------------------------------\n")
	socketio.emit('data', data)


if __name__ == '__main__':
	#get local ip address of this computer to use for running the server
	ip_address = socket.gethostbyname(socket.gethostname())
	print("\n-----------------------------------------------")
	print("SERVER IP ADDRESS: " + ip_address)
	print("-----------------------------------------------\n")

	socketio.run(app, host=ip_address, port=5000)