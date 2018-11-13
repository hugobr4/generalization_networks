import random
import numpy as np

def make_gauss(N, sig, mu):
    return lambda x: N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2))


c_color = random.randrange(430, 771)

c_intensity = np.random.choice((1.0, 1.25, 1.5))

delta = np.random.choice(range(-40, 41))
