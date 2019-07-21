"""
Flask application to print live temperature data with socket.io
Aim is to create a web app that is constantly updated with temperatures sent by the raspberry pi.
@date=July 20th, 2019
@author=henry garant
"""

from threading import Thread

from flask_socketio import SocketIO
from flask import Flask, render_template
from mock_client import RandomTempThread


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

# turn the flask app into a socketio app
socketio = SocketIO(app)

#random temperature Generator Thread
thread = Thread()


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')


@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random temperature generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = RandomTempThread(socketio)
        thread.start()


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host='192.168.1.180', port=5000)