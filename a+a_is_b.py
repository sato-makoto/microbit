from microbit import *
display.show(Image.CHESSBOARD)
for x in range(10,100):
    y = x * 2
    if y > 99 \
            and str(y)[1] == str(x)[1] \
            and len ({str(x)[0], str(x)[1], str(y)[0], str(y)[2]}) == 4:
        display.scroll('{0}+{0}={1}'.format(x, y))
        sleep(1000)
display.show(Image.HAPPY)