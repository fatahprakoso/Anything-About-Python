
def biseksi(fx, lowerLimit, upperLimit):
    if (fx(lowerLimit)*fx(upperLimit) < 0):
        while abs(fx(lowerLimit)*fx(upperLimit)) > 0.000001:
            c = (upperLimit+lowerLimit)/2
            if (fx(upperLimit)*fx(c) < 0):
                lowerLimit = c
            else:
                upperLimit = c
        print("root: %f" % c)
    else:
        print("Error: The limits are not allowable. Please enter new limits parameter.")

