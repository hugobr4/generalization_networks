import numpy as np
import matplotlib.pyplot as plt

def make_gauss(N, sig, mu):
    return lambda x: N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2))

def main():
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(-40, 40, 0.01)
    s = np.array([7.5, 16.25, 25])
    m = [0, 0, 0]
    c = ['y','g','orange']
    i = s/25

    for sig, mu, color in zip(s, m, c):
        # Substitue '*10' for the cond_intensity
        gauss = make_gauss(sig, sig*0.4, mu)(x)
        ax.plot(x, gauss, color, linewidth=2)

    plt.legend([f'Weak,  {i[0]}',
                f'Medium {i[1]}',
                f'Strong {i[2]}'],
                loc='best')

    plt.xlabel("∆")

    plt.show()

if __name__ == '__main__':
   main()
