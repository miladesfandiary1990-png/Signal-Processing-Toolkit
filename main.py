from math import sin
import numpy as np


class Signal:
    def __init__(self, frequency, amplitude, duration, sample_rate):
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        self.sample_rate = sample_rate
        self.signal= generate()  
        
    def generate(self):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)
        return self.amplitude * np.sin(2 * np.pi * self.frequency * t)

    def visualize(self, x, y):
        plt.plot(x, y)
        plt.show()
    def add_noise(self):
        pass


s1 = Signal()
print(s1.generate(10))