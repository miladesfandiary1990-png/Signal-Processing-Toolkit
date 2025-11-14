from math import sin
import numpy as np


class Signal:
    def __init__(self):
        pass

    def generate(self, frequency, duration, amplitude, sample_rate):
        return amplitude*np.sin(frequency * np.array(range(sample_rate * duration)))

    def visualize(self):
        pass

    def add_noise(self):
        pass


s1 = Signal()
print(s1.generate(10,2,3,100))