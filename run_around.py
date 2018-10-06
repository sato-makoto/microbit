from microbit import *
s = 200

while True:
    for x in range(0,5):
        display.set_pixel(x,0,9)
        sleep(s)
        display.set_pixel(x,0,0)
    for y in range(0,5):
        display.set_pixel(x,y,9)
        sleep(s)
        display.set_pixel(x,y,0)
    for x in range(4,-1,-1):
        display.set_pixel(x,y,9)
        sleep(s)
        display.set_pixel(x,y,0)
    for y in range(4,-1,-1):
        display.set_pixel(x,y,9)
        sleep(s)
        display.set_pixel(x,y,0)