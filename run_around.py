from microbit import *
x, y, i, w = 0, 0, 0, 0
w = 200
round = [[y, x] for x in range(5) for y in range(5) \
    if x ==0 or y == 4 ]
round += [[y, x] for x in range(4, -1, -1) \
    for y in range(4, -1, -1) if x == 4 or y == 0 if x != y]

while True:
    display.set_pixel(round[i][0], round[i][1], 9)
    if i == len(round)-1:
        i = 0
    else:
        i += 1
    sleep(w)
    display.clear()       
        