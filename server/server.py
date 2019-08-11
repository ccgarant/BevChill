"""
Flask application to print live temperature data with socket.io
Aim is to create a web app that is constantly updated with temperatures sent by the raspberry pi.
@date=July 20th, 2019
@author=henry garant
"""

import socket
from flask_socketio import SocketIO
from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

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

@socketio.on('data')
def test_data(data):
    print(data)
    socketio.emit('data', data)


if __name__ == '__main__':
	#get local ip address of this computer to use for running the server
	ip_address = socket.gethostbyname(socket.gethostname())
	print("\n\n-----------------------------------------------")
	print("SERVER IP ADDRESS: " + ip_address)
	print("-----------------------------------------------\n\n")

	socketio.run(app, host=ip_address, port=5000)