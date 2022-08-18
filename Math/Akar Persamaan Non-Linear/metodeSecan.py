import sys
sys.path.append('Utils/Visualization')

import FunctionsVisualization as img


def newtonMethod(fx, x1, x2):
    if((x1+x2 != 0) & (x1-x2 != 0)):
        while True:
            buff = x2
            x2 = x2-(fx(x2)*(x2-x1)/(fx(x2)-fx(x1)))
            x1 = buff

            if(abs(x2-x1)/x2 < (0.0000000001)):
                break
        print(x2)
    else:
        print("Pembatas salah!")


contohFungsi = lambda x: x**7 - 1000
img.visualization2Variable(
    [0,5,0.5],
    contohFungsi,
    "Metode Secan",
    "Metnum/Akar Persamaan Non-Linear/Metode Secan",
    "metode-secan.png"
)


a = float(input("Masukkan pembatas: "))
b = float(input("Masukkan pembatas: "))


newtonMethod(contohFungsi, a, b)
