"""
alganal.py
Description:
A utility program to plot algorithmic time complexity of a function.
Author: Mahesh Venkitachalam
Website: electronut.in
"""

from matplotlib import pyplot
import numpy as np
import timeit
from functools import partial
import random

def fconst(N):
    """
    O(1) function
    """
    x = 1

def flinear(N):
    """
    O(n) function
    """
    x = [i for i in range(N)]

def fsquare(N):
    """
    O(n^2) function
    """
    for i in range(N):
        for j in range(N):
            x = i*j

def fshuffle(N):
    # O(N)
    random.shuffle(list(range(N)))

def fsort(N):
    x = list(range(N))
    random.shuffle(x)
    x.sort()

def plotTC(fn, nMin, nMax, nInc, nTests):
    """
    Run timer and plot time complexity
    """
    x = []
    y = []
    for i in range(nMin, nMax, nInc):
        N = i
        testNTimer = timeit.Timer(partial(fn, N))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, 'o')
    #pyplot.legend([p1,], [fn.__name__, ])

# main() function
def main():
    print('Analyzing Algorithms...')

    plotTC(fconst, 10, 1000, 10, 10)
    plotTC(flinear, 10, 1000, 10, 10)
    plotTC(fsquare, 10, 1000, 10, 10)
    #plotTC(fshuffle, 10, 1000, 1000, 10)
    plotTC(fsort, 10, 1000, 10, 10)

    # enable this in case you want to set y axis limits
    #pyplot.ylim((-0.1, 0.5))
    
    # show plot
    pyplot.show()

# call main
if __name__ == '__main__':
    main()
