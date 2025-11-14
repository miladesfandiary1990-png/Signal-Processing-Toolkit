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

    def visualize(self):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)
        plt.plot(t, self.signal)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.show()
    def add_noise(self, noise_level=0.3):
        noise = noise_level * np.random.randn(len(self.signal))
        self.signal = self.signal + noise


s1 = Signal(frequency=10, amplitude=1, duration=1, sample_rate=1000)
s1.add_noise()

s2 = Signal(frequency=15, amplitude=1, duration=1, sample_rate=1000)
s2.add_noise()
s3 = Signal(frequency=5, amplitude=1, duration=1, sample_rate=1000)
s4 = Signal(frequency=2, amplitude=1, duration=1, sample_rate=1000)


s3.add_noise()
# Now works:
s5 = s1 + s2 + s3 +s4
s5.visualize()