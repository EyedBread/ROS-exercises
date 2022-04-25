#!/usr/bin/env python2


import Tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import math
import time
import rospy
from std_msgs.msg import Float64

root = tk.Tk()
fig = Figure(figsize=(5, 4), dpi=100)
a = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)  



def callback(x):
    a.plot(x.data, h(x.data),'.--b')
    fig.canvas.draw()
    time.sleep(0.01)


def h(t):
    lam = lambd(t)
    return (3*(math.pi)*(math.exp(-1*lam)))

def lambd(t):
    return (5*(math.sin(2*(math.pi)*1*t)))


def _quit():
    root.quit()    
    root.destroy()  
                    
                

if __name__ == '__main__':
    root.wm_title("GUI Plot")
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    a.set_title("Live plot")
    a.set_ylabel("h(t)")
    a.set_xlabel("t")

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    button = tk.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tk.BOTTOM)

    rospy.init_node("plotter", anonymous = True)
    rospy.Subscriber('plotting', Float64, callback)
    tk.mainloop()
