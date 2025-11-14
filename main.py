import numpy as np
import matplotlib.pyplot as plt
class Signal:
    def __init__(self, frequency, amplitude, duration, sample_rate):
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        self.sample_rate = sample_rate
        self.signal=generate()
    def generate(self):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)
        return self.amplitude * np.sin(2 * np.pi * self.frequency * t)

    def visualize(self, signal):
        fig, axs = plt.subplots(1, 3, figsize=(10, 8))
        for i in signal in enumerate(signals):
        x = range(len(signal))
        axs[i].plot(x. signal)
        axs[i].set_title(f'signal {signal(i).frequency} Hz')
        axs[i].grid(True)

    plt.tight_layout()
    plt.show()
