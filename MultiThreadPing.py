#!/usr/bin/python3

pingServers	= {'yahoo.com', 'google.com', 'bing.com'}

import os, platform
from threading import Thread
from subprocess import Popen, PIPE


def ping(filename, results):
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
            results.append((int(''.join(filter(lambda x: x.isdigit(), str(word)))),filename))
            return (int(''.join(filter(lambda x: x.isdigit(), str(word)))), filename) # cleanse the string of anything but numbers

def start(pingServers):
    results = []
    fastest = {}
    threadList = []
    for i in pingServers:
        t = Thread(target=ping, args=(i,results))
        t.start()
        threadList.append(t)
    
    for t in threadList:
        t.join()
    results = [x for x in results if x is not None] # get rid of any list elements that did not resolve
    results.sort()
    print("Sorted Results:",results)
    if len(results) > 0:
        print("Closest:",results[0])
        print(results[0][1])
    return results[0]

if __name__ == '__main__':
    #freeze_support()
    start(pingServers)
