from cProfile import label
from cgitb import text
from distutils.cmd import Command
from tkinter import *
import tkinter as Tk
from turtle import back, bgcolor
from tkmacosx import Button
from PIL import ImageTk, Image

root = Tk.Tk()
title = root.title("Home")
root.resizable
root.state("zoomed")
root.configure(background="#000030")


def openMarvel():
    newWindow = Toplevel(root)
    width = newWindow.winfo_screenwidth()
    height = newWindow.winfo_screenheight()
    newWindow.title("Marvel Comics")
    newWindow.resizable
    newWindow.geometry("%dx%d" % (width, height))


def openDC():
    newDCWindow = Toplevel(root)
    width = newDCWindow.winfo_screenwidth()
    height = newDCWindow.winfo_screenheight()
    newDCWindow.title("DC Comics")
    newDCWindow.resizable
    newDCWindow.geometry("%dx%d" % (width, height))


# Create Images
marvelPic = Image.open("Marvel.jpeg")
DCpic = Image.open("DC.jpeg")
valiantpic = Image.open("Valiant.jpeg")
darkhorsePic = Image.open("DarkHorse.jpeg.png")
resizedDarkhorsePic = darkhorsePic.resize((250, 200))
resizedValiantPic = valiantpic.resize((350, 200))
resizedDCpic = DCpic.resize((350, 200))
resizedMarvelPic = marvelPic.resize((350, 200))

darkhorseImage = ImageTk.PhotoImage(resizedDarkhorsePic)
DCImage = ImageTk.PhotoImage(resizedDCpic)
marvelImage = ImageTk.PhotoImage(resizedMarvelPic)
valiantImage = ImageTk.PhotoImage(resizedValiantPic)

# create Labels / put on window

marvelLabel = Label(image=marvelImage).grid(row=0, column=2)
DCLabel = Label(image=DCImage).grid(row=0, column=3)
valiantLabel = Label(image=valiantImage).grid(row=0, column=4)
darkhorseLabel = Label(image=darkhorseImage).grid(row=0, column=5)

# create Buttons / put on window


MarvelButton = Button(root, text="Marvel", bg="gold",
                      fg="#000030", width=100, command=openMarvel)
MarvelButton.grid(row=1, column=2)
DCButton = Button(root, text="DC Comics",
                  bg="gold", fg="#000030", width=100, command=openDC)
DCButton.grid(row=1, column=3)
valiantButton = Button(root, text="Valiant", bg="gold",
                       fg="#000030", width=100).grid(row=1, column=4)
darkhorseButton = Button(root, text="Dark Horse", bg="gold",
                         fg="#000030", width=100).grid(row=1, column=5)


root.mainloop()
