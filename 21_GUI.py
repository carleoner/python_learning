from tkinter import *
from PIL import Image, ImageTk

# widget classes
# label - single-line caption for other widgets, button, entry - input() alike, 
# text - multi-line entry, frame - container widget to organize other widgets
# ComboBox - selection from the list
# Checkbutton, radiobutton, PanedWindow
# Canvas - draw shapes: lines, ovals, rect
# tkMessageBox - not a widget but complete Python module - disp message, dialogs

# geometry management
# pack() -  expand (when true fills whole parent's space), 
#           fill (fill more than recquired), side (which side of the parent's space)
# grid() -  row, column, rowspan, columnspawn, sticky
# place()-  (height,width)(x,y)(relx,rely)(relheight,relwidth)(bordermode)

window = Tk()
name = Label(window, text="Hello", bg='white', fg='Blue', font=('Serif',16))

img = Image.open('../data/21_image.png')
logo = ImageTk.PhotoImage(img)
image = Label(window, image=logo)

button = Button(window, text='Start')

username = Label(window, text='Username', font=('Serif', 12))
inputBox = Entry(window)

#img.show() show an image in the system's viewer
name.pack()
image.pack()
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
button.place(x=100,y=350)
window.mainloop()