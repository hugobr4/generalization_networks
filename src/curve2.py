import numpy as np
import matplotlib.pyplot as plt

def make_gauss(N, sig, mu):
    return lambda x: N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2))


def main():
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(-40, 40, 0.01)
    s = np.array([3.0, 6.5, 15.0])
    m = [0, 0, 0]
    c = ['y', 'g', 'orange']
    n = np.array([5.0, 10.0, 15.0])

    for n, sig, mu, color in zip(n, s, m, c):
        # Substitue '*10' for the cond_intensity
        gauss = make_gauss(n, sig, mu)(x)
        ax.plot(x, gauss, color, linewidth=2)

    plt.legend([f'Weak',
                f'Medium',
                f'Strong'],
                loc='best')

    plt.xlabel("∆")

    plt.show()

if __name__ == '__main__':
   main()
