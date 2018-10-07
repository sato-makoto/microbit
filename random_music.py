from microbit import *
import music
import random
 
mlist = [
        music.DADADADUM, music.ENTERTAINER, music.PRELUDE,
        music.ODE, music.NYAN, music.RINGTONE,
        music.FUNK, music.BLUES, music.BIRTHDAY,
        music.WEDDING, music.FUNERAL, music.PUNCHLINE,
        music.PYTHON, music.BADDY, music.CHASE,
        music.BA_DING, music.WAWAWAWAA, music.JUMP_UP,
        music.JUMP_DOWN, music.POWER_UP, music.POWER_DOWN ]

while len(mlist) > 0:
    num = random.randint(0,len(mlist)-1)
    music.play(mlist[num])
    mlist.pop(num)
    sleep(300)
    display.scroll(str(len(mlist)))