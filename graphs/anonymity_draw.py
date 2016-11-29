import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def draw(filename):
    print "Processing data"
    data = open(filename).read().strip().splitlines()
    x = [int(line.split(",")[0]) for line in data]
    x2 = x[400000:]
    y_1 = [int(line.split(",")[1]) for line in data]
    y_1_5 = [sum(y_1[i:min(len(y_1) - 1, i+5)]) for i in range(0, len(y_1))]
    y_1_10 = [sum(y_1[i:min(len(y_1) - 1, i+10)]) for i in range(0, len(y_1))]
    y_1_20 = [sum(y_1[i:min(len(y_1) - 1, i+20)]) for i in range(0, len(y_1))]

    print "Drawing...."

    plt.hist2d(x, y_1_5, bins=40, range=[[0.0, 440000], [0.0, 100.0]])
    plt.xlabel('Block')
    plt.ylabel('Anonymity Set')
    plt.title("Anonymity Sets Since Chain Start")
    plt.show()
    plt.hist2d(x[400000:], y_1_5[400000:], bins=40, range=[[400000.0, 440000], [0.0, 100.0]])
    plt.xlabel('Block')
    plt.ylabel('Anonymity Set')
    plt.title("Anonymity Sets Since 400k")
    plt.show()

    plt.hist(y_1[400000:], bins=100, range=[0, 100])
    plt.xlabel('Anonymity Set')
    plt.ylabel('Number of Blocks')
    plt.title("Anonymity Set with Single-Block Localization")
    plt.show()
    plt.hist(y_1_5[400000:], bins=100, range=[0, 100])
    plt.xlabel('Anonymity Set')
    plt.ylabel('Number of Blocks')
    plt.title("Anonymity Set with 5-Block Localization")
    plt.show()
    plt.hist(y_1_10[400000:], bins=100, range=[0, 100])
    plt.xlabel('Anonymity Set')
    plt.ylabel('Number of Blocks')
    plt.title("Anonymity Set with 10-Block Localization")
    plt.show()
    plt.hist(y_1_20[400000:], bins=100, range=[0, 100])
    plt.xlabel('Anonymity Set')
    plt.ylabel('Number of Blocks')
    plt.title("Anonymity Set with 20-Block Localization")
    plt.show()


    print "Processing2"
    # todo check
    y_342 = [int(line.split(",")[2]) for line in data]
    y_342_5 = [sum(y_342[i:min(len(y_342) - 1, i+5)]) for i in range(400000, len(y_342))]
    y_10 = [int(line.split(",")[3]) for line in data]
    y_10_5 = [sum(y_10[i:min(len(y_10) - 1, i+5)]) for i in range(400000, len(y_10))]
    y_100 = [int(line.split(",")[4]) for line in data]
    y_100_5 = [sum(y_100[i:min(len(y_100) - 1, i+5)]) for i in range(400000, len(y_100))]
    y_1000 = [int(line.split(",")[5]) for line in data]
    y_1000_5 = [sum(y_1000[i:min(len(y_1000) - 1, i+5)]) for i in range(400000, len(y_1000))]
    y_10000 = [int(line.split(",")[6]) for line in data]
    y_10000_5 = [sum(y_10000[i:min(len(y_10000) - 1, i+5)]) for i in range(400000, len(y_10000))]


    print "Drawing2"
    plt.hist2d(x2, y_1_5[400000:], bins=40, range=[[400000.0, 440000], [0.0, 100.0]])
    plt.xlabel('Block')
    plt.ylabel('Anonymity Set')
    plt.title("5-Block Anonymity, .01 BTC")
    plt.show()

    plt.hist2d(x2, y_342_5, bins=40, range=[[400000.0, 440000], [0.0, 100.0]])
    plt.xlabel('Block')
    plt.ylabel('Anonymity Set')
    plt.title("5-Block Anonymity, .0342 BTC")
    plt.show()

    plt.hist2d(x2, y_10_5, bins=40, range=[[400000.0, 440000], [0.0, 100.0]])
    plt.xlabel('Block')
    plt.ylabel('Anonymity Set')
    plt.title("5-Block Anonymity, .1 BTC")
    plt.show()

    plt.hist2d(x2, y_100_5, bins=40, range=[[400000.0, 440000], [0.0, 100.0]])
    plt.xlabel('Block')
    plt.ylabel('Anonymity Set')
    plt.title("5-Block Anonymity, 1 BTC")
    plt.show()

    plt.hist2d(x2, y_1000_5, bins=40, range=[[400000.0, 440000], [0.0, 100.0]])
    plt.xlabel('Block')
    plt.ylabel('Anonymity Set')
    plt.title("5-Block Anonymity, 10 BTC")
    plt.show()

    plt.hist2d(x2, y_10000_5, bins=40, range=[[400000.0, 440000], [0.0, 100.0]])
    plt.xlabel('Block')
    plt.ylabel('Anonymity Set')
    plt.title("5-Block Anonymity, 100 BTC")
    plt.show()
