#!/usr/bin/python3

import sys 

num = len(sys.argv)
if num == 0:
    print("{} arguments.".format(num))
    print("{}: {}".format(num, sys.argv)) 
if num == 1:
    print("{} argument.".format(num))  
else:
    print("{} argument.".format(num)) 
    print("{}: {}".format(num, sys.argv)) 


    