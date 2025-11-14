from math import sin
import numpy as np


class Signal:
    def __init__(self, frequency, amplitude, duration, sample_rate):
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        self.sample_rate = sample_rate
        self.signal= generate(frequency)  

       self.visualize(x, y)

    def generate(self, frequency, duration, amplitude, sample_rate):
        return np.sin(frequency * np.array(range(sample_rate * duration)))

    def visualize(self, x, y):
        plt.plot(x, y)
        plt.show()
    def add_noise(self):
        pass


s1 = Signal()
print(s1.generate(10))