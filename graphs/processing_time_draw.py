import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def draw(filename):
    print "Drawing"
    data = open(filename).read().strip().splitlines()
    x = [float(line.split(",")[0]) for line in data]
    y = [float(line.split(",")[1]) for line in data]

    print sum(y)

    plt.hist2d(x, y, bins=30, range=[[0.0, 440000.0], [0.0, 90.0]])
    plt.xlabel('Block Number')
    plt.ylabel('Processing Time (s)')
    plt.title('Full Blockchain Processing Time')
    plt.show()
    plt.hist2d(x, y, bins=30, range=[[300000.0, 440000.0], [0.0, 90.0]])
    plt.xlabel('Block Number')
    plt.ylabel('Processing Time (s)')
    plt.title('Recent Blocks Processing Time')
    plt.show()

