import pandas as pd
import numpy as np
from tkinter import *
from mywindow import LRwindow


window = Tk() #creates a window
lrw = LRwindow(window)
window.title("House price prediction")
window.mainloop() #keeps window alive
