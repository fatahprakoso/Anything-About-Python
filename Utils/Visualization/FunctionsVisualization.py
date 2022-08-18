import matplotlib.pyplot as plt
import numpy as np


def visualization2Variable(arangeArray, theFunc, title, imgFilePath, imgFileName):
    """2 dimensional visualization of function with 2 variable

    Args:
        arangeArray (array): [Xstart:num, Xend:num, difference:num]
        theFunc (function): the function
        title (string): title of image
        imgFilePath (string): output file path
        imgFileName (string): output file name
    """

    x = np.arange(arangeArray[0], arangeArray[1], arangeArray[2])
    y = theFunc(x)

    plt.plot(x, y, '-')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    if(imgFilePath[len(imgFileName)-1]== '/'):
        plt.savefig(imgFilePath + imgFileName)
    else :
        plt.savefig(imgFilePath + "/" + imgFileName)
