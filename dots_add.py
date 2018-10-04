from microbit import *
flag = 1
while True:
    for x in range(5):
        for y in range(5):
            if flag == 1:
                flag = 0
                display.set_pixel(y, x, 9)
            else:
                display.set_pixel(x, y, 9)
                flag = 1
            sleep(100)
#            display.clear()
#    display.show(Image.HAPPY)
    sleep(1000)
    display.clear()