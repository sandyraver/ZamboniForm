#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Apr 29, 2017 06:14:03 AM
#    Apr 29, 2017 06:23:01 AM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    global flood
    flood = StringVar()
    global dry
    dry = StringVar()
    global edge
    edge = StringVar()
    global threeLap
    threeLap = StringVar()
    global wash
    wash = StringVar()
    global wet
    wet = StringVar()
    global centerFlood
    centerFlood = StringVar()
    global rink1
    rink1 = StringVar()
    global Recent_Resurfaces
    Recent_Resurfaces = StringVar()
    global rink2
    rink2 = StringVar()
    global boardBrush
    boardBrush = StringVar()
    global dateStr
    dateStr = StringVar()
    global timeStr
    timeStr = StringVar()
    global timeStr
    timeStr = StringVar()
    global dumpStr
    dumpStr = StringVar()
    global tempStr
    tempStr = StringVar()
    global humidStr
    humidStr = StringVar()
    global commStr
    commStr = StringVar()
    global initStr
    initStr = StringVar()
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import zamtest
    zamtest.vp_start_gui()
