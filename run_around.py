from microbit import *
x, y, i, w = 0, 0, 0, 0
w_ori = 800
round = [[x, y] for x in range(5)]
round += [[4, y] for y in range(5)]
round += [[x, 4] for x in range(4, -1, -1)]
round += [[0, y] for y in range(4, -1, -1)]
while True:
    if round[i] == [0, 0] \
            or round[i] == [0, 4] \
            or round[i] == [4, 0] \
            or round[i] == [4, 4]:
        w = w_ori/2
    else:
        w = w_ori
    display.set_pixel(round[i][0], round[i][1], 9)
    if i == 19:
        i = 0
    else:
        i += 1
    sleep(w)
    display.clear()       
        