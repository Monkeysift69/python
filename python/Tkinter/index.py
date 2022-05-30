from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My Gui")

#Size of the window +X+Y
root.geometry("500x500+300+300")

#Second Window
myWindow = Tk()
myWindow.title("My Second Window")

# ⁡⁢⁣⁢⁡⁣⁢⁣⁡⁢⁣⁣⁡⁢⁣𝗖𝗿𝗲𝗮𝘁𝗲 𝗮 𝗹𝗮𝗯𝗲𝗹⁡⁡⁡⁡
myLabel = Label(text="Hello World",
fg = "red",
font = 20,
bg = "blue").pack()

#Text input
text = StringVar()
myText = Entry(root,textvariable=text).pack()

def showms():
    message = text.get()
    print(message)
    #Label(root,text="Hello World",bg = "red", fg="blue").pack()


# Create Button
btn1 = Button(text="Click Me",command=showms).pack()






root.mainloop()
