import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg

from libs import file_name


def count_letters():
    ##
    # Show Window about letters in text.
    ##
    try:
        file = open(file_name.name_file)
        win = tk.Toplevel()
        win.geometry("400x200")
        win.title("Number of letters")

        data = file.read()
        letters = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y', 'B', 'b', 'C', 'c', 'D', 'd', 'F', 'f',
                   'G', 'g', 'H', 'h', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'p', 'P', 'R', 'r', 'S', 's',
                   'T', 't', 'W', 'w', 'X', 'x', 'Z', 'z']
        count = 0
        for char in data:
            if char in letters:
                count = count + 1

        text = Label(win, text="Number of letters in text: ")
        text.pack()
        number_of_letters = Label(win, text=count)
        number_of_letters.pack()

    except IOError:
        msg.showinfo("There is no file!", "Download file...")

