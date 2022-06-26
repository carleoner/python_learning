from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def gui():

    def greetUser(event):
        username = inputBox.get()
        greet['text'] = 'Welcome ' + username

    def showMessage():
        messagebox.showinfo(title="Learn Everyday", message="Welcome " + inputBox.get())

    window = Tk()
    name = Label(window, text="Learn Everyday", fg="Blue", font=('Serif', 16))
    img = Image.open('../data/21_image.png')
    logo = ImageTk.PhotoImage(img)
    image = Label(window, image=logo)

    frame = Frame(window)
    username = Label(frame, text="Username", font=('Serif',12))
    inputBox = Entry(frame)
    button = Button(window, text="Login", command=showMessage)
    button1 = Button(window, text="Start")
    button1.bind('<Button-1>', greetUser)
    greet = Label(window)

    name.pack()
    #image.pack()
    frame.pack()
    username.pack()
    inputBox.pack()
    button.pack()
    button1.pack()
    greet.pack()
    window.mainloop()

if __name__ == '__main__':
    gui()
