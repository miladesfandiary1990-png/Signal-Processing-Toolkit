class Signal:
    def __init__(self, frequency, amplitude, duration, sample_rate):
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        self.sample_rate = sample_rate
        self.signal=generate(frequency)
    def generate(self):
        pass

    def visualize(self):
        pass

    def add_noise(self):
        pass


