import numpy as np
import math

def hkd(vektor1,vektor2):
    return np.inner(vektor1,vektor2)

def panjang_vektor(vektor):
    return math.sqrt(np.sum(np.power(vektor,2)))

def gram_schmidt(vektor1,vektor2,vektor3):
    vektor2 -= np.multiply(vektor1,hkd(vektor1,vektor2)/panjang_vektor(vektor1)**2)
    vektor3 -= np.array(np.multiply(vektor1,hkd(vektor1,vektor3)/panjang_vektor(vektor1)**2)) + np.array(np.multiply(vektor2,hkd(vektor3,vektor2)/panjang_vektor(vektor2)**2))

    vektor1=np.divide(vektor1,panjang_vektor(vektor1))
    vektor2=np.divide(vektor2,panjang_vektor(vektor2))
    vektor3=np.divide(vektor3,panjang_vektor(vektor3))

    return vektor1,vektor2,vektor3