import tkinter as tk
from tkinter import *
from libs import file_name
from tkinter import messagebox as msg


def count_words():
    ##
    # Count words in file
    ##
    try:
        file = open(file_name.name_file)
        win = tk.Toplevel()
        win.geometry("400x200")
        win.title("Number of words")
        data = file.read()
        rm_spaces = data.replace(".", " ")
        words = len(rm_spaces.split(" "))
        text = Label(win, text="Number of words in text: ")
        text.pack()
        number_of_words = Label(win, text=words)
        number_of_words.pack()


    except IOError:
        msg.showinfo("There is no file!", "Download file...")

