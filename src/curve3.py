import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

#rc('text', usetex=True)


def make_gauss(n, sig, mu):
    return lambda x: n / (sig * (2*np.pi)**.5) * np.e ** (- (x - mu)**2 / (2 * sig**2))


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    '''
    x is the x axis limits, regarding the color spectrum
    s = Std dev, will be our conditioning coefficient
    n = mean which will be our max value
    '''
    x = np.arange(-40, 40, 0.1)
    s = np.array([3.0, 6.25, 10.0])
    n = np.array([5.0, 10.0, 15.0])

    # mu is the middle of curve on the x axis. Should always be 0
    m = [0, 0, 0]
    c = ['y', 'g', 'orange']

    def plot_gauss(n, sig, mu, color):
        gauss = make_gauss(n, sig, mu)(x)
        ax.plot(x, gauss, color, linewidth=2)

    for n, sig, mu, color in zip(n, s, m, c):
        plot_gauss(n, sig, mu, color)

    plt.xlabel("Color difference (∆ nm)")
    plt.show()


if __name__ == '__main__':
    main()


#gauss = make_gauss(s[0], s[0], m[0])(x)
