import string
import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg

from libs import file_name


def count_punctuation_marks():
    ##
    # Count punctuation marks in file
    ##
    try:
        file = open(file_name.name_file)
        win = tk.Toplevel()
        win.geometry("400x200")
        win.title("Number of punctuation marks")
        data = file.read()

        punctuation_marks = 0
        for char in data:
            if char in string.punctuation:
                punctuation_marks = punctuation_marks + 1

        text = Label(win, text="Number of punctuation marks in text: ")
        text.pack()
        number_of_punctuation_marks = Label(win, text=punctuation_marks)
        number_of_punctuation_marks.pack()
    except IOError:
        msg.showinfo("There is no file!", "Download file...")

