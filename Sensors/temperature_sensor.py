import time
import random
import json
import sys
import Sender.sender as sdr

from threading import Timer
from Sensors.sensor import Sensor

class TemperatureSensor(Sensor):
    def __init__(self, power, duty_cycle, data, message_topic, frequency_of_message):
        Sensor.__init__(self, power, duty_cycle, data, message_topic, frequency_of_message)

    def sensor_data(self):
        record_data = {'sid': self.message_topic, 'timestamp': time.ctime(time.time()), 'temperature': random.uniform(96.5, 98.7)}
        record = json.dumps(record_data)
        print("Temperature data generated")
        print("Data:", record)
        return record

    def send_data(self):
        self.data = self.sensor_data()
        # send data
        sdr.send(self.data)
        self.power = self.battery.decrease_trans_energy(sys.getsizeof(self.data))
        print("size: ", sys.getsizeof(self.data))
        print("energy level: ", self.power)


if __name__ == '__main__':
    tempsensor = TemperatureSensor(100, 30, {}, 'BodyTemperature', 1)
    tempsensor.send_data()

