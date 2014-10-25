import numpy as np
from itertools import product
import heapq
import time
import cProfile
import random

def subarray(arr, minx, maxx, miny, maxy):
    return arr[minx:maxx,miny:maxy]

def partition(num, parts):
    avg = float(num)/parts
    partitions = []
    count = 0.0
    while count < num:
        partitions.append(count)
        count += avg
    return partitions+[num]

def getpairs(lst):
    pairs = []
    for u, v in zip(lst[:-1], lst[1:]):
        pairs.append((u,v))
    return pairs

def arrayparts_(arr, xparts, yparts, evalf):
    parts = []
    xsplit = getpairs(partition(len(arr),xparts))
    ysplit = getpairs(partition(len(arr[0]), yparts))
    subarrs = product(xsplit, ysplit)
    for ((x1, x2), (y1, y2)) in subarrs:
        subarr = subarray(arr, x1, x2, y1, y2)
        score = evalf(subarr)
        parts.append(((x1, x2, y1, y2), score))
    return parts

def arrayparts(arr, xparts, yparts):
    parts = []
    xsplit = getpairs(partition(len(arr),xparts))
    ysplit = getpairs(partition(len(arr[0]), yparts))
    subarrs = product(xsplit, ysplit)
    for ((x1, x2), (y1, y2)) in subarrs:
        subarr = subarray(arr, x1, x2, y1, y2)
        parts.append((subarr, (x1, x2, y1, y2)))
    return parts

def selmax(parts, num = None):
    if not num:
        num = max(1,len(parts)/5)
    return [val for val in heapq.nlargest(num, parts, key = lambda x: x[1]) if val[1]]

def sqsum(arr): #0.67
    return np.sum(arr**2)

def approxsum(arr, sponge = 10): #0.67
    return np.sum(arr[::sponge, ::sponge])

def rowsum(arr, sponge = 10): #0.57
    return np.sum(arr[::sponge])

def replacearr_(oarr, narr, xparts, yparts, selectf = selmax, evalf = rowsum):
    darr = np.absolute(narr-oarr) #ohh
    parts = arrayparts(darr, xparts, yparts, evalf)
    replparts = selectf(parts)
    return [(subarray(narr, *part), part) for part, score in replparts]

rats = [0, 0, 0]
def replacearr(oarr, narr, xparts, yparts, selectf = selmax, evalf = approxsum):
    global rats
    one = time.time()
    oparts = arrayparts(oarr, xparts, yparts)
    nparts = arrayparts(narr, xparts, yparts)
    two = time.time()
    parts = []
    for (opart, p1), (npart, p2) in zip(oparts, nparts):
        diff = (evalf(npart)-evalf(opart))**2 
        parts.append((p1, diff))
    three = time.time()
    replparts = selectf(parts)
    four = time.time()
    rats[0] += two-one
    rats[1] += three-two
    rats[2] += four-three
    #print rats
    return [(subarray(narr, *part), part) for part, score in replparts]

#arr1 = np.zeros((1000,2000))
#arr2 = np.random.randint(0, 256**3-1, size = (1000,2000))
#cProfile.run('''
#for x in xrange(100):
#    parts = replacearr(arr1, arr2, 20, 10)
#''')
#
#print rats
