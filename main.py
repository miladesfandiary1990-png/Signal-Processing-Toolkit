import matplotlib.pyplot as plt

class Signal:
    def visualize(self, signal):
        fig, axs = plt.subplots(1, 3, figsize=(10, 8))
        for i, sig in enumerate(signal):
            x = range(len(sig))
            axs[i].plot(x, sig)
            axs[i].set_title(f'signal {i} Hz')
            axs[i].grid(True)

        plt.tight_layout()
        plt.show(block=True)
        return fig