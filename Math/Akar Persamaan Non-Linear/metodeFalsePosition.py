import sys
sys.path.append('Utils/Visualization')

import FunctionsVisualization as img


def falsePosition(fx, lowerLimit, upperLimit):
    if (fx(lowerLimit)*fx(upperLimit) < 0 and lowerLimit+upperLimit != 0):
        c = 0
        while True:
            buff = c
            # perbedaan dengan metode biseksi terletak pada penentuan nilai c
            c = upperLimit - (fx(upperLimit)*(lowerLimit-upperLimit)
                              )/(fx(lowerLimit)-fx(upperLimit))
            if (fx(upperLimit)*fx(c) < 0):
                lowerLimit = c
            else:
                upperLimit = c

            if (abs((c-buff)/c) < (0.001)):
                break
        print("Akar persamaannya adalah %f" % c)
    else:
        print("Batasan yang dimasukkan salah!")


contohFungsi = lambda x: x**3 - 2*(x**2) + 6*x - 4.0

img.visualization2Variable(
    [0.6, 1.5, 0.05],
    contohFungsi,
    "Metode False Position",
    "Metnum/Akar Persamaan Non-Linear/Metode False Position/",
    "metode-false-position.png"
)

a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas : "))


falsePosition(contohFungsi, a, b)
