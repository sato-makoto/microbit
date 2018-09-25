#!/usr/bin/env python
maxnum = 2**25

for x in range(maxnum):
        numstr = str(bin(x))[2:].replace('1', '9')
        emp_str = "% 25s" % numstr
        zero_str = emp_str.replace(' ', '0')
        all = zero_str[:5] + ':' +  \
                zero_str[5:10] + ':' + \
                zero_str[10:15] + ':' + \
                zero_str[15:20] + ':' + \
                zero_str[20:]
        print(all)
