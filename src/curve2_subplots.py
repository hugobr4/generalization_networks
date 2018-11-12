import numpy as np
import matplotlib.pyplot as plt
"""
TODO: refactor as curve3
"""


def make_gauss(N, sig, mu):
    return lambda x: N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2))


def main():
    fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, sharex=True)
    '''
    x is the x axis limits, regarding the color spectrum
    s = Std dev, will be our conditioning coefficient
    n = mean which will be our max value
    '''
    x = np.arange(-40, 40, 0.01)
    s = np.array([3, 6, 10])
    m = [0, 0, 0]
    c = ['y', 'g', 'orange']
    n = s * (2.5, 3.0, 3.5)
    #import pdb; pdb.set_trace()

    gauss = make_gauss(n[0], s[0], m[0])(x)
    ax1.plot(x, gauss, c[0], linewidth=2)
    gauss = make_gauss(n[1], s[1], m[1])(x)
    ax2.plot(x, gauss, c[1], linewidth=2)
    gauss = make_gauss(n[2], s[2], m[2])(x)
    ax3.plot(x, gauss, c[2], linewidth=2)

    plt.legend([f'Weak',
                f'Medium',
                f'Strong'],
                loc='best')

    ax1

    plt.xlabel("∆ nm")
    plt.ylabel("Response degree")

    plt.show()

if __name__ == '__main__':
   main()
