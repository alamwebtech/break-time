# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 22:58:16 2018

@author: ferar
"""
import time
import webbrowser

total_break = 3
break_count = 0

print("This programe will start on " + time.ctime())

while(break_count <total_break):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")
    break_count = break_count +1