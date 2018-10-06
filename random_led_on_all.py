from microbit import *
import random

sleep_time = 150

def rand_on(led):
    while len(led) != 0:
        on = random.randint(0,len(led)-1)
        point = led.pop(on)
        display.set_pixel(point[0], point[1], 9)
        sleep(sleep_time)

while True:
    all_led = [[x,y] for x in range(5) for y in range(5)]
    rand_on(all_led)
    sleep(sleep_time)
    display.clear()