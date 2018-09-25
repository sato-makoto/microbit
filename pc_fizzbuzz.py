#!/usr/bin/env python
maxnum = 2**25

for x in range(1, maxnum + 1):
    if x % 15 == 0:
        print('fizzbuzz')
    elif x % 5 == 0:
        print('buzz')
    elif x % 3 == 0:
        print('fizz')
    else:
        numstr = str(bin(x))[2:].replace('1', '9')
        emp_str = "% 25s" % numstr
        zero_str = emp_str.replace(' ', '0')
        all = zero_str[:5] + ':' +  \
                zero_str[5:10] + ':' + \
                zero_str[10:15] + ':' + \
                zero_str[15:20] + ':' + \
                zero_str[20:]
        print(all)
