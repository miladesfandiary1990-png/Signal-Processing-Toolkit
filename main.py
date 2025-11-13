from math import sin
import numpy as np
class Signal:
    def __init__(self):
        pass    
    def generate(self, frequency,sample=1000):
        return(np.sin(frequency*np.array(range(sample))))
    def visualize (self):
        pass
    def add_noise(self):
        pass
s1=Signal()
print(s1.generate(10))