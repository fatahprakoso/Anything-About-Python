import sys
sys.path.append('Utils/Visualization')

import FunctionsVisualization as img


def newtonMethod(fx, difFx, x):
    while True:
        x0 = x
        fxr = fx(x)
        diffFxr = difFx(x)
        x -= x0-(fxr/diffFxr)

        if(abs(x-x0)/x < (0.0000000001)):
            break
    print(x)


contohFungsi = lambda x: x**7 - 1000
difFx = lambda x: 7*x**6

img.visualization2Variable(
    [0,5,0.5],
    contohFungsi,
    'Metode Newton',
    'Metnum/Akar Persamaan Non-Linear/Metode Newton',
    'metode-newton.png'
)

a = float(input("Masukkan pembatas: "))

newtonMethod(contohFungsi, difFx, a)
