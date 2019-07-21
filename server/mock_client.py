import random
from time import sleep
from threading import Thread, Event

thread_stop_event = Event()


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
        # infinite loop of magical random numbers
        print("Making random walk of numbers")
        # Probability to move up
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
            print(number)
            self.app.emit('newnumber', {'number': number}, namespace='/test')
            sleep(self.delay)

    def run(self):
        self.randomNumberGenerator()