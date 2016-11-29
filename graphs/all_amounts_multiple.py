import numpy as np
import matplotlib.pyplot as plt
from pylab import *


def draw(filename1, filename2, color=['blue', 'green']):
    print "Drawing1"
    data = open(filename1).read().strip().splitlines()
    x1 = [float(line) for line in data if len(line) > 1]
    data = open(filename2).read().strip().splitlines()
    x2 = [float(line) for line in data if len(line) > 1]

    print "Drawing2"
    plt.hist([x1, x2], 50, color=color, stacked=True)
    plt.show()
    plt.hist([x1, x2], 50, range=(0.01, 10), color=color, stacked=True)
    plt.show()
    plt.hist([x1, x2], 50, range=(0.01, 100), normed=True, color=color, stacked=True)
    plt.show()

    

