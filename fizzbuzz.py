from microbit import *
fizzbuzz = '99900:99900:90999:00990:00999:'
fizz = '09999:09000:09999:09000:09000:'
buzz = '09990:09009:09990:09009:09990:'

# maxnum = 33554432
maxnum = 30

for x in range(1,maxnum+1):
    if x % 15 == 0:
        display.show(Image(fizzbuzz))
    elif x % 5 == 0:
        display.show(Image(buzz))
    elif x % 3 == 0:
        display.show(Image(fizz))
    else:
        numstr = str(bin(x))[2:].replace('1', '9')
        emp_str = "% 25s" % numstr
        zero_str = emp_str.replace(' ', '0')
        all = zero_str[:5] + ':' + zero_str[5:10] + ':' \
            + zero_str[10:15] + ':' + zero_str[15:20] \
            + ':' + zero_str[20:] + ':'
        display.show(Image(all))
    sleep(1000)