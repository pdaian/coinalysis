import numpy as np
import matplotlib.pyplot as plt
from pylab import *


def draw(filename, color='blue'):
    print "Drawing1"
    data = open(filename).read().strip().splitlines()
    x = [float(line) for line in data if len(line) > 1]

    print "Drawing2"
    plt.hist(x, 50, range=(10, 1000), color=color)
    plt.xlabel('Transaction Amount')
    plt.ylabel('Number of Transactions')
    plt.show()
    plt.hist(x, 50, color=color)
    plt.xlabel('Transaction Amount')
    plt.ylabel('Number of Transactions')
    plt.show()
    plt.hist(x, 50, range=(0.01, 10), color=color)
    plt.xlabel('Transaction Amount')
    plt.ylabel('Number of Transactions')
    plt.show()
    plt.hist(x, 50, range=(0.01, 100), normed=True, color=color)
    plt.xlabel('Transaction Amount')
    plt.ylabel('Percentage of Transactions')
    plt.show()

    

