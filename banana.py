# ここにコードを書いてね :-)
from microbit import *
# バナナ + バナナ = シナモン
# a: バ b:ナ c:シ d:モ e:ン

def calc():
    c = 1
    for a in range(1, 10):
        for b in range(10):
            for d in range(10):
                for e in range(10):
                    check = {a, b, c, d, e}
                    banana = a * 100 + b * 10 + b
                    answer = 1000 + b * 100 + d * 10 + e
                    if banana * 2 == answer and len(check) == 5:
                        b2 = str(banana) + ' + ' + str(banana)
                        all = b2 + ' = ' + str(answer)
                        display.scroll(all)

display.show(Image.CHESSBOARD)
while True:
    if button_a.was_pressed():
        display.clear()
        calc()
        display.show(Image.HAPPY)
        sleep(2000)
        display.clear()
    display.show(Image.CHESSBOARD)