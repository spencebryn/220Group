from cgitb import text
from distutils.cmd import Command
from tkinter import *
import tkinter as Tk
from turtle import bgcolor
from tkmacosx import Button
from PIL import ImageTk, Image

root = Tk.Tk()
title = root.title("Home")
root.resizable
root.state("zoomed")
root.configure(background="#000030")

comicBookPic = Image.open("comic_book.jpeg")
resizedComicBookPic = comicBookPic.resize((200, 200))
comicBookImage = ImageTk.PhotoImage(resizedComicBookPic)

comicBookImageButton = Label(
    image=comicBookImage).grid(row=0, column=2)
comicsButton = Button(root, text="Comics", bg="gold", fg="#000030", width=100)
comicsButton.grid(row=1, column=2)
boardgamesButton = Button(root, text="Boardgames",
                          bg="gold", fg="#000030", width=100)
boardgamesButton.grid(row=0, column=3)

root.mainloop()
