import numpy as np
import matplotlib.pyplot as plt

def make_gauss(N, sig, mu):
    return lambda x: N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2))

def main():
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(-40, 40, 0.01)
    s = np.sqrt([0.1, 0.5, 1, 5])
    m = [0, 0, 0, 0]
    c = ['b','r','y','g']

    for sig, mu, color in zip(s, m, c):
        gauss = make_gauss(sig, sig, mu)(x)
        ax.plot(x, gauss, color, linewidth=2)

    plt.xlim(-5, 5)
    plt.ylim(0, 0.5)
    plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best')
    plt.show()

if __name__ == '__main__':
   main()
