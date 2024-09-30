
import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

max = 255
while max > 0:
    
    for i in range(10):
        cp.pixels[i] = (max, 0, 0) 
    cp.pixels.show()
    time.sleep(0.3)

    max = max - 1
