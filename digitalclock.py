from tkinter import *
from time import strftime 
root = Tk()
root.title('DigitalClock') 

 
#%I is a directive that tells Python to give the hour in the 12-hour format
#%H is  a directive that tells Python to give the hour in the 24-hour format
#Additionally, you may include the %p directive which will display “AM” or “PM”.
 
def time(): 
    string = strftime('%I:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'black', 
            foreground = 'white') 

lbl.pack(anchor = 'center') 
time() 
  
mainloop()
