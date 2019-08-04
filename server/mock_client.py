import random
from time import sleep
from threading import Thread, Event

thread_stop_event = Event()
app = None

class RandomTempThread(Thread):
    def __init__(self, app):
        self.delay = 1
        self.app = app
        super(RandomTempThread, self).__init__()

    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread
        """
        prob = 0.5
        last_temp = 75

        while not thread_stop_event.isSet():
            rand_point = random.uniform(0, 1)
            number = last_temp
            if rand_point < prob:
                number -= 2 * rand_point
            else:
                number += 2 * rand_point - prob
            number = round(number, 2)
            data = {
                "time_stamp": '07/26/19 18:41:31',
                "elapsed_time": 1.885,
                "tempC_probe": 21.875,
                "tempF_probe": number,
                "tempC_amb": 24.0,
                "tempF_amb": 75.2,
                "tempC_humidity": 52.0
            }

            self.app.emit('data', data, namespace='/data')
            sleep(self.delay)

    def run(self):
        self.randomNumberGenerator()