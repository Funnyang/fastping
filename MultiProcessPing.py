#!/usr/bin/python3


pingServers	= {'yahoo.com', 'google.com', 'bing.com'}

import os, platform
from multiprocessing import Pool
from subprocess import Popen, PIPE


def ping(filename):
    base, fname = os.path.split(filename)
    if platform.system() == 'Windows':
        p = Popen(['ping', '-n', '1', filename], stdout=PIPE)
    else:
        p = Popen(['ping', '-c', '1', filename], stdout=PIPE)

    text = p.communicate()[0]
    words = text.split()
    for word in words:
        if ("time=" in str(word)) or ("time<" in str(word)):
            word=str(word).split('.')[0] # remove trailing decimals on Mac machines
            time = ''.join(filter(lambda x: x.isdigit(), str(word)))
            return (int(''.join(filter(lambda x: x.isdigit(), str(word)))), filename) # cleanse the string of anything but numbers

def start(pingServers):
    fastest = {}
    pool = Pool()
    results = pool.map(ping, pingServers)
    results = [x for x in results if x is not None] # get rid of any list elements that did not resolve
    results.sort()
    print("Sorted Results:",results)
    if len(results) > 0:
        print("Closest:",results[0])
        print(results[0][1])
    
    pool.close()
    pool.join()
    return results[0]

if __name__ == '__main__':
    #freeze_support()
    start(pingServers)
