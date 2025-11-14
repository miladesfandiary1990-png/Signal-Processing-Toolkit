import matplotlib.pyplot as plt
class Signal:
    def visualize(self, signal):
        fig, axs = plt.subplots(1, 3, figsize=(10, 8))
        for i in signal in enumerate(signals):
        x = range(len(signal))
        axs[i].plot(x. signal)
        axs[i].set_title(f'signal {signal(i).frequency} Hz')
        axs[i].grid(True)

    plt.tight_layout()
    plt.show()