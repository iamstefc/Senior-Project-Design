import smbus
import matplotlib.pyplot as plt
import time
import thread
from multiprocessing import Queue
import sys
import threading
actualdeltas = []
INTERVAL = 1

#!/usr/bin/env python

import io
import fcntl

# i2c_raw.py
# 2016-02-26
# Public Domain

I2C_SLAVE=0x0703

if sys.hexversion < 0x03000000:
   def _b(x):
      return x
else:
   def _b(x):
      return x.encode('latin-1')

class i2c:

   def __init__(self, device, bus):

      self.fr = io.open("/dev/i2c-"+str(bus), "rb", buffering=0)
      self.fw = io.open("/dev/i2c-"+str(bus), "wb", buffering=0)

      # set device address

      fcntl.ioctl(self.fr, I2C_SLAVE, device)
      fcntl.ioctl(self.fw, I2C_SLAVE, device)

   def write(self, data):
      print(type(data))
      if type(data) is list:
         data = bytearray(data)
      elif type(data) is str:
         data = _b(data)
      self.fw.write(data)

   def read(self, count):
      return self.fr.read(count)

   def close(self):
      self.fw.close()
      self.fr.close()


dev = i2c(0x44, 1) # device 0x32, bus 1
#arr = bytearray(dev.read(128))
#actualdeltas = []
#datalist=[]
li = list([])

class myThread(threading.Thread):
    def __init__(self, target, interval):
        threading.Thread.__init__(self)
        self.target = target
        self.interval = 1
        
    def run(self):
        global li
        print("read")
        #actualdeltas.append(time.clock()-target)
        if li is None:
            li = list(bytearray(dev.read(255)))
        else:
            li = list(bytearray(dev.read(255)))
        self.target = self.target+self.interval
        threading.Timer(self.target - time.clock(),self.run, []).start()
    

def work():
        global li
        #actualdeltas.append(time.clock()-target)
        if li is None:
            li = list(bytearray(dev.read(255)))
        else:
            li = list(bytearray(dev.read(255)))
        #self.target = self.target+self.interval
        #threading.Timer(self.target - time.clock(),self.run, []).start()

target = time.clock() + INTERVAL
print("start")
mythread = myThread(target, INTERVAL)
mythread.start()
l = None
while True:
    #work()
    print("plot")
    if l is not None:
        l.pop(0).remove()
    plt.gcf().canvas.flush_events()
    l = plt.plot(li)
    plt.pause(0.25)
plt.show(block = False)

"""
"""

