import numpy as np
import matplotlib.pyplot as plt

def make_gauss(N, sig, mu):
    return lambda x: N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2))

def main():
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(-40, 40, 0.01)
    s = np.sqrt([0.1, 0.5, 1])
    m = [0, 0, 0]
    c = ['y','g','orange']

    for sig, mu, color in zip(s, m, c):
        # Substitue '*10' for the cond_intensity
        gauss = make_gauss(sig, sig*10, mu)(x)
        ax.plot(x, gauss, color, linewidth=2)

    plt.legend(['Weak', 'Medium', 'Strong'], loc='best')
    plt.show()

if __name__ == '__main__':
   main()
