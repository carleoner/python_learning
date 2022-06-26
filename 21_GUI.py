from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

########################################################
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
#
########################################################

window = Tk()
name = Label(window, text="Hello", bg='white', fg='Blue', font=('Serif',16))

img = Image.open('../data/21_image.png')
logo = ImageTk.PhotoImage(img)
image = Label(window, image=logo)

frame = Frame(window)
button = Button(frame, text='Start')

username = Label(frame, text='Username', font=('Serif', 12))
inputBox = Entry(frame)

#img.show() show an image in the system's viewer
name.pack()
image.pack()
frame.pack()
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
button.pack()
window.mainloop()

########################################################

window1 = Tk()
frame = Frame(window1)
lbl = Label(frame, text="Inside lbl")
btn = Button(frame, text="Inside btn")
frame.pack()
lbl.pack(side=TOP)
btn.pack(side=BOTTOM)
window1.mainloop()

########################################################

window2 = Tk()
lbl = Label(window2, text="Choose ur fav language")
frame = Frame(window2)
python = Checkbutton(frame, text="Python", state=DISABLED)
french = Checkbutton(frame, text="French")
python.select()

label = Label(frame)
def sel():
   selection = "You selected a " + str(var.get())
   label.config(text = selection)
   if str(var.get()) == "dog":
    messagebox.showwarning(title="Question", message="Hot Dog")

var = StringVar()
cat = Radiobutton(frame, text="cat", variable=var, value="cat", command=sel)
dog = Radiobutton(frame, text="dog", variable=var, value="dog", command=sel)

lbl.pack()
frame.pack()
python.pack()
french.pack()
cat.pack()
dog.pack()
label.pack()
window2.mainloop()