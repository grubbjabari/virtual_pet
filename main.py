from tkinter import *

def create_window():
    new_window = Tk()
    
window=Tk()

Button(window,text="New Window",command=create_window).pack()

window.title('Virtual World')
window.geometry("300x200")
#TODO: Create a window that is the size of a phone or youtube shorts reel
window.mainloop()