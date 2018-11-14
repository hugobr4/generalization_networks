import numpy as np
import matplotlib.pyplot as plt


def make_gauss(N, sig, mu):
    return lambda x: N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2))


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid(alpha=0.5, linestyle='--')

    '''
    x is the x axis limits, regarding the color spectrum
    s = Std dev, will be our conditioning coefficient
    n = mean which will be our max value
    i = intesity of conditioning. Will modify our mean
    '''

    x = np.arange(-50, 50, 0.01)
    m = [0, 0, 0]
    c = ['y', 'g', 'orange']
    s = np.sqrt([14, 14, 14])
    s = i * 2
    n = s * i

    import pdb; pdb.set_trace()
    for n, sig, mu, color in zip(n, s, m, c):
        gauss = make_gauss(n, sig, mu)(x)
        ax.plot(x, gauss, color, linewidth=3)

    plt.legend([f'Weak',
                f'Medium',
                f'Strong'],
                loc='best')

    plt.xlabel("∆ nm")
    plt.ylabel("Response degree")

    plt.title("Gaussian fit for distribution")

    plt.show()


if __name__ == '__main__':
   main()
