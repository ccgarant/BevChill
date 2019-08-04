"""
Flask application to print live temperature data with socket.io
Aim is to create a web app that is constantly updated with temperatures sent by the raspberry pi.
@date=July 20th, 2019
@author=henry garant
"""

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


@socketio.on('connect', namespace='/data')
def test_connect():
    # need visibility of the global thread object
    print('Client connected')

@socketio.on('disconnect', namespace='/data')
def test_disconnect():
    print('Client disconnected')

@socketio.on('data', namespace='/data')
def test_data(data):
    print(data)
    socketio.emit('data', data, namespace='/data')


if __name__ == '__main__':
    socketio.run(app, host="192.168.1.180", port=5000)