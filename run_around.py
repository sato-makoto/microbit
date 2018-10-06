from microbit import *
x, y, i = 0, 0, 0
w = 50
round = [[x, y] for x in range(1,4)]
round += [[4, y] for y in range(1,4)]
round += [[x, 4] for x in range(3, 0, -1)]
round += [[0, y] for y in range(3, 0, -1)]

round.reverse()

while True:
    display.set_pixel(round[i][0], round[i][1], 9)
    if i == len(round)-1:
        i = 0
    else:
        i += 1
    sleep(w)
    display.clear()       