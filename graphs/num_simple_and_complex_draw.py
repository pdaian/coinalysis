import numpy as np
import matplotlib.pyplot as plt
from pylab import *


def draw(filename):
    print "Drawing"
    data = open(filename).read().strip().splitlines()
    x = [line.split(",")[0] for line in data]
    y = [line.split(",")[1] for line in data]
    plt.scatter(x, y)
    plt.show()

def draw1(filename):
    print "Drawing"
    data = open(filename).read().strip().splitlines()
    x = [int(line.split(",")[0]) for line in data]
    y = [int(line.split(",")[1]) for line in data]
    z = [int(line.split(",")[2]) for line in data]

    plt.hist2d(y, z, bins=30, range=[[20.0, 4000.0], [20.0, 200.0]])
    plt.show()
    plt.hist2d(x, y, bins=30, range=[[0.0, 440000], [0.0, 4000.0]])
    plt.show()
    plt.hist2d(x, y, bins=30, range=[[0.0, 440000], [5.0, 20000.0]])
    plt.show()
    plt.hist2d(x, z, bins=30, range=[[0.0, 440000], [0.0, 200.0]])
    plt.show()
    plt.hist2d(x, z, bins=30, range=[[0.0, 440000], [5.0, 1000.0]])
    plt.show()

draw = draw1

