# fastping
A python multi-threaded and multi-process implementation to check ping times and return the server with the shortest ping time

 # FastestPing
These are two different Python scripts that do the same thing in two different ways.

The MultiProcessPing.py uses true multi-processing and the pool() function to spawn processes across mutliple processors (CPU).  If you use MultiProcessPing.py, all your entry points into this script need to be protected like this:

if __name__ == "__main__":

If you dont do that, you will have errors popup for each process.

The MultiThreadPing.py uses multi-threading, which in Python only uses one processor (CPU), but multiple threads.  Using this script does not require every entry be guarded with 

if __name__ == "__main__":

### Examples
Here is an example of how to use each of these scripts:

```sh
pingServers	= {'google.com', 'yahoo.com', 'bing.com'}

import MultiProcessPing
a = MultiProcessPing.start(pingServers)

import MultiThreadPing
a = MultiThreadPing.start(pingServers)
```




