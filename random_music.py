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

plist = [
        'DADADADUM', 'ENTERTAINER', 'PRELUDE',
        'ODE', 'NYAN', 'RINGTONE',
        'FUNK', 'BLUES', 'BIRTHDAY',
        'WEDDING', 'FUNERAL', 'PUNCHLINE',
        'PYTHON', 'BADDY', 'CHASE',
        'BA_DING', 'WAWAWAWAA', 'JUMP_UP',
        'JUMP_DOWN', 'POWER_UP', 'POWER_DOWN' ]

while len(mlist) > 0:
    num = random.randint(0,len(mlist)-1)
    title = str(mlist[num]).replace('music.','')
    music.play(mlist.pop(num))
    sleep(300)
    display.scroll(plist.pop(num))

display.show(Image.HAPPY)