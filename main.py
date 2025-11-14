import numpy as np
import matplotlib.pyplot as plt

class Signal:
    def __init__(self, frequency, amplitude, duration, sample_rate):
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        self.sample_rate = sample_rate
        self.signal = self.generate()

    def generate(self):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)
        return self.amplitude * np.sin(2 * np.pi * self.frequency * t)

    def visualize(self):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)
        plt.plot(t, self.signal)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.show()

    def add_noise(self, noise_level=0.1):
        noise = noise_level * np.random.randn(len(self.signal))
        self.signal = self.signal + noise

    def combine(self, other):
        return self.signal + other.signal

    # NEW: allow s1 + s2 syntax
    def __add__(self, other):
        if not isinstance(other, Signal):
            raise TypeError("Can only add Signal objects")
        # Create a new Signal object with combined data
        new = Signal(
            frequency=self.frequency,         # placeholder — frequency doesn't matter
            amplitude=self.amplitude,
            duration=self.duration,
            sample_rate=self.sample_rate
        )
        new.signal = self.signal + other.signal
        return new


# Example usage
f1=int(input())
s1 = Signal(frequency=f1, amplitude=1, duration=1, sample_rate=1000)
print (s1.signal)
s1.visualize()
s1.add_noise()
s1.visualize()
s2 = Signal(frequency=15, amplitude=1, duration=1, sample_rate=1000)
s2.add_noise()
s3 = Signal(frequency=5, amplitude=1, duration=1, sample_rate=1000)


s3.add_noise()
# Now works:
s5 = s1 + s2 + s3
s5.visualize()
