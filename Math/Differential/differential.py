def differential(type,f,x0,h,k):
    diff1 = []
    diff2 = []

    if type == "forward":
        forwardDif = lambda x,k: (f(x+h(k)) - f(x))/h(k)
        forwardDif2 = lambda x,k: (forwardDif(x+h(k),k) - forwardDif(x,k))/h(k)

        for i in range(k+1):
            diff1.insert(i,forwardDif(x0,i))
            diff2.insert(i,forwardDif2(x0,i))

    if type == "backward":
        backwardDif = lambda x,k: (f(x) - f(x-h(k)))/h(k)
        backwardDif2 = lambda x,k: (backwardDif(x,k) - backwardDif(x-h(k),k))/h(k)

        for i in range(k+1):
            diff1.insert(i,backwardDif(x0,i))
            diff2.insert(i,backwardDif2(x0,i))

    if type == "centre" or type == "center":
        centreDif = lambda x, k: (f(x+h(k)) - f(x-h(k)))/2*h(k)
        centreDif2 = lambda x, k: (centreDif(x+h(k),k) - centreDif(x-h(k),k))/2*h(k)

        for i in range(k+1):
            diff1.insert(i,centreDif(x0,i))
            diff2.insert(i,centreDif2(x0,i))

    print("First Derivative (",type,")")
    print("==================================")
    for i in range(k):
        print("k=",i,":",diff1[i])

    print("\nSecond Derivative (",type,")")
    print("==================================")
    for i in range(k):
        print("k=",i,":",diff2[i])

    print("\n")

sample = lambda x: x**2 - 1
hSquence = lambda k: 10**(k*-1)

differential("forward", sample, 1, hSquence , 4)
differential("backward", sample, 1, hSquence , 4)
differential("centre", sample, 1, hSquence , 4)