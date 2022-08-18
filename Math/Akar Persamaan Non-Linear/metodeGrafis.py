import numpy as np
import matplotlib.pyplot as plt


def metodeGrafik(arangeArray, theFunc, imgFileName):
    x = np.arange(arangeArray[0], arangeArray[1], arangeArray[2])
    y = theFunc(x)

    plt.plot(x, y, '-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.savefig(imgFileName)


metodeGrafik([0.1, 2, 0.1], lambda x: x**3 - 2 *
             (x**2) + 6*x - 4, "Metnum/Akar Persamaan Non-Linear/Metode Grafik/metode-grafis.png")
